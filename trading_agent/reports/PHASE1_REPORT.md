# Fase 1: pesquisa e validação (gate de aprovação)

**Data:** 18/11/2026 · **Status:** aguardando sua aprovação para a Fase 2 · **Dinheiro real:** NÃO · **Escopo:** só BTC (sua decisão em 18/11/2026)

Todos os números vêm de `python research.py` (resultados brutos em `phase1_results.json`). Premissas estão marcadas como **[PREMISSA]**.

---

## 1. Visão geral do sistema

| Item | Definição |
|---|---|
| Mercado | Cripto spot, **somente BTC** contra USD (BTC_USD na Crypto.com). Só compra (long-only), sem alavancagem e sem short |
| Corretora (execução) | Crypto.com Exchange. **[PREMISSA]** Você não citou uma exchange; escolhi esta porque você já tem o conector ativo |
| Dados de pesquisa | Binance (dados públicos), diário, de 17/08/2017 a 17/11/2026. A Crypto.com só tem histórico a partir de 11/2020 |
| Compatibilidade entre as fontes | Correlação dos retornos diários do BTC: 0,9993. Diferença mediana de preço: 0,04%; no percentil 99, 0,30%. Dá para pesquisar numa e executar na outra |
| Custos | **[PREMISSA]** As fontes públicas divergem (0,075% a 0,25%/0,50%). Base: 0,30% por lado (taxa 0,25% + slippage 0,05%). Estresse: 0,60% por lado |
| Conta | Até R$ 5 mil, risco baixo. Tick mínimo de 0,00001 BTC; o tamanho mínimo de ordem não é obstáculo |
| Fuso | America/New_York. O candle diário fecha às 00:00 UTC (19h ou 20h em NY); a revisão noturna roda às 21h NY |
| Timeframe | Diário. Timeframes menores multiplicam custo e ruído, o que é ruim para conta pequena e taxa de varejo |

### Regime atual (17/11/2026, fechamento)
- **BTC: CHOPPY.** US$ 64.947; −14,4% em 10 dias; −22,8% abaixo da máxima de 30 dias; volatilidade de 50% ao ano (percentil 82).
- **Funding dos perpétuos (Crypto.com):** perto de zero (BTC 0,0006% na última leitura). Sem sinal de euforia alavancada. Open interest não foi coletado. Os dois dados são só informativos, porque o sistema não opera derivativos.
- **Quando operar:** só no fechamento diário, com dados validados. **Quando ficar de fora:** dado velho ou inconsistente, erro de API, kill switch ativado.

---

## 2. Classificador de regime: reprovado

Regras simples e fixas (sem otimização): tendência pelo *efficiency ratio* de 20 dias, volatilidade pelo percentil de 1 ano, crash pela queda em 10 dias, pelo drawdown de 30 dias e por volume anormal.

Avaliação: comparei o rótulo de cada dia com o que aconteceu nos 20 dias seguintes.

| | BTC |
|---|---|
| Acerto do classificador | **36,2%** |
| Acerto do palpite ingênuo ("sempre RANGE") | 50,0% |
| CRASH: precisão / recall | 10,9% / 10,7% |
| Retorno médio dos 10 dias seguintes a um rótulo CRASH | +1,41% |

**Conclusão:** o classificador erra 64% das vezes e acerta menos que o palpite ingênuo. Um regime identificado olhando para trás não prevê o regime seguinte. Usar o rótulo como filtro (reduzir exposição em CHOPPY e zerar em CRASH) **piorou** o Sharpe em 4 de 5 estratégias no BTC. Ele **não** entra como filtro de trade. Fica só como relatório informativo, e a proteção contra crash passa a vir do dimensionamento por volatilidade e do kill switch.

---

## 3. Estratégias candidatas

| Estratégia | Edge (1 frase) | Quem está do outro lado | Holding |
|---|---|---|---|
| SMA_TREND | Preço acima da média móvel tende a continuar subindo | Quem vende cedo demais e quem aposta contra a tendência | semanas a meses |
| SMA_CROSS | Mesmo prêmio de tendência, com duas médias | Idem | meses |
| DONCHIAN | Rompimento da máxima de N dias tende a continuar | Quem vende topos e shorts forçados a cobrir | semanas a meses |
| TSMOM | Retorno positivo nos últimos L dias prevê retorno positivo | Investidores ancorados no preço passado | semanas a meses |
| RSI_REVERSION | Queda forte de curto prazo dentro de uma alta de longo prazo tende a voltar | Quem vende em pânico ou é liquidado | 1 a 10 dias |

