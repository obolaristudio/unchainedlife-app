# Sensibilidade a taxa (BTC, walk-forward 2020-2026)

Custo por lado = taxa + 0,05% slippage. Estresse = 2x. Gerado por `python fee_sensitivity.py`.

| Taxa/lado | Estratégia | Sharpe | Sharpe 2x | B&H | Max DD % | Custo/ano % | DSR | Critérios | Falhou em | Veredito |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.075% | SMA_TREND | 0.95 | 0.85 | 0.76 | -30.3 | 1.35 | 0.65 | 6/7 | deflated_sharpe_ge_0_95 | WATCHLIST |
| 0.075% | TSMOM | 0.82 | 0.82 | 0.76 | -28.8 | 1.31 | 0.527 | 6/7 | deflated_sharpe_ge_0_95 | WATCHLIST |
| 0.100% | SMA_TREND | 0.92 | 0.8 | 0.76 | -30.5 | 1.69 | 0.602 | 6/7 | deflated_sharpe_ge_0_95 | WATCHLIST |
| 0.100% | TSMOM | 0.81 | 0.81 | 0.76 | -29.1 | 1.57 | 0.493 | 6/7 | deflated_sharpe_ge_0_95 | WATCHLIST |
| 0.150% | SMA_TREND | 0.88 | 0.74 | 0.76 | -30.8 | 2.26 | 0.533 | 5/7 | survives_2x_costs, deflated_sharpe_ge_0_95 | REJECT |
| 0.150% | TSMOM | 0.76 | 0.75 | 0.76 | -29.5 | 2.07 | 0.409 | 4/7 | beat_buy_hold_sharpe, survives_2x_costs, deflated_sharpe_ge_0_95 | REJECT |
| 0.250% | SMA_TREND | 0.8 | 0.62 | 0.76 | -31.5 | 3.39 | 0.362 | 5/7 | survives_2x_costs, deflated_sharpe_ge_0_95 | REJECT |
| 0.250% | TSMOM | 0.81 | 0.66 | 0.76 | -29.1 | 2.16 | 0.369 | 5/7 | survives_2x_costs, deflated_sharpe_ge_0_95 | REJECT |
| 0.500% | SMA_TREND | 0.65 | 0.44 | 0.76 | -33.1 | 6.21 | 0.083 | 4/7 | beat_buy_hold_sharpe, survives_2x_costs, deflated_sharpe_ge_0_95 | REJECT |
| 0.500% | TSMOM | 0.69 | 0.76 | 0.76 | -30.2 | 3.54 | 0.101 | 4/7 | beat_buy_hold_sharpe, survives_2x_costs, deflated_sharpe_ge_0_95 | REJECT |
