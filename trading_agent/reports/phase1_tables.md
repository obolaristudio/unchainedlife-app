_Gerado em 2026-11-18T11:31:14+00:00 por `python research.py`. Variantes testadas: 224._

| Ativo | Estratégia | Sharpe | Sharpe 2x custo | CAGR % | Max DD % | Trades | Win % | PF | DSR | Testes ok | Veredito |
|---|---|---|---|---|---|---|---|---|---|---|---|
| BTC | *Buy & hold* | 0.76 | – | 31.2 | -76.6 | – | – | – | – | – | benchmark |
| BTC | *Buy & hold vol-target 20%* | 0.68 | – | 14.1 | -39.8 | – | – | – | – | – | benchmark |
| ETH | *Buy & hold* | 0.68 | – | 25.9 | -79.3 | – | – | – | – | – | benchmark |
| ETH | *Buy & hold vol-target 20%* | 0.62 | – | 12.9 | -40.6 | – | – | – | – | – | benchmark |
| BTC | TSMOM | 0.81 | 0.66 | 12.8 | -29.1 | 43 | 34.9 | 3.02 | 0.168 | 5/7 | REJECT |
| BTC | SMA_TREND | 0.8 | 0.62 | 13.9 | -31.5 | 62 | 22.6 | 2.28 | 0.164 | 5/7 | REJECT |
| BTC | SMA_TREND+REGIME | 0.77 | 0.4 | 12.3 | -25.8 | 73 | 19.2 | 2.06 | 0.146 | 5/7 | REJECT |
| BTC | TSMOM+REGIME | 0.65 | 0.34 | 9.5 | -28.7 | 68 | 32.4 | 1.93 | 0.086 | 3/7 | REJECT |
| BTC | SMA_CROSS | 0.51 | 0.42 | 7.8 | -34.4 | 25 | 40.0 | 1.88 | 0.045 | 3/7 | REJECT |
| BTC | SMA_CROSS+REGIME | 0.41 | 0.0 | 5.5 | -33.9 | 33 | 33.3 | 1.62 | 0.025 | 3/7 | REJECT |
| BTC | DONCHIAN | 0.4 | 0.29 | 5.0 | -30.6 | 26 | 30.8 | 1.64 | 0.023 | 3/7 | REJECT |
| BTC | DONCHIAN+REGIME | 0.33 | 0.19 | 3.8 | -28.6 | 32 | 28.1 | 1.46 | 0.015 | 3/7 | REJECT |
| BTC | RSI_REVERSION+REGIME | 0.18 | 0.07 | 0.9 | -11.6 | 35 | 65.7 | 1.36 | 0.007 | 2/7 | REJECT |
| BTC | RSI_REVERSION | 0.01 | -0.3 | -0.2 | -19.0 | 45 | 73.3 | 1.0 | 0.002 | 2/7 | REJECT |
| ETH | DONCHIAN | 0.97 | 0.85 | 15.6 | -20.5 | 19 | 52.6 | 3.76 | 0.279 | 5/7 | WATCHLIST |
| ETH | SMA_TREND | 0.88 | 0.64 | 15.6 | -25.8 | 52 | 25.0 | 2.59 | 0.213 | 5/7 | REJECT |
| ETH | SMA_TREND+REGIME | 0.81 | 0.67 | 13.3 | -25.8 | 66 | 22.7 | 2.1 | 0.162 | 5/7 | REJECT |
| ETH | DONCHIAN+REGIME | 0.73 | 0.64 | 9.2 | -20.5 | 31 | 41.9 | 2.12 | 0.121 | 5/7 | REJECT |
| ETH | TSMOM | 0.66 | 0.67 | 11.2 | -31.2 | 67 | 29.9 | 2.04 | 0.087 | 4/7 | REJECT |
| ETH | SMA_CROSS | 0.53 | 0.47 | 8.6 | -34.0 | 20 | 45.0 | 2.22 | 0.047 | 3/7 | REJECT |
| ETH | TSMOM+REGIME | 0.51 | 0.31 | 7.5 | -31.7 | 84 | 26.2 | 1.58 | 0.04 | 3/7 | REJECT |
| ETH | SMA_CROSS+REGIME | 0.41 | 0.29 | 5.6 | -30.5 | 46 | 32.6 | 1.55 | 0.022 | 3/7 | REJECT |
| ETH | RSI_REVERSION | -0.01 | -0.01 | -0.2 | -9.6 | 18 | 55.6 | 0.93 | 0.001 | 2/7 | REJECT |
| ETH | RSI_REVERSION+REGIME | -0.13 | -0.25 | -0.5 | -12.2 | 15 | 53.3 | 0.81 | 0.0 | 1/7 | REJECT |