Sinal separado da execução: o sinal sai no fechamento do dia *t* e a ordem é executada no dia *t+1*. O tamanho da posição é calculado por volatility targeting (20% ao ano na pesquisa) com teto de 100%, sem alavancagem. Cada estratégia foi testada com e sem o filtro de regime.

## 4. Validação

- **Walk-forward:** a melhor variante é escolhida em 2 anos de dados e testada às cegas nos 6 meses seguintes; a janela avança 6 meses e o processo se repete. São 13 janelas de teste, de 16/08/2020 a 17/11/2026, sem divisão aleatória dos dados.
- **112 variantes testadas no BTC.** O *Deflated Sharpe Ratio* (DSR) corrige o resultado por esse número de tentativas. Observação: numa rodada anterior também testei o ETH, mas isso não melhora a escolha do BTC, porque no BTC os resultados foram piores que no ETH.
- **Testes automáticos (13, todos passando):** ausência de look-ahead em todas as estratégias e no classificador, momento correto da execução e dos custos, limites de peso, CRASH zerando a posição, janelas de walk-forward sem sobreposição e validação de dados ruins.
- **Critérios de aprovação, definidos antes de ver os resultados** (é preciso passar nos 7):
  1. Sharpe acima do buy-and-hold puro;
  2. Sharpe acima do buy-and-hold com o mesmo dimensionamento por volatilidade;
  3. com custo dobrado, ainda vence os dois benchmarks;
  4. DSR ≥ 0,95;
  5. mediana das variantes ≥ 50% do Sharpe do walk-forward;
  6. pelo menos 20 trades;
  7. drawdown não pior que o benchmark.

### Tabela comparativa: BTC, fora da amostra (16/08/2020 a 17/11/2026), líquida de custos

| Estratégia | Sharpe | Sharpe 2x custo | CAGR % | Max DD % | Trades | Win % | PF | DSR | Critérios | Veredito |
|---|---|---|---|---|---|---|---|---|---|---|
| *Buy & hold* | 0,76 | – | 31,2 | −76,6 | – | – | – | – | – | benchmark |
| *Buy & hold vol-target 20%* | 0,68 | – | 14,1 | −39,8 | – | – | – | – | – | benchmark |
| TSMOM | 0,81 | 0,66 | 12,8 | −29,1 | 43 | 34,9 | 3,02 | 0,37 | 5/7 | REJECT |
| SMA_TREND | 0,80 | 0,62 | 13,9 | −31,5 | 62 | 22,6 | 2,28 | 0,36 | 5/7 | REJECT |
| SMA_TREND+REGIME | 0,77 | 0,40 | 12,3 | −25,8 | 73 | 19,2 | 2,06 | 0,34 | 5/7 | REJECT |
| TSMOM+REGIME | 0,65 | 0,34 | 9,5 | −28,7 | 68 | 32,4 | 1,93 | 0,23 | 3/7 | REJECT |
| SMA_CROSS | 0,51 | 0,42 | 7,8 | −34,4 | 25 | 40,0 | 1,88 | 0,14 | 3/7 | REJECT |
| SMA_CROSS+REGIME | 0,41 | 0,00 | 5,5 | −33,9 | 33 | 33,3 | 1,62 | 0,09 | 3/7 | REJECT |
| DONCHIAN | 0,40 | 0,29 | 5,0 | −30,6 | 26 | 30,8 | 1,64 | 0,09 | 3/7 | REJECT |
| DONCHIAN+REGIME | 0,33 | 0,19 | 3,8 | −28,6 | 32 | 28,1 | 1,46 | 0,06 | 3/7 | REJECT |
| RSI_REVERSION+REGIME | 0,18 | 0,07 | 0,9 | −11,6 | 35 | 65,7 | 1,36 | 0,03 | 2/7 | REJECT |
| RSI_REVERSION | 0,01 | −0,30 | −0,2 | −19,0 | 45 | 73,3 | 1,00 | 0,01 | 2/7 | REJECT |

Os resultados por janela de 6 meses estão em `phase1_results.json` (`candidates[].per_fold`).

