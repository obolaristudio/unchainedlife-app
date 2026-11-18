"""Option B: rerun the full Phase 1 validation at each plausible Crypto.com fee level.

Cost per side = fee + 0.05% slippage; stress = 2x. Writes reports/fee_sensitivity.md.
"""
from agent import backtest as bt
import research

FEES = [0.00075, 0.0010, 0.0015, 0.0025, 0.0050]  # per side: maker tiers .. retail taker
SLIP = 0.0005

rows = []
for fee in FEES:
    bt.BASE_COST, bt.STRESS_COST = fee + SLIP, 2 * (fee + SLIP)
    res = research.main(False, tag=f"_fee{fee*100:.3f}".replace(".", "p"), quiet=True)
    for c in res["candidates"]:
        if c["strategy"] in ("TSMOM", "SMA_TREND"):
            rows.append((fee, c))

L = ["# Sensibilidade a taxa (BTC, walk-forward 2020-2026)", "",
     "Custo por lado = taxa + 0,05% slippage. Estresse = 2x. Gerado por `python fee_sensitivity.py`.", "",
     "| Taxa/lado | Estratégia | Sharpe | Sharpe 2x | B&H | Max DD % | Custo/ano % | DSR | Critérios | Falhou em | Veredito |",
     "|---|---|---|---|---|---|---|---|---|---|---|"]
for fee, c in rows:
    failed = ", ".join(k for k, v in c["checks"].items() if not v) or "-"
    L.append(f"| {fee*100:.3f}% | {c['strategy']} | {c['sharpe']} | {c['sharpe_2x_cost']} | 0.76 | {c['max_dd_pct']} | "
             f"{c['cost_drag_pct_per_year']} | {c['dsr']} | {c['passed']}/7 | {failed} | {c['verdict']} |")
open(research.REPORTS / "fee_sensitivity.md", "w").write("\n".join(L) + "\n")
print("\n".join(L))
