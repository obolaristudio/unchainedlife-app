"""Phase 1 research: data -> regime -> candidates -> walk-forward -> verdicts.

Run:  python research.py            (uses cached data in ./data)
      python research.py --refresh  (re-download)
Writes reports/phase1_results.json and reports/phase1_tables.md. Every number in the
report comes from this script.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from agent import backtest as bt
from agent import data, metrics, regime
from agent.strategies import CANDIDATES
from agent.walkforward import make_folds, walk_forward

ROOT = Path(__file__).resolve().parent
REPORTS = ROOT / "reports"
ASSETS = {"BTC": ("BTCUSDT", "BTC_USD"), "ETH": ("ETHUSDT", "ETH_USD")}
SIZING_TARGET_VOL = 0.20

# Pre-registered verdict rules (fixed before looking at results).
RULES = {
    "beat_buy_hold_sharpe": "OOS net Sharpe > raw buy-and-hold Sharpe",
    "beat_voltarget_hold_sharpe": "OOS net Sharpe > vol-targeted buy-and-hold Sharpe (same sizing)",
    "survives_2x_costs": "At 2x costs, OOS Sharpe still > both benchmarks",
    "deflated_sharpe_ge_0_95": "Deflated Sharpe probability >= 0.95 after counting every variant tested",
    "robust_parameters": "Median OOS Sharpe of ALL variants >= 50% of walk-forward Sharpe and > 0",
    "enough_trades": ">= 20 OOS trades",
    "drawdown_not_worse": "OOS max drawdown no worse than vol-targeted buy-and-hold",
}


def benchmarks(df, start, end, cost):
    hold = pd.Series(1.0, index=df.index)
    raw = bt.run(df, hold, cost).loc[start:end, "ret"]
    vt = bt.run(df, bt.target_weights(df, hold, bt.SizingConfig(SIZING_TARGET_VOL)), cost).loc[start:end, "ret"]
    return raw, vt


def funding_snapshot():
    out = {}
    for inst in ["BTCUSD-PERP", "ETHUSD-PERP"]:
        try:
            res = data._get_json(f"https://api.crypto.com/exchange/v1/public/get-valuations"
                                 f"?instrument_name={inst}&valuation_type=funding_hist&count=21")
            vals = [float(x["v"]) for x in res["result"]["data"]]
            out[inst] = {"last_funding_rate_pct": round(vals[0] * 100, 4),
                         "avg_last_21_pct": round(float(np.mean(vals)) * 100, 4)}
        except Exception as e:  # informational only
            out[inst] = {"error": str(e)[:120]}
    return out


def main(refresh: bool) -> None:
    REPORTS.mkdir(exist_ok=True)
    results = {"generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
               "cost_base_per_side": bt.BASE_COST, "cost_stress_per_side": bt.STRESS_COST,
               "sizing_target_vol": SIZING_TARGET_VOL, "rules": RULES, "assets": {}}

    frames, venue_check = {}, {}
    for a, (bsym, csym) in ASSETS.items():
        frames[a] = data.load(f"binance_{bsym}_1d", data.fetch_binance_daily, bsym, refresh=refresh)
        cdc = data.load(f"cdc_{csym}_1d", data.fetch_cdc_daily, csym, refresh=refresh)
        venue_check[a] = data.crosscheck_venues(frames[a], cdc)
    results["venue_crosscheck"] = venue_check
    results["funding"] = funding_snapshot()

    # Regime classifier: accuracy vs what actually happened next.
    reg_eval = {}
    for a, df in frames.items():
        ev = regime.evaluate(df)
        reg_eval[a] = {k: v for k, v in ev.items() if k != "confusion"}
        reg_eval[a]["confusion"] = ev["confusion"].to_dict()
        f = regime.features(df).iloc[-1]
        reg_eval[a]["current"] = {"date": str(df.index[-1].date()), "close": float(df["close"].iloc[-1]),
                                  "regime": regime.classify(df).iloc[-1],
                                  **{k: round(float(v), 3) for k, v in f.items()}}
    results["regime"] = reg_eval

    # Walk-forward every candidate x {regime filter off/on} x asset.
    rows, variant_sharpes_all, wf_store = [], [], {}
    n_trials = 0
    for a, df in frames.items():
        reg = regime.classify(df)
        folds = make_folds(df.index)
        start, end = folds[0].test_start, folds[-1].test_end
        bh_raw, bh_vt = benchmarks(df, start, end, bt.BASE_COST)
        bh_raw_s, bh_vt_s = benchmarks(df, start, end, bt.STRESS_COST)
        results["assets"][a] = {
            "data_start": str(df.index[0].date()), "data_end": str(df.index[-1].date()),
            "oos_start": str(start.date()), "oos_end": str(end.date()), "folds": len(folds),
            "buy_hold": metrics.summarize(bh_raw), "voltarget_hold": metrics.summarize(bh_vt),
        }
        for strat in CANDIDATES:
            for use_reg in (False, True):
                sizing = bt.SizingConfig(SIZING_TARGET_VOL, use_regime=use_reg)
                wf = walk_forward(df, strat, sizing, reg, bt.BASE_COST, folds)
                wf_s = walk_forward(df, strat, sizing, reg, bt.STRESS_COST, folds)
                n_trials += len(wf["variant_sharpes"])
                variant_sharpes_all.extend(wf["variant_sharpes"].values())
                name = f"{strat.name}{'+REGIME' if use_reg else ''}"
                oos = wf["oos"]
                summ = metrics.summarize(oos["ret"], bt.trades(oos))
                stress = metrics.summarize(wf_s["oos"]["ret"])
                vs = np.array(list(wf["variant_sharpes"].values()))
                per_fold = []
                for ch in wf["chosen"]:
                    seg = oos.loc[ch["test_start"]:ch["test_end"]]
                    per_fold.append({**ch, **metrics.summarize(seg["ret"], bt.trades(seg)),
                                     "buy_hold_sharpe": round(metrics.sharpe(bh_raw.loc[ch["test_start"]:ch["test_end"]]), 2)})
                wf_store[(a, name)] = oos["ret"]
                rows.append({
                    "asset": a, "strategy": name, "base": strat.name, **summ,
                    "sharpe_2x_cost": stress["sharpe"],
                    "cost_drag_pct_per_year": round(float(oos["cost"].mean() * 365 * 100), 2),
                    "variants": len(vs), "variant_sharpe_median": round(float(np.median(vs)), 2),
                    "variant_share_beating_bh": round(float((vs > metrics.sharpe(bh_raw)).mean() * 100), 0),
                    "distinct_params_chosen": len({c["params"] for c in wf["chosen"]}),
                    "per_fold": per_fold,
                    "_bh": (metrics.sharpe(bh_raw), metrics.sharpe(bh_vt), metrics.sharpe(bh_raw_s),
                            metrics.sharpe(bh_vt_s), metrics.max_drawdown(bh_vt)),
                })

    # Deflated Sharpe uses ALL variants across all strategies/assets.
    var_daily = float(np.var(np.array(variant_sharpes_all) / np.sqrt(365)))
    results["total_variants_tested"] = n_trials
    for r in rows:
        bh, vt, bh_s, vt_s, vt_dd = r.pop("_bh")
        r["dsr"] = round(metrics.deflated_sharpe(wf_store[(r["asset"], r["strategy"])], n_trials, var_daily), 3)
        checks = {
            "beat_buy_hold_sharpe": r["sharpe"] > bh,
            "beat_voltarget_hold_sharpe": r["sharpe"] > vt,
            "survives_2x_costs": r["sharpe_2x_cost"] > max(bh_s, vt_s),
            "deflated_sharpe_ge_0_95": r["dsr"] >= 0.95,
            "robust_parameters": r["variant_sharpe_median"] >= 0.5 * r["sharpe"] and r["variant_sharpe_median"] > 0,
            "enough_trades": r["trades"] >= 20,
            "drawdown_not_worse": r["max_dd_pct"] / 100 >= vt_dd,
        }
        r["checks"] = checks
        r["passed"] = sum(checks.values())
        r["verdict"] = "DEPLOY (paper)" if all(checks.values()) else (
            "WATCHLIST" if checks["beat_buy_hold_sharpe"] and checks["beat_voltarget_hold_sharpe"]
            and checks["survives_2x_costs"] and checks["robust_parameters"] else "REJECT")
    results["candidates"] = rows

    (REPORTS / "phase1_results.json").write_text(json.dumps(results, indent=2, default=str))
    write_tables(results)
    print(f"variants tested: {n_trials}")
    for r in sorted(rows, key=lambda x: -x["sharpe"]):
        print(f"{r['asset']} {r['strategy']:<22} SR {r['sharpe']:>5} SR2x {r['sharpe_2x_cost']:>5} "
              f"DD {r['max_dd_pct']:>6} trades {r['trades']:>3} DSR {r['dsr']:.2f} "
              f"pass {r['passed']}/7 {r['verdict']}")
    for a, v in results["assets"].items():
        print(a, "B&H", v["buy_hold"], "VT-B&H", v["voltarget_hold"])


def write_tables(res: dict) -> None:
    L = [f"_Gerado em {res['generated_utc']} por `python research.py`. Variantes testadas: "
         f"{res['total_variants_tested']}._", ""]
    L += ["| Ativo | Estratégia | Sharpe | Sharpe 2x custo | CAGR % | Max DD % | Trades | Win % | PF | DSR | Testes ok | Veredito |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for a, v in res["assets"].items():
        for lab, k in (("Buy & hold", "buy_hold"), ("Buy & hold vol-target 20%", "voltarget_hold")):
            b = v[k]
            L.append(f"| {a} | *{lab}* | {b['sharpe']} | – | {b['cagr_pct']} | {b['max_dd_pct']} | – | – | – | – | – | benchmark |")
    for r in sorted(res["candidates"], key=lambda x: (x["asset"], -x["sharpe"])):
        L.append(f"| {r['asset']} | {r['strategy']} | {r['sharpe']} | {r['sharpe_2x_cost']} | {r['cagr_pct']} | "
                 f"{r['max_dd_pct']} | {r['trades']} | {r['win_rate_pct']} | {r['profit_factor']} | {r['dsr']} | "
                 f"{r['passed']}/7 | {r['verdict']} |")
    (REPORTS / "phase1_tables.md").write_text("\n".join(L) + "\n")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--refresh", action="store_true")
    main(ap.parse_args().refresh)
    sys.exit(0)