### Leitura crítica
1. **Nenhuma estratégia passou nos 7 critérios.** O melhor DSR foi 0,37 (TSMOM), contra 0,95 exigido. Isso significa cerca de 37% de probabilidade de o edge ser real, o que não basta para arriscar capital.
2. **TSMOM e SMA_TREND falharam em 2 critérios:** com custo dobrado, o Sharpe (0,66 e 0,62) fica abaixo do buy-and-hold (0,76), e o DSR é insuficiente. Nos outros 5 critérios elas passaram: batem os dois benchmarks no custo base, os parâmetros são robustos (a mediana das variantes é 0,74 a 0,77), têm trades suficientes e drawdown menor.
3. **O ganho comprovado é de risco, não de retorno.** A queda máxima cai de −77% para cerca de −30%. Em troca, o CAGR cai de 31% para cerca de 13%, porque a posição média fica bem abaixo de 100%.
4. **A taxa é o gargalo:** cerca de 3,4% ao ano de custo na SMA_TREND e 2,2% na TSMOM. Com taxa de varejo, isso consome boa parte da vantagem.
5. **Comprar quedas (RSI) não funciona no BTC:** win rate de 73%, mas o profit factor é 1,0.
6. O período fora da amostra inclui dois grandes mercados de alta, o que favorece estratégias de tendência.

## 5. Veredito do gate da Fase 1

**RECUSO operar BTC com dinheiro real.** Nenhuma estratégia bateu o benchmark de forma estatisticamente confiável depois dos custos.

### Opções para você decidir

| Opção | O que é | Minha avaliação |
|---|---|---|
| **A. Fase 2 só em paper trading (recomendada)** | Motor de risco, kill switch, execução na Crypto.com e revisão noturna. Rodar BTC TSMOM e BTC SMA_TREND em simulação por pelo menos 6 meses | Mede o custo real (que é o ponto fraco) e valida a infraestrutura. **Não** prova o edge |
| B. Reduzir custo antes de tudo | Confirmar a sua taxa real na Crypto.com e usar ordens limit (maker). Se a taxa real ficar perto de 0,075%, rodo a validação de novo | Barato e com alto impacto: o custo é o principal motivo da reprovação |
| C. Parar aqui | Para uma conta de R$ 5 mil, um aporte mensal fixo (DCA) em BTC com a regra de tendência só para reduzir a exposição em quedas | Muitas vezes é a decisão financeira certa |


### Opção B executada: sensibilidade à taxa (18/11/2026)
Validação completa refeita para cada faixa de taxa (custo = taxa + 0,05% de slippage). Tabela em `fee_sensitivity.md`.

| Taxa por lado | SMA_TREND | TSMOM |
|---|---|---|
| 0,075% (maker, faixa baixa) | Sharpe 0,95 · 6/7 · DSR 0,65 · **WATCHLIST** | Sharpe 0,82 · 6/7 · DSR 0,53 · **WATCHLIST** |
| 0,10% | Sharpe 0,92 · 6/7 · DSR 0,60 · **WATCHLIST** | Sharpe 0,81 · 6/7 · DSR 0,49 · **WATCHLIST** |
| 0,15% | 5/7 · REJECT | 4/7 · REJECT |
| 0,25% | 5/7 · REJECT | 5/7 · REJECT |
| 0,50% (taker de varejo) | 4/7 · REJECT (perde para o buy-and-hold) | 4/7 · REJECT |

**Linha de corte: taxa de até 0,10% por lado.** Acima disso, as duas reprovam. Abaixo disso, passam em 6 dos 7 critérios e falham só no DSR (máximo de 0,65 contra 0,95). Mesmo no melhor caso, **dinheiro real continua vetado**. A taxa define se vale ir para a simulação (Opção A).

### Se você aprovar a Opção A, estas regras já ficam travadas no código da Fase 2
- **Dimensionamento:** volatilidade-alvo de 10% ao ano (e não 20%), o que reduz pela metade os drawdowns da tabela (estimativa: −10% a −16%). **[ESTIMATIVA]** Ainda é preciso validar se isso fica abaixo do kill switch. Teto de 30% da conta em BTC; frações de Kelly (nunca Kelly cheio) só depois de existir histórico real.
- **Limites, todos em código:** perda diária máxima de 3%; **drawdown máximo de 15%, que zera todas as posições e trava o sistema**; dado com mais de 26h é considerado velho e bloqueia ordens; 3 erros de API seguidos param o sistema; o kill switch é checado antes de **toda** ordem.
- **Fail closed:** qualquer dúvida (dado inválido, saldo divergente, resposta inesperada da API) significa não operar e registrar o motivo.
- **IA nunca decide.** Ela pode sugerir na revisão noturna; quem decide é o código determinístico. Nenhuma mudança é aplicada sem a sua aprovação.
- **Chave de API sem permissão de saque.** O agente nunca move fundos nem altera os próprios limites.
- **Critérios de desligamento automático (bear case ao vivo):** drawdown acima de 15%; Sharpe móvel de 6 meses abaixo de −1; custo real médio acima de 2x o modelado; 3 meses seguidos rendendo menos que o buy-and-hold vol-target por mais de 5 pontos percentuais.
- **Métricas monitoradas:** PnL, exposição, drawdown, slippage real versus modelado, latência e erros de API, idade do dado, divergência entre o sinal do backtest e o sinal ao vivo.

