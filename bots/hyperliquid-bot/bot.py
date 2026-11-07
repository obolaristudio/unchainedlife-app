"""Bot de tendência EMA 20/50 para a Hyperliquid.

Uso:
    python bot.py            # loop contínuo (use DRY_RUN=true primeiro)
    python bot.py --once     # roda um ciclo e sai (teste rápido)

Proteções:
- DRY_RUN=true por padrão: só registra o que faria.
- Toda entrada sai com STOP e ALVO na corretora (não depende do bot estar ligado).
- Para de abrir operações no dia se o capital cair DAILY_LOSS_LIMIT.
- Não mexe em posição que ele não abriu (ex.: trade manual).
"""
import argparse
import json
import logging
import os
import sys
import time
from datetime import datetime, timezone

import eth_account
from hyperliquid.exchange import Exchange
from hyperliquid.info import Info

import config
from market import base_url, fetch_candles, round_px, round_sz
from strategy import check_signal, position_size

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout), logging.FileHandler("bot.log")],
)
log = logging.getLogger("hl-bot")


# --- estado persistente -------------------------------------------------------
def load_state() -> dict:
    if os.path.exists(config.STATE_FILE):
        with open(config.STATE_FILE) as f:
            return json.load(f)
    return {"last_candle": 0, "day": "", "day_start_equity": 0.0, "bot_position": False}


def save_state(s: dict) -> None:
    with open(config.STATE_FILE, "w") as f:
        json.dump(s, f, indent=2)


# --- helpers de conta -----------------------------------------------------
def account_snapshot(info: Info, addr: str, coin: str):
    st = info.user_state(addr)
    equity = float(st["marginSummary"]["accountValue"])
    szi = 0.0
    for ap in st["assetPositions"]:
        if ap["position"]["coin"] == coin:
            szi = float(ap["position"]["szi"])
    return equity, szi


def cancel_coin_orders(ex: Exchange, info: Info, addr: str, coin: str) -> None:
    for o in info.open_orders(addr):
        if o["coin"] == coin:
            ex.cancel(coin, o["oid"])
            log.info("Ordem pendente cancelada: oid=%s", o["oid"])


def ok(resp) -> bool:
    if not resp or resp.get("status") != "ok":
        log.error("Resposta com erro: %s", resp)
        return False
    for s in resp["response"]["data"].get("statuses", []):
        if isinstance(s, dict) and "error" in s:
            log.error("Ordem rejeitada: %s", s["error"])
            return False
    return True


