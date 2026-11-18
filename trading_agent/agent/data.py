"""Market data: download, cache and validate daily OHLCV candles.

Research history comes from Binance public market data (deep history since 2017).
Execution venue is Crypto.com Exchange, whose public API only serves recent candles;
`crosscheck_venues` measures how closely the two venues agree on the overlap.
"""
from __future__ import annotations

import json
import time
import urllib.request
from pathlib import Path

import numpy as np
import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
BINANCE_URL = "https://data-api.binance.vision/api/v3/klines"
CDC_URL = "https://api.crypto.com/exchange/v1/public/get-candlestick"
DAY_MS = 86_400_000


def _get_json(url: str, retries: int = 4) -> object:
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=30) as resp:
                return json.loads(resp.read())
        except Exception:  # network errors: back off and retry
            if attempt == retries - 1:
                raise
            time.sleep(2 ** attempt)
    raise RuntimeError("unreachable")


def fetch_binance_daily(symbol: str, start_ms: int = 1_500_000_000_000) -> pd.DataFrame:
    rows: list[list] = []
    cursor = start_ms
    while True:
        batch = _get_json(f"{BINANCE_URL}?symbol={symbol}&interval=1d&limit=1000&startTime={cursor}")
        if not batch:
            break
        rows.extend(batch)
        cursor = batch[-1][0] + DAY_MS
        if len(batch) < 1000:
            break
    df = pd.DataFrame(rows).iloc[:, :7]
    df.columns = ["open_time", "open", "high", "low", "close", "volume", "close_time"]
    now_ms = int(time.time() * 1000)
    df = df[df["close_time"] < now_ms]  # drop the candle that is still forming
    return _finalize(df)


def fetch_cdc_daily(instrument: str) -> pd.DataFrame:
    """Page backwards through Crypto.com daily candles until the API runs dry."""
    rows: dict[int, dict] = {}
    end_ts = int(time.time() * 1000)
    while True:
        res = _get_json(f"{CDC_URL}?instrument_name={instrument}&timeframe=1D&count=300&end_ts={end_ts}")
        data = res["result"]["data"]
        new = [d for d in data if d["t"] not in rows]
        if not new:
            break
        for d in new:
            rows[d["t"]] = d
        end_ts = min(d["t"] for d in data) - 1
    df = pd.DataFrame(rows.values()).rename(
        columns={"t": "open_time", "o": "open", "h": "high", "l": "low", "c": "close", "v": "volume"}
    )
    df = df[df["open_time"] + DAY_MS <= int(time.time() * 1000)]
    return _finalize(df[["open_time", "open", "high", "low", "close", "volume"]])


def _finalize(df: pd.DataFrame) -> pd.DataFrame:
    out = df[["open_time", "open", "high", "low", "close", "volume"]].copy()
    for c in ["open", "high", "low", "close", "volume"]:
        out[c] = out[c].astype(float)
    out.index = pd.to_datetime(out["open_time"], unit="ms", utc=True)
    out.index.name = "date"
    out = out.drop(columns="open_time").sort_index()
    out = out[~out.index.duplicated()]
    validate(out)
    return out


def validate(df: pd.DataFrame) -> None:
    """Fail closed on bad data instead of silently trading on it."""
    if df.empty:
        raise ValueError("empty dataset")
    if not df.index.is_monotonic_increasing:
        raise ValueError("timestamps not sorted")
    if (df[["open", "high", "low", "close"]] <= 0).any().any():
        raise ValueError("non-positive prices")
    if (df["high"] < df[["open", "close", "low"]].max(axis=1) - 1e-9).any():
        raise ValueError("high below open/close/low")
    gaps = df.index.to_series().diff().dt.days.dropna()
    if (gaps > 3).any():
        raise ValueError(f"gap in data larger than 3 days: {gaps[gaps > 3].index[:3].tolist()}")


def load(name: str, fetcher, *args, refresh: bool = False) -> pd.DataFrame:
    DATA_DIR.mkdir(exist_ok=True)
    path = DATA_DIR / f"{name}.csv"
    if path.exists() and not refresh:
        df = pd.read_csv(path, index_col="date", parse_dates=["date"])
        validate(df)
        return df
    df = fetcher(*args)
    df.to_csv(path)
    return df


def crosscheck_venues(research: pd.DataFrame, venue: pd.DataFrame) -> dict:
    j = research[["close"]].join(venue[["close"]], rsuffix="_venue", how="inner")
    r1, r2 = np.log(j["close"]).diff().dropna(), np.log(j["close_venue"]).diff().dropna()
    gap = (j["close_venue"] / j["close"] - 1).abs()
    return {
        "overlap_days": int(len(j)),
        "first_overlap": str(j.index[0].date()) if len(j) else None,
        "daily_return_correlation": float(r1.corr(r2)) if len(r1) > 2 else None,
        "median_abs_price_gap_pct": float(gap.median() * 100) if len(j) else None,
        "p99_abs_price_gap_pct": float(gap.quantile(0.99) * 100) if len(j) else None,
    }
