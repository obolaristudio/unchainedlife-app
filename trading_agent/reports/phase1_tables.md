_Gerado em 2026-11-18T11:36:48+00:00 por `python research.py`. Variantes testadas: 112._

| Ativo | Estratégia | Sharpe | Sharpe 2x custo | CAGR % | Max DD % | Trades | Win % | PF | DSR | Testes ok | Veredito |
|---|---|---|---|---|---|---|---|---|---|---|---|
| BTC | *Buy & hold* | 0.76 | – | 31.2 | -76.6 | – | – | – | – | – | benchmark |
| BTC | *Buy & hold vol-target 20%* | 0.68 | – | 14.1 | -39.8 | – | – | – | – | – | benchmark |
| BTC | TSMOM | 0.81 | 0.66 | 12.8 | -29.1 | 43 | 34.9 | 3.02 | 0.369 | 5/7 | REJECT |
| BTC | SMA_TREND | 0.8 | 0.62 | 13.9 | -31.5 | 62 | 22.6 | 2.28 | 0.362 | 5/7 | REJECT |
| BTC | SMA_TREND+REGIME | 0.77 | 0.4 | 12.3 | -25.8 | 73 | 19.2 | 2.06 | 0.335 | 5/7 | REJECT |
| BTC | TSMOM+REGIME | 0.65 | 0.34 | 9.5 | -28.7 | 68 | 32.4 | 1.93 | 0.23 | 3/7 | REJECT |
| BTC | SMA_CROSS | 0.51 | 0.42 | 7.8 | -34.4 | 25 | 40.0 | 1.88 | 0.141 | 3/7 | REJECT |
| BTC | SMA_CROSS+REGIME | 0.41 | 0.0 | 5.5 | -33.9 | 33 | 33.3 | 1.62 | 0.09 | 3/7 | REJECT |
| BTC | DONCHIAN | 0.4 | 0.29 | 5.0 | -30.6 | 26 | 30.8 | 1.64 | 0.085 | 3/7 | REJECT |
| BTC | DONCHIAN+REGIME | 0.33 | 0.19 | 3.8 | -28.6 | 32 | 28.1 | 1.46 | 0.062 | 3/7 | REJECT |
| BTC | RSI_REVERSION+REGIME | 0.18 | 0.07 | 0.9 | -11.6 | 35 | 65.7 | 1.36 | 0.031 | 2/7 | REJECT |
| BTC | RSI_REVERSION | 0.01 | -0.3 | -0.2 | -19.0 | 45 | 73.3 | 1.0 | 0.01 | 2/7 | REJECT |
