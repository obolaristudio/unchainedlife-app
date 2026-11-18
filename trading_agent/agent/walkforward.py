"""Anchored-free rolling walk-forward: pick params on train, trade them blind on test."""
from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from . import backtest as bt
from .metrics import sharpe
from .strategies import Strategy

TRAIN_DAYS = 730
TEST_DAYS = 182


@dataclass
class Fold:
    train_start: pd.Timestamp
    train_end: pd.Timestamp
    test_start: pd.Timestamp
    test_end: pd.Timestamp


def make_folds(index: pd.DatetimeIndex, warmup: int = 365,
               train: int = TRAIN_DAYS, test: int = TEST_DAYS) -> list[Fold]:
    folds, i = [], warmup
    while i + train + 1 < len(index):
        te_end = min(i + train + test, len(index)) - 1
        folds.append(Fold(index[i], index[i + train - 1], index[i + train], index[te_end]))
        i += test
    return folds


def all_param_returns(df: pd.DataFrame, strat: Strategy, sizing: bt.SizingConfig,
                      regime: pd.Series, cost: float) -> dict[str, pd.DataFrame]:
    """Backtest every parameter set once on the full history (signals are causal)."""
    out = {}
    for p in strat.params():
        w = bt.target_weights(df, strat.signal(df, **p), sizing, regime)
        out[_key(p)] = bt.run(df, w, cost)
    return out


def _key(p: dict) -> str:
    return ",".join(f"{k}={v}" for k, v in p.items())


def walk_forward(df: pd.DataFrame, strat: Strategy, sizing: bt.SizingConfig,
                 regime: pd.Series, cost: float, folds: list[Fold]) -> dict:
    runs = all_param_returns(df, strat, sizing, regime, cost)
    oos_parts, chosen = [], []
    for f in folds:
        train_scores = {k: sharpe(r.loc[f.train_start:f.train_end, "ret"]) for k, r in runs.items()}
        best = max(train_scores, key=train_scores.get)
        oos_parts.append(runs[best].loc[f.test_start:f.test_end])
        chosen.append({"test_start": str(f.test_start.date()), "test_end": str(f.test_end.date()),
                       "params": best, "train_sharpe": round(train_scores[best], 2)})
    oos = pd.concat(oos_parts)
    oos = oos[~oos.index.duplicated()]
    # Every variant over the same OOS window, used for robustness + DSR.
    start, end = folds[0].test_start, folds[-1].test_end
    variant_sharpes = {k: sharpe(r.loc[start:end, "ret"]) for k, r in runs.items()}
    return {"oos": oos, "chosen": chosen, "variant_sharpes": variant_sharpes, "runs": runs}
