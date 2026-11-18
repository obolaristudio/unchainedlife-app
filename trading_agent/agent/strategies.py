"""Candidate strategies. Signals only (0 = flat, 1 = long); no sizing, no execution.

Spot, long-only, no leverage: the account is small and low-risk, so shorting is out.
Each signal at row t uses closes up to t; the backtester applies it to day t+1.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from itertools import product
from typing import Callable

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class Strategy:
    name: str
    edge: str
    counterparty: str
    why_persists: str
    rules: str
    holding: str
    fn: Callable[..., pd.Series]
    grid: dict = field(default_factory=dict)

    def params(self) -> list[dict]:
        keys = list(self.grid)
        combos = [dict(zip(keys, v)) for v in product(*self.grid.values())]
        return [p for p in combos if _valid(p)]

    def signal(self, df: pd.DataFrame, **p) -> pd.Series:
        return self.fn(df, **p).fillna(0.0).clip(0, 1)


def _valid(p: dict) -> bool:
    if "fast" in p and p["fast"] >= p["slow"]:
        return False
    if "exit" in p and p["exit"] >= p["entry"]:
        return False
    return True


def sma_trend(df, n):
    c = df["close"]
    return (c > c.rolling(n).mean()).astype(float).where(c.rolling(n).mean().notna())


def sma_cross(df, fast, slow):
    c = df["close"]
    f, s = c.rolling(fast).mean(), c.rolling(slow).mean()
    return (f > s).astype(float).where(s.notna())


def donchian(df, entry, exit):
    c = df["close"]
    hi = df["high"].rolling(entry).max().shift(1)
    lo = df["low"].rolling(exit).min().shift(1)
    pos = np.full(len(df), np.nan)
    state = 0.0
    for i, (ci, h, l) in enumerate(zip(c.values, hi.values, lo.values)):
        if np.isnan(h) or np.isnan(l):
            continue
        if state == 0 and ci > h:
            state = 1.0
        elif state == 1 and ci < l:
            state = 0.0
        pos[i] = state
    return pd.Series(pos, index=df.index)


def tsmom(df, lookback):
    c = df["close"]
    return (c / c.shift(lookback) - 1 > 0).astype(float).where(c.shift(lookback).notna())


def rsi(close: pd.Series, n: int) -> pd.Series:
    d = close.diff()
    up = d.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    dn = (-d.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    return 100 - 100 / (1 + up / dn.replace(0, np.nan))


def rsi_reversion(df, k, lo, max_hold):
    c = df["close"]
    r = rsi(c, k)
    trend_ok = c > c.rolling(200).mean()
    exit_ma = c.rolling(5).mean()
    pos = np.full(len(df), np.nan)
    state, held = 0.0, 0
    for i in range(len(df)):
        if np.isnan(r.iloc[i]) or np.isnan(exit_ma.iloc[i]) or i < 200:
            continue
        if state == 0 and r.iloc[i] < lo and trend_ok.iloc[i]:
            state, held = 1.0, 0
        elif state == 1:
            held += 1
            if c.iloc[i] > exit_ma.iloc[i] or held >= max_hold:
                state = 0.0
        pos[i] = state
    return pd.Series(pos, index=df.index)


CANDIDATES = [
    Strategy(
        "SMA_TREND",
        "Crypto prices trend: price above its moving average tends to keep rising more often than chance.",
        "Late sellers and mean-reversion traders fading the move; holders who take profit too early.",
        "Slow information diffusion, retail herding and reflexive leverage cycles in crypto.",
        "Long when close > SMA(n); flat otherwise. Decided at daily close (00:00 UTC), filled next bar.",
        "weeks to months",
        sma_trend,
        {"n": [20, 30, 50, 75, 100, 150, 200]},
    ),
    Strategy(
        "SMA_CROSS",
        "Same trend premium, filtered by two averages to cut whipsaws.",
        "Same as SMA_TREND.",
        "Same as SMA_TREND.",
        "Long when SMA(fast) > SMA(slow); flat otherwise.",
        "months",
        sma_cross,
        {"fast": [10, 20, 30, 50], "slow": [50, 100, 150, 200]},
    ),
    Strategy(
        "DONCHIAN",
        "Breakouts to new N-day highs tend to continue (classic turtle trend following).",
        "Range traders selling the highs; short sellers forced to cover.",
        "Stop-loss and liquidation cascades make breakouts self-reinforcing.",
        "Enter long on close above prior N-day high; exit on close below prior M-day low.",
        "weeks to months",
        donchian,
        {"entry": [20, 40, 55, 80], "exit": [10, 20, 30]},
    ),
    Strategy(
        "TSMOM",
        "Time-series momentum: positive trailing return predicts positive next-period return.",
        "Investors anchored to past prices; contrarian buyers/sellers.",
        "Documented across asset classes (Moskowitz, Ooi, Pedersen 2012); behavioral underreaction.",
        "Long when return over last L days > 0; flat otherwise.",
        "weeks to months",
        tsmom,
        {"lookback": [30, 60, 90, 120, 180, 365]},
    ),
    Strategy(
        "RSI_REVERSION",
        "Short-term oversold dips inside a long-term uptrend snap back.",
        "Panicked sellers and forced liquidations paying for immediacy.",
        "Liquidity provision premium: someone must absorb forced selling.",
        "Long when RSI(k) < lo and close > SMA200; exit when close > SMA5 or after max_hold days.",
        "1 to 10 days",
        rsi_reversion,
        {"k": [2, 3, 4], "lo": [10, 20, 30], "max_hold": [5, 10]},
    ),
]
