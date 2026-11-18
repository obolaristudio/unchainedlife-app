"""Vectorised daily backtester for long-only spot with realistic costs.

Timing: signal/weight decided at close of day t -> held during day t+1.
Cost: (fee + slippage) charged on every unit of turnover |w_t - w_{t-1}|.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from .regime import REGIME_EXPOSURE

# Conservative base case: Crypto.com retail spot is quoted between 0.075% and
# 0.25% maker / 0.50% taker depending on the source. Base = 0.25% fee + 0.05% slip.
BASE_COST = 0.0030   # per side, fraction of notional
STRESS_COST = 0.0060  # 2x base (taker 0.50% + 0.10% slippage)


@dataclass
class SizingConfig:
    target_vol: float | None = 0.20  # annualised; None = full exposure when long
    vol_window: int = 20
    max_weight: float = 1.0          # no leverage
    rebalance_band: float = 0.10     # skip rebalances smaller than this (cuts cost)
    use_regime: bool = False


def target_weights(df: pd.DataFrame, signal: pd.Series, sizing: SizingConfig,
                   regime: pd.Series | None = None) -> pd.Series:
    w = signal.astype(float).copy()
    if sizing.target_vol is not None:
        vol = np.log(df["close"]).diff().rolling(sizing.vol_window).std() * np.sqrt(365)
        w = w * (sizing.target_vol / vol).clip(upper=sizing.max_weight)
    if sizing.use_regime and regime is not None:
        w = w * regime.map(REGIME_EXPOSURE).fillna(0.0)
    w = w.fillna(0.0).clip(0, sizing.max_weight)
    # Rebalance band: only move when the change is material or we go to/from flat.
    out = np.zeros(len(w))
    cur = 0.0
    for i, x in enumerate(w.values):
        if (x == 0) != (cur == 0) or abs(x - cur) >= sizing.rebalance_band:
            cur = x
        out[i] = cur
    return pd.Series(out, index=w.index)


def run(df: pd.DataFrame, weights: pd.Series, cost: float = BASE_COST) -> pd.DataFrame:
    asset_ret = df["close"].pct_change().fillna(0.0)
    w_held = weights.shift(1).fillna(0.0)          # weight decided yesterday
    turnover = weights.diff().abs().fillna(weights.abs())
    costs = (turnover * cost).shift(1).fillna(0.0)  # paid when the order fills (next bar)
    net = w_held * asset_ret - costs
    return pd.DataFrame({"weight": w_held, "asset_ret": asset_ret, "cost": costs, "ret": net})


def trades(bt: pd.DataFrame) -> pd.Series:
    """Per-trade compounded net return, trade = contiguous run of weight > 0."""
    in_mkt = bt["weight"] > 0
    starts = in_mkt & ~in_mkt.shift(1, fill_value=False)
    if not starts.any():
        return pd.Series(dtype=float)
    # Trade spans its in-market days plus the first flat day (when the exit cost is paid).
    span = in_mkt | in_mkt.shift(1, fill_value=False)
    tid = starts.cumsum().where(span)
    tid = tid[tid > 0]
    return (1 + bt["ret"].loc[tid.index]).groupby(tid).prod() - 1
