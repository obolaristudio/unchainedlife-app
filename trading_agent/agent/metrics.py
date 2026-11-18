"""Performance metrics and multiple-testing correction (Deflated Sharpe Ratio)."""
from __future__ import annotations

from statistics import NormalDist

import numpy as np
import pandas as pd

ANN = 365  # crypto trades every day
_N = NormalDist()


def sharpe(r: pd.Series) -> float:
    sd = r.std()
    return float(r.mean() / sd * np.sqrt(ANN)) if sd > 0 else 0.0


def max_drawdown(r: pd.Series) -> float:
    eq = (1 + r).cumprod()
    return float((eq / eq.cummax() - 1).min()) if len(eq) else 0.0


def cagr(r: pd.Series) -> float:
    if len(r) == 0:
        return 0.0
    return float((1 + r).prod() ** (ANN / len(r)) - 1)


def summarize(r: pd.Series, trade_rets: pd.Series | None = None) -> dict:
    out = {
        "sharpe": round(sharpe(r), 2),
        "cagr_pct": round(cagr(r) * 100, 1),
        "max_dd_pct": round(max_drawdown(r) * 100, 1),
        "ann_vol_pct": round(float(r.std() * np.sqrt(ANN) * 100), 1),
        "days": int(len(r)),
    }
    if trade_rets is not None:
        wins, losses = trade_rets[trade_rets > 0], trade_rets[trade_rets <= 0]
        out["trades"] = int(len(trade_rets))
        out["win_rate_pct"] = round(float(len(wins) / len(trade_rets) * 100), 1) if len(trade_rets) else 0.0
        out["profit_factor"] = (
            round(float(wins.sum() / -losses.sum()), 2) if len(losses) and losses.sum() < 0 else float("inf")
        )
    return out


def deflated_sharpe(r: pd.Series, n_trials: int, sr_trials_var: float) -> float:
    """Probability the true Sharpe > 0 after correcting for `n_trials` tested variants.

    Bailey & Lopez de Prado (2014). Sharpe values here are per-period (daily).
    """
    T = len(r)
    if T < 30 or r.std() == 0:
        return 0.0
    sr = r.mean() / r.std()
    g = 0.5772156649
    sd = np.sqrt(max(sr_trials_var, 1e-12))
    n = max(n_trials, 2)
    sr0 = sd * ((1 - g) * _N.inv_cdf(1 - 1 / n) + g * _N.inv_cdf(1 - 1 / (n * np.e)))
    skew, kurt = float(r.skew()), float(r.kurt()) + 3
    denom = np.sqrt(max(1 - skew * sr + (kurt - 1) / 4 * sr ** 2, 1e-12))
    return float(_N.cdf((sr - sr0) * np.sqrt(T - 1) / denom))
