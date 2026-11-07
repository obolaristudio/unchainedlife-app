"""Leitura de dados públicos da Hyperliquid (não precisa de chave)."""
import time
from typing import List

from hyperliquid.info import Info
from hyperliquid.utils import constants

from strategy import Candle

INTERVAL_MS = {"15m": 900_000, "1h": 3_600_000, "4h": 14_400_000, "1d": 86_400_000}


def base_url(testnet: bool) -> str:
    return constants.TESTNET_API_URL if testnet else constants.MAINNET_API_URL


def fetch_candles(info: Info, coin: str, interval: str, n: int) -> List[Candle]:
    """Últimos n candles FECHADOS (o candle em formação é descartado)."""
    step = INTERVAL_MS[interval]
    now = int(time.time() * 1000)
    raw = info.candles_snapshot(coin, interval, now - step * (n + 2), now)
    candles = [Candle(int(r["t"]), float(r["o"]), float(r["h"]), float(r["l"]), float(r["c"]))
               for r in raw]
    return [c for c in candles if c.t + step <= now][-n:]


def round_px(px: float, sz_decimals: int) -> float:
    """Regra da Hyperliquid para perps: até 5 algarismos significativos
    e no máximo (6 - szDecimals) casas decimais."""
    return round(float(f"{px:.5g}"), 6 - sz_decimals)


def round_sz(sz: float, sz_decimals: int) -> float:
    factor = 10 ** sz_decimals
    return int(sz * factor) / factor   # sempre arredonda para baixo
