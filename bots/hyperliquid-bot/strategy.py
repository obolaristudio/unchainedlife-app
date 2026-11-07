"""Estratégia de tendência EMA 20/50 + gestão de risco conservadora.

Funções puras (sem rede): usadas pelo bot ao vivo e pelo backtest,
para que o que foi testado seja exatamente o que roda.
"""
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Candle:
    t: int      # abertura (ms)
    o: float
    h: float
    l: float
    c: float


@dataclass
class Signal:
    side: str          # "long" | "short"
    entry: float       # preço de referência (fechamento do candle)
    stop: float
    take: float


def ema(values: List[float], period: int) -> List[float]:
    k = 2 / (period + 1)
    out: List[float] = []
    for i, v in enumerate(values):
        out.append(v if i == 0 else v * k + out[-1] * (1 - k))
    return out


def atr(candles: List[Candle], period: int = 14) -> List[float]:
    trs: List[float] = []
    for i, c in enumerate(candles):
        if i == 0:
            trs.append(c.h - c.l)
        else:
            pc = candles[i - 1].c
            trs.append(max(c.h - c.l, abs(c.h - pc), abs(c.l - pc)))
    # média de Wilder
    out: List[float] = []
    for i, tr in enumerate(trs):
        out.append(tr if i == 0 else (out[-1] * (period - 1) + tr) / period)
    return out


def check_signal(candles: List[Candle], fast: int, slow: int,
                 atr_period: int, sl_atr_mult: float, rr: float) -> Optional[Signal]:
    """Sinal no ÚLTIMO candle fechado: cruzamento da EMA rápida sobre a lenta."""
    if len(candles) < slow * 3:
        return None
    closes = [c.c for c in candles]
    ef, es = ema(closes, fast), ema(closes, slow)
    a = atr(candles, atr_period)[-1]
    price = closes[-1]
    crossed_up = ef[-2] <= es[-2] and ef[-1] > es[-1]
    crossed_down = ef[-2] >= es[-2] and ef[-1] < es[-1]
    dist = a * sl_atr_mult
    if crossed_up:
        return Signal("long", price, price - dist, price + dist * rr)
    if crossed_down:
        return Signal("short", price, price + dist, price - dist * rr)
    return None


def position_size(equity: float, entry: float, stop: float,
                  risk_pct: float, max_leverage: float) -> float:
    """Tamanho em moeda (BTC) para arriscar risk_pct do capital até o stop,
    limitado pela alavancagem máxima."""
    dist = abs(entry - stop)
    if dist <= 0 or equity <= 0:
        return 0.0
    size_by_risk = (equity * risk_pct) / dist
    size_by_lev = (equity * max_leverage) / entry
    return min(size_by_risk, size_by_lev)