# --- ciclo principal ----------------------------------------------------------
def cycle(info: Info, ex, state: dict, sz_dec: int) -> None:
    addr = config.ACCOUNT_ADDRESS
    coin = config.COIN
    equity, szi = account_snapshot(info, addr, coin)

    today = datetime.now(timezone.utc).date().isoformat()
    if state["day"] != today:
        state["day"], state["day_start_equity"] = today, equity
        log.info("Novo dia (UTC). Capital inicial do dia: $%.2f", equity)

    # posição fechada por stop/alvo -> limpa ordem órfã
    if szi == 0 and state["bot_position"]:
        log.info("Posição encerrada (stop ou alvo atingido).")
        state["bot_position"] = False
        if ex:
            cancel_coin_orders(ex, info, addr, coin)

    if szi != 0 and not state["bot_position"]:
        log.warning("Existe posição em %s que o bot NÃO abriu. Nada será feito.", coin)
        return

    candles = fetch_candles(info, coin, config.INTERVAL, config.EMA_SLOW * 4)
    last = candles[-1]
    if last.t == state["last_candle"]:
        return  # ainda no mesmo candle
    state["last_candle"] = last.t

    sig = check_signal(candles, config.EMA_FAST, config.EMA_SLOW,
                       config.ATR_PERIOD, config.SL_ATR_MULT, config.RR)
    log.info("Candle %s fechado em $%.1f | capital $%.2f | posição %s | sinal: %s",
             config.INTERVAL, last.c, equity, szi, sig.side if sig else "nenhum")
    if not sig:
        return

    current_side = "long" if szi > 0 else "short" if szi < 0 else None
    if current_side == sig.side:
        return

    # sinal contrário: fecha a atual
    if current_side:
        log.info("Sinal contrário -> fechando %s", current_side)
        if ex:
            cancel_coin_orders(ex, info, addr, coin)
            if not ok(ex.market_close(coin, slippage=config.SLIPPAGE)):
                return
        state["bot_position"] = False
        equity, _ = account_snapshot(info, addr, coin)

    # limite de perda diária
    floor = state["day_start_equity"] * (1 - config.DAILY_LOSS_LIMIT)
    if equity < floor:
        log.warning("Limite de perda diária atingido ($%.2f < $%.2f). Sem novas entradas hoje.",
                    equity, floor)
        return

    size = round_sz(position_size(equity, sig.entry, sig.stop,
                                  config.RISK_PER_TRADE, config.MAX_LEVERAGE), sz_dec)
    if size * sig.entry < config.MIN_NOTIONAL_USD:
        log.warning("Capital insuficiente para o valor mínimo de ordem ($%.2f).", size * sig.entry)
        return

    is_buy = sig.side == "long"
    risk_usd = abs(sig.entry - sig.stop) * size
    log.info("ENTRADA %s %s %s @~$%.1f | stop $%.1f | alvo $%.1f | risco ~$%.2f",
             sig.side.upper(), size, coin, sig.entry, sig.stop, sig.take, risk_usd)
    if not ex:
        log.info("[DRY_RUN] Nenhuma ordem enviada.")
        return

    ex.update_leverage(config.MAX_LEVERAGE, coin, is_cross=False)
    resp = ex.market_open(coin, is_buy, size, slippage=config.SLIPPAGE)
    if not ok(resp):
        return
    filled = resp["response"]["data"]["statuses"][0].get("filled")
    if not filled:
        log.error("Ordem não executada: %s", resp)
        return
    avg = float(filled["avgPx"])
    fsz = float(filled["totalSz"])
    shift = avg - sig.entry  # mantém as distâncias de stop/alvo a partir do preço real
    stop, take = sig.stop + shift, sig.take + shift
    state["bot_position"] = True
    log.info("Executado: %s %s @ $%.1f", fsz, coin, avg)

    for kind, px in (("sl", stop), ("tp", take)):
        trig = round_px(px, sz_dec)
        worst = round_px(px * (1 - config.SLIPPAGE if is_buy else 1 + config.SLIPPAGE), sz_dec)
        r = ex.order(coin, not is_buy, fsz, worst,
                     {"trigger": {"triggerPx": trig, "isMarket": True, "tpsl": kind}},
                     reduce_only=True)
        if ok(r):
            log.info("%s colocado em $%s", "STOP" if kind == "sl" else "ALVO", trig)
        elif kind == "sl":
            log.error("FALHA AO COLOCAR STOP -> fechando posição por segurança.")
            ex.market_close(coin, slippage=config.SLIPPAGE)
            state["bot_position"] = False
            return


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--once", action="store_true")
    once = p.parse_args().once

    if not config.ACCOUNT_ADDRESS:
        sys.exit("Defina HL_ACCOUNT_ADDRESS no .env")
    url = base_url(config.TESTNET)
    info = Info(url, skip_ws=True)
    ex = None
    if not config.DRY_RUN:
        if not config.API_SECRET:
            sys.exit("Defina HL_API_SECRET no .env (chave da API Wallet)")
        wallet = eth_account.Account.from_key(config.API_SECRET)
        ex = Exchange(wallet, url, account_address=config.ACCOUNT_ADDRESS)

    sz_dec = next(a["szDecimals"] for a in info.meta()["universe"] if a["name"] == config.COIN)
    log.info("Bot iniciado | %s %s | EMA %s/%s | %sx | risco %.0f%%/trade | %s | %s",
             config.COIN, config.INTERVAL, config.EMA_FAST, config.EMA_SLOW,
             config.MAX_LEVERAGE, config.RISK_PER_TRADE * 100,
             "TESTNET" if config.TESTNET else "MAINNET",
             "DRY_RUN (simulação)" if config.DRY_RUN else "AO VIVO")

    state = load_state()
    while True:
        try:
            cycle(info, ex, state, sz_dec)
            save_state(state)
        except Exception:  # rede instável não pode derrubar o bot
            log.exception("Erro no ciclo; tentando de novo no próximo.")
        if once:
            break
        time.sleep(config.POLL_SECONDS)


if __name__ == "__main__":
    main()