## 6. Plano de construção

```
trading_agent/
  agent/data.py          dados + validação (fail closed)        ✅ Fase 1
  agent/regime.py        classificador + avaliação               ✅ Fase 1 (reprovado, só informativo)
  agent/strategies.py    sinais (sem execução)                   ✅ Fase 1
  agent/backtest.py      custos, sizing, trades                  ✅ Fase 1
  agent/metrics.py       Sharpe, DD, PF, Deflated Sharpe         ✅ Fase 1
  agent/walkforward.py   walk-forward                            ✅ Fase 1
  research.py            pipeline reprodutível                   ✅ Fase 1
  tests/test_core.py     13 testes                               ✅ Fase 1
  agent/risk.py          limites + kill switch                   ⏳ Fase 2: PRIMEIRO módulo
  agent/broker.py        cliente Crypto.com (paper + live)       ⏳ Fase 2
  agent/runner.py        loop diário 24/7                        ⏳ Fase 2
  agent/journal.py       log de toda decisão (input/output)      ⏳ Fase 2
  nightly_review.py      relatório noturno, sem auto-aplicar     ⏳ Fase 2
```

- **Primeiro módulo da Fase 2:** `agent/risk.py`, escrito com os testes antes do código. O kill switch não pode depender de nenhum outro módulo.
- **Reproduzir a Fase 1:** `cd trading_agent && pip install -r requirements.txt && pytest && python research.py`
- **Comando de paper trading:** ainda não existe. Ele só será criado depois da sua aprovação, como `python -m agent.runner --mode paper`.

---

## HOW CAN THIS SYSTEM FAIL?

1. **O edge não existe.** É a hipótese principal, segundo o DSR. A tendência em cripto já é amplamente conhecida e operada; o que sobra pode ser só o prêmio de risco do próprio ativo.
2. **Regime diferente.** O teste cobriu 2020 a 2026, com dois mercados de alta. Um mercado lateral longo (como 2018–2019) produz serrote e custo sem retorno.
3. **Custos maiores que o modelado.** No BTC, com custo dobrado, nenhuma estratégia de tendência bate o benchmark. Taxa de varejo é o principal gargalo de uma conta de R$ 5 mil.
4. **Gap no fechamento.** Uma queda de 20% em poucas horas, antes da decisão diária, passa por cima do stop e pode estourar a perda diária. O dimensionamento por volatilidade reduz, mas não elimina, esse risco.
5. **Falha da exchange ou da API:** fora do ar, saque bloqueado, mudança de regras ou de taxas, risco de contraparte (precedente: FTX). Mitigação: fail closed, chave sem saque e nunca deixar na exchange mais do que a conta de trading.
6. **Falha da infraestrutura.** A máquina cai e a posição fica aberta sem gestão. Mitigação: stop de proteção registrado na própria exchange e alerta de "heartbeat".
7. **Divergência entre as fontes de dados.** A pesquisa usa Binance e a execução usa Crypto.com. A diferença média é baixa (0,04%), mas no percentil 99 chega a 0,3%.
8. **Erro humano ou de IA.** Alguém altera limites ou aplica uma "melhoria" sugerida sem validação. Mitigação: limites no código, nenhuma mudança sem a sua aprovação e nova validação completa a cada alteração.
9. **Viés do próprio processo.** Escolhi as 5 famílias de estratégia sabendo, de antemão, que tendência costuma funcionar em cripto. Isso é um viés de seleção que o DSR não captura totalmente.

**Prioridade: sobreviver.** Com o resultado de hoje, o sistema mais seguro é o que não opera dinheiro real.
