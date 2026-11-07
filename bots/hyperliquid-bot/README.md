# Bot Hyperliquid: tendência EMA 20/50

Bot simples e auditável para operar **BTC perpétuo na Hyperliquid** com regras fixas e risco conservador.

> ⚠️ Trade alavancado pode zerar o capital. O backtest não garante resultado futuro. Use só dinheiro que você aceita perder.

## Regras

| Item | Valor |
|---|---|
| Ativo / tempo gráfico | BTC, candles de **4h** (`INTERVAL=1h` também funciona) |
| Entrada **long** | EMA 20 cruza para **cima** da EMA 50 (candle fechado) |
| Entrada **short** | EMA 20 cruza para **baixo** da EMA 50 |
| Stop | 1,5 × ATR(14) a partir da entrada, enviado **na corretora** |
| Alvo | 2 × a distância do stop (2:1) |
| Saída antecipada | Cruzamento contrário fecha a posição e abre a oposta |
| Alavancagem máx. | 3x (isolada) |
| Risco por trade | 2% do capital |
| Trava diária | Sem novas entradas no dia (UTC) depois de perder 5% |
| Proteção | Não mexe em posição que o bot não abriu |

## Backtest (dados reais da Hyperliquid, capital de US$ 30, já com taxas)

| Tempo gráfico | Período | Resultado | Acerto | Profit factor | Drawdown máx. | Só segurar BTC |
|---|---|---|---|---|---|---|
| 1h | abr–nov/2026 | +9,8% | 40,7% | 1,08 | 16,5% | +0,7% |
| **4h** | **ago/2024–nov/2026** | **+37,0%** | **42,5%** | **1,29** | **15,9%** | +28,0% |

Leitura honesta: o 1h fica praticamente no empate (profit factor 1,08). O 4h tem vantagem pequena e consistente num período maior. É por isso que o padrão é **4h**. A estratégia acerta menos da metade das vezes e lucra porque os ganhos são o dobro das perdas. Espere sequências de 4 a 6 stops seguidos.

Para rodar de novo: `python backtest.py --interval 4h --capital 30`

## Instalação na VPS (Ubuntu, ~US$ 5/mês)

```bash
# 1. usuário dedicado e código
sudo adduser --disabled-password --gecos "" bot
sudo apt update && sudo apt install -y python3-venv git
sudo -iu bot
git clone <URL-DO-REPO> repo && cp -r repo/bots/hyperliquid-bot ~/hyperliquid-bot
cd ~/hyperliquid-bot
python3 -m venv venv && ./venv/bin/pip install -r requirements.txt

# 2. configuração (edite com seus dados)
cp .env.example .env && chmod 600 .env && nano .env

# 3. teste rápido
./venv/bin/python backtest.py
./venv/bin/python bot.py --once
exit

# 4. deixar rodando 24h
sudo cp /home/bot/hyperliquid-bot/deploy/hl-bot.service /etc/systemd/system/
sudo systemctl daemon-reload && sudo systemctl enable --now hl-bot
journalctl -u hl-bot -f        # acompanhar o log
```

## Ordem segura para ligar

1. **Semana 1: `DRY_RUN=true`.** O bot só registra o que faria. Confira os sinais no `bot.log`.
2. **Semanas 2 a 4: `DRY_RUN=false` com US$ 20–50.** Opera de verdade, com pouco dinheiro.
3. **Só aumente o capital** depois de pelo menos 15 a 20 operações reais com resultado parecido com o do backtest.

## Segurança

- Use uma **carteira só para o bot**, separada da do Fomo.
- No `.env` vai a chave da **API Wallet** (opera, mas não saca), nunca a chave da carteira principal.
- O `.env` nunca vai para o GitHub (está no `.gitignore`).
- Para desligar na hora: `sudo systemctl stop hl-bot`. Stop e alvo já enviados continuam valendo na corretora.
