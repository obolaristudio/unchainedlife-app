"""Backtest da estratégia com dados reais da Hyperliquid.

Uso:
    python backtest.py                 # BTC 1h, capital US$30
    python backtest.py --capital 50 --interval 4h

Premissas (conservadoras):
- Entrada no fechamento do candle do sinal.
- Taxa taker de 0,045% na entrada e na saída.
- Se stop e alvo cabem no mesmo candle, conta o STOP (pior caso).
- Sinal contrário fecha a posição e abre a oposta.
- Funding não é simulado (custo extra real, normalmente pequeno).
"""
import argparse
from datetime import datetime, timezone

from hyperliquid.info import Info

import config
from market import base_url, fetch_candles
from strategy import check_signal, position_size

FEE = 0.00045


def run(capital: float, interval: str, coin: str) -> None:
    info = Info(base_url(False), skip_ws=True)
    candles = fetch_candles(info, coin, interval, 5000)
    warmup = config.EMA_SLOW * 3
    equity = peak = capital
    max_dd = 0.0
    pos = None  # dict(side, entry, stop, take, size)
    trades, skipped = [], 0
    day, day_start = None, equity

    def close(price: float, reason: str) -> None:
        nonlocal equity, pos
        sign = 1 if pos["side"] == "long" else -1
        pnl = (price - pos["entry"]) * pos["size"] * sign
        fees = (pos["entry"] + price) * pos["size"] * FEE
        equity += pnl - fees
        trades.append(pnl - fees)
        pos = None

    for i in range(warmup, len(candles)):
        c = candles[i]
        d = datetime.fromtimestamp(c.t / 1000, timezone.utc).date()
        if d != day:
            day, day_start = d, equity

        # 1) stop / alvo dentro do candle
        if pos:
            if pos["side"] == "long":
                if c.l <= pos["stop"]:
                    close(pos["stop"], "stop")
                elif c.h >= pos["take"]:
                    close(pos["take"], "take")
            else:
                if c.h >= pos["stop"]:
                    close(pos["stop"], "stop")
                elif c.l <= pos["take"]:
                    close(pos["take"], "take")

        # 2) sinal no fechamento
        sig = check_signal(candles[: i + 1], config.EMA_FAST, config.EMA_SLOW,
                           config.ATR_PERIOD, config.SL_ATR_MULT, config.RR)
        if sig:
            if pos and pos["side"] != sig.side:
                close(c.c, "reverse")
            blocked = equity < day_start * (1 - config.DAILY_LOSS_LIMIT)
            if not pos and not blocked:
                size = position_size(equity, sig.entry, sig.stop,
                                     config.RISK_PER_TRADE, config.MAX_LEVERAGE)
                if size * sig.entry < config.MIN_NOTIONAL_USD:
                    skipped += 1
                else:
                    pos = dict(side=sig.side, entry=sig.entry, stop=sig.stop,
                               take=sig.take, size=size)

        peak = max(peak, equity)
        max_dd = max(max_dd, (peak - equity) / peak)

    if pos:
        close(candles[-1].c, "end")

    wins = [t for t in trades if t > 0]
    losses = [t for t in trades if t <= 0]
    pf = sum(wins) / abs(sum(losses)) if losses and sum(losses) != 0 else float("inf")
    start = datetime.fromtimestamp(candles[warmup].t / 1000, timezone.utc).date()
    end = datetime.fromtimestamp(candles[-1].t / 1000, timezone.utc).date()

    print(f"\n=== Backtest {coin} {interval} | {start} -> {end} ===")
    print(f"Capital inicial:   ${capital:,.2f}")
    print(f"Capital final:     ${equity:,.2f}  ({(equity / capital - 1) * 100:+.1f}%)")
    print(f"Operações:         {len(trades)}  (puladas por valor mínimo: {skipped})")
    if trades:
        print(f"Taxa de acerto:    {len(wins) / len(trades) * 100:.1f}%")
        print(f"Profit factor:     {pf:.2f}   (>1,3 = bom; <1 = perde dinheiro)")
        print(f"Maior ganho/perda: ${max(trades):+.2f} / ${min(trades):+.2f}")
    print(f"Drawdown máximo:   {max_dd * 100:.1f}%")
    hold_pnl = (candles[-1].c / candles[warmup].c - 1) * 100
    print(f"Comparação: só comprar e segurar {coin} no período = {hold_pnl:+.1f}%\n")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--capital", type=float, default=30.0)
    p.add_argument("--interval", default=config.INTERVAL)
    p.add_argument("--coin", default=config.COIN)
    a = p.parse_args()
    run(a.capital, a.interval, a.coin)
