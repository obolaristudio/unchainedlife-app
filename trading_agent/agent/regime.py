"""Explainable regime classifier: CALM_TREND, RANGE, CHOPPY, CRASH.

Every input at row t uses data up to and including the close of day t only.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

CALM_TREND, RANGE, CHOPPY, CRASH = "CALM_TREND", "RANGE", "CHOPPY", "CRASH"
LABELS = [CALM_TREND, RANGE, CHOPPY, CRASH]

# Exposure multiplier per regime (applied on top of any strategy signal).
REGIME_EXPOSURE = {CALM_TREND: 1.0, RANGE: 1.0, CHOPPY: 0.5, CRASH: 0.0}

# Thresholds (fixed up front, NOT optimised, so they cannot overfit).
ER_WINDOW = 20          # efficiency-ratio window (trend strength)
ER_TREND = 0.30         # ER above this = trending
VOL_WINDOW = 20         # realized volatility window
VOL_LOOKBACK = 365      # percentile reference window
VOL_CHOPPY_PCT = 0.75   # vol percentile above this = choppy
CRASH_RET_10D = -0.15   # 10-day return below this = crash
CRASH_DD_30D = -0.25    # drawdown from 30-day high below this = crash
CRASH_RET_3D = -0.10    # fast drop ...
CRASH_VOL_Z = 2.0       # ... with abnormal volume


def efficiency_ratio(close: pd.Series, n: int) -> pd.Series:
    change = (close - close.shift(n)).abs()
    path = close.diff().abs().rolling(n).sum()
    return change / path


def features(df: pd.DataFrame) -> pd.DataFrame:
    c = df["close"]
    logret = np.log(c).diff()
    vol = logret.rolling(VOL_WINDOW).std() * np.sqrt(365)
    vol_pct = vol.rolling(VOL_LOOKBACK, min_periods=180).rank(pct=True)
    lv = np.log(df["volume"].replace(0, np.nan))
    vol_z = (lv - lv.rolling(60).mean()) / lv.rolling(60).std()
    return pd.DataFrame({
        "er": efficiency_ratio(c, ER_WINDOW),
        "vol": vol,
        "vol_pct": vol_pct,
        "ret_3d": c / c.shift(3) - 1,
        "ret_10d": c / c.shift(10) - 1,
        "dd_30d": c / c.rolling(30).max() - 1,
        "volume_z": vol_z,
    })


def classify(df: pd.DataFrame) -> pd.Series:
    f = features(df)
    crash = (
        (f["ret_10d"] < CRASH_RET_10D)
        | (f["dd_30d"] < CRASH_DD_30D)
        | ((f["ret_3d"] < CRASH_RET_3D) & (f["volume_z"] > CRASH_VOL_Z))
    )
    choppy = f["vol_pct"] > VOL_CHOPPY_PCT
    trend = f["er"] > ER_TREND
    label = np.select([crash, choppy, trend], [CRASH, CHOPPY, CALM_TREND], default=RANGE)
    out = pd.Series(label, index=df.index, name="regime")
    out[f[["er", "vol_pct", "dd_30d"]].isna().any(axis=1)] = None
    return out


def forward_truth(df: pd.DataFrame, horizon: int = 20) -> pd.Series:
    """Ex-post label of what actually happened over the NEXT `horizon` days.

    Used only to grade the classifier, never as a trading input.
    """
    c = df["close"]
    logret = np.log(c).diff()
    fwd_min = c[::-1].rolling(horizon).min()[::-1].shift(-1)
    fwd_dd = fwd_min / c - 1
    fwd_vol = logret[::-1].rolling(horizon).std()[::-1].shift(-1) * np.sqrt(365)
    hist_vol = logret.rolling(VOL_WINDOW).std() * np.sqrt(365)
    vol_thr = hist_vol.rolling(VOL_LOOKBACK, min_periods=180).quantile(VOL_CHOPPY_PCT)
    fwd_er = efficiency_ratio(c, horizon).shift(-horizon)
    label = np.select(
        [fwd_dd < -0.20, fwd_vol > vol_thr, fwd_er > ER_TREND],
        [CRASH, CHOPPY, CALM_TREND],
        default=RANGE,
    )
    out = pd.Series(label, index=df.index, name="truth")
    out[fwd_er.isna() | vol_thr.isna()] = None
    return out


def evaluate(df: pd.DataFrame, horizon: int = 20) -> dict:
    pred, truth = classify(df), forward_truth(df, horizon)
    m = pd.concat([pred, truth], axis=1).dropna()
    fwd_ret = (df["close"].shift(-10) / df["close"] - 1).reindex(m.index)
    acc = float((m["regime"] == m["truth"]).mean())
    majority = m["truth"].value_counts(normalize=True)
    confusion = pd.crosstab(m["regime"], m["truth"]).reindex(index=LABELS, columns=LABELS, fill_value=0)
    crash_pred = m["regime"] == CRASH
    crash_true = m["truth"] == CRASH
    by_regime = {
        lab: {
            "days": int((m["regime"] == lab).sum()),
            "share_pct": round(float((m["regime"] == lab).mean() * 100), 1),
            "fwd_10d_mean_pct": round(float(fwd_ret[m["regime"] == lab].mean() * 100), 2),
            "fwd_10d_p05_pct": round(float(fwd_ret[m["regime"] == lab].quantile(0.05) * 100), 2),
        }
        for lab in LABELS
    }
    return {
        "days_evaluated": int(len(m)),
        "accuracy_pct": round(acc * 100, 1),
        "error_rate_pct": round((1 - acc) * 100, 1),
        "baseline_always_majority_pct": round(float(majority.iloc[0]) * 100, 1),
        "majority_label": str(majority.index[0]),
        "crash_precision_pct": round(float((crash_pred & crash_true).sum() / max(crash_pred.sum(), 1)) * 100, 1),
        "crash_recall_pct": round(float((crash_pred & crash_true).sum() / max(crash_true.sum(), 1)) * 100, 1),
        "confusion": confusion,
        "by_regime": by_regime,
    }
