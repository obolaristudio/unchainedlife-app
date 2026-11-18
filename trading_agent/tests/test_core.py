import numpy as np
import pandas as pd
import pytest

from agent import backtest as bt
from agent import data, metrics, regime, walkforward
from agent.strategies import CANDIDATES


def synthetic(n=1200, seed=0):
    rng = np.random.default_rng(seed)
    close = 100 * np.exp(np.cumsum(rng.normal(0.0005, 0.03, n)))
    idx = pd.date_range("2018-01-01", periods=n, freq="D", tz="UTC")
    return pd.DataFrame({"open": close, "high": close * 1.01, "low": close * 0.99,
                         "close": close, "volume": rng.uniform(1e3, 2e3, n)}, index=idx)


@pytest.mark.parametrize("strat", CANDIDATES, ids=lambda s: s.name)
def test_signals_have_no_lookahead(strat):
    """Changing future prices must not change any past signal."""
    df = synthetic()
    p = strat.params()[0]
    base = strat.signal(df, **p)
    cut = 900
    shocked = df.copy()
    shocked.iloc[cut:, :4] *= 3.0
    after = strat.signal(shocked, **p)
    pd.testing.assert_series_equal(base.iloc[:cut], after.iloc[:cut])


def test_regime_has_no_lookahead():
    df = synthetic()
    shocked = df.copy()
    shocked.iloc[900:, :4] *= 0.3
    pd.testing.assert_series_equal(regime.classify(df).iloc[:900], regime.classify(shocked).iloc[:900])


def test_backtest_applies_signal_next_day_and_charges_costs():
    idx = pd.date_range("2020-01-01", periods=4, freq="D", tz="UTC")
    df = pd.DataFrame({"close": [100.0, 110.0, 121.0, 121.0]}, index=idx)
    w = pd.Series([1.0, 1.0, 0.0, 0.0], index=idx)  # buy at close day0, sell at close day2
    res = bt.run(df, w, cost=0.01)
    # day0: no position yet, entry cost lands on day1 together with the +10% move
    assert res["ret"].iloc[0] == pytest.approx(0.0)
    assert res["ret"].iloc[1] == pytest.approx(0.10 - 0.01)
    assert res["ret"].iloc[2] == pytest.approx(0.10)
    assert res["ret"].iloc[3] == pytest.approx(-0.01)  # exit cost, flat day
    tr = bt.trades(res)
    assert len(tr) == 1
    assert tr.iloc[0] == pytest.approx((1.09) * 1.10 * 0.99 - 1)


def test_weights_never_exceed_one_or_go_negative():
    df = synthetic()
    sig = pd.Series(1.0, index=df.index)
    w = bt.target_weights(df, sig, bt.SizingConfig(target_vol=5.0))
    assert w.max() <= 1.0 and w.min() >= 0.0


def test_crash_regime_forces_flat():
    df = synthetic()
    reg = pd.Series(regime.CRASH, index=df.index)
    w = bt.target_weights(df, pd.Series(1.0, index=df.index), bt.SizingConfig(use_regime=True), reg)
    assert (w == 0).all()


def test_folds_are_ordered_and_test_windows_do_not_overlap():
    idx = pd.date_range("2017-01-01", periods=3000, freq="D", tz="UTC")
    folds = walkforward.make_folds(idx)
    assert len(folds) > 5
    for f in folds:
        assert f.train_start < f.train_end < f.test_start <= f.test_end
    for a, b in zip(folds, folds[1:]):
        assert a.test_end < b.test_start


def test_metrics_known_values():
    r = pd.Series([0.1, -0.5, 0.2])
    assert metrics.max_drawdown(r) == pytest.approx(-0.5)
    assert metrics.sharpe(pd.Series([0.0] * 10)) == 0.0


def test_deflated_sharpe_penalises_more_trials():
    r = pd.Series(np.random.default_rng(1).normal(0.001, 0.02, 1500))
    assert metrics.deflated_sharpe(r, 2, 1e-4) > metrics.deflated_sharpe(r, 500, 1e-4)


def test_validate_rejects_bad_data():
    df = synthetic(50)
    bad = df.copy()
    bad.iloc[10, 3] = -1
    with pytest.raises(ValueError):
        data.validate(bad)
    with pytest.raises(ValueError):
        data.validate(df.drop(df.index[20:30]))
