# Fase 1: pesquisa e validação (gate de aprovação)

**Data:** 18/11/2026 · **Status:** aguardando sua aprovação para a Fase 2 · **Dinheiro real:** NÃO

Todos os números vêm de `python research.py` (resultados brutos em `phase1_results.json`). Premissas estão marcadas como **[PREMISSA]**.

---

## 1. Visão geral do sistema

| Item | Definição |
|---|---|
| Mercado | Cripto spot, BTC e ETH contra USD. Só compra (long-only), sem alavancagem e sem short |
| Corretora (execução) | Crypto.com Exchange. **[PREMISSA]** Você não citou uma exchange; escolhi esta porque você já tem o conector ativo |
| Dados de pesquisa | Binance (dados públicos), diário, de 17/08/2017 a 17/11/2026. A Crypto.com só tem histórico a partir de 11/2020 |
| Compatibilidade entre as fontes | Correlação dos retornos diários: 0,9993 (BTC) e 0,9999 (ETH). Diferença mediana de preço: 0,04%. Dá para pesquisar numa e executar na outra |
| Custos | **[PREMISSA]** As fontes públicas divergem (0,075% a 0,25%/0,50%). Base: 0,30% por lado (taxa 0,25% + slippage 0,05%). Estresse: 0,60% por lado |
| Conta | Até R$ 5 mil, risco baixo. Tick mínimo de 0,00001 BTC; o tamanho mínimo de ordem não é obstáculo |
| Fuso | America/New_York. O candle diário fecha às 00:00 UTC (19h ou 20h em NY); a revisão noturna roda às 21h NY |
| Timeframe | Diário. Timeframes menores multiplicam custo e ruído, o que é ruim para conta pequena e taxa de varejo |

### Regime atual (17/11/2026, fechamento)
- **BTC: CHOPPY.** US$ 64.947; −14,4% em 10 dias; −22,8% abaixo da máxima de 30 dias; volatilidade de 50% ao ano (percentil 82).
- **ETH: CRASH.** US$ 1.825; −18,5% em 10 dias; −26,2% abaixo da máxima de 30 dias.
- **Funding dos perpétuos (Crypto.com):** perto de zero (BTC 0,0006%, ETH 0,0014% na última leitura). Sem sinal de euforia alavancada. Open interest não foi coletado. Os dois dados são só informativos, porque o sistema não opera derivativos.
- **Quando operar:** só no fechamento diário, com dados validados. **Quando ficar de fora:** dado velho ou inconsistente, erro de API, kill switch ativado.

---

## 2. Classificador de regime: reprovado

Regras simples e fixas (sem otimização): tendência pelo *efficiency ratio* de 20 dias, volatilidade pelo percentil de 1 ano, crash pela queda em 10 dias, pelo drawdown de 30 dias e por volume anormal.

Avaliação: comparei o rótulo de cada dia com o que aconteceu nos 20 dias seguintes.

| | BTC | ETH |
|---|---|---|
| Acerto do classificador | **36,2%** | **35,9%** |
| Acerto do palpite ingênuo ("sempre RANGE") | 50,0% | 50,2% |
| CRASH: precisão / recall | 10,9% / 10,7% | 23,0% / 25,3% |
| Retorno médio dos 10 dias seguintes a um rótulo CRASH | +1,41% | +0,30% |

**Conclusão:** o classificador erra 64% das vezes e acerta menos que o palpite ingênuo. Um regime identificado olhando para trás não prevê o regime seguinte. Usar o rótulo como filtro (reduzir exposição em CHOPPY e zerar em CRASH) **piorou** o Sharpe em 9 de 10 comparações. Ele **não** entra como filtro de trade. Fica só como relatório informativo, e a proteção contra crash passa a vir do dimensionamento por volatilidade e do kill switch.

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
- **224 variantes testadas no total.** O *Deflated Sharpe Ratio* (DSR) corrige o resultado por esse número de tentativas.
- **Testes automáticos (13, todos passando):** ausência de look-ahead em todas as estratégias e no classificador, momento correto da execução e dos custos, limites de peso, CRASH zerando a posição, janelas de walk-forward sem sobreposição e validação de dados ruins.
- **Critérios de aprovação, definidos antes de ver os resultados** (é preciso passar nos 7):
  1. Sharpe acima do buy-and-hold puro;
  2. Sharpe acima do buy-and-hold com o mesmo dimensionamento por volatilidade;
  3. com custo dobrado, ainda vence os dois benchmarks;
  4. DSR ≥ 0,95;
  5. mediana das variantes ≥ 50% do Sharpe do walk-forward;
  6. pelo menos 20 trades;
  7. drawdown não pior que o benchmark.

### Tabela comparativa (fora da amostra, líquida de custos)

| Ativo | Estratégia | Sharpe | Sharpe 2x custo | CAGR % | Max DD % | Trades | Win % | PF | DSR | Critérios | Veredito |
|---|---|---|---|---|---|---|---|---|---|---|---|
| BTC | *Buy & hold* | 0,76 | – | 31,2 | −76,6 | – | – | – | – | – | benchmark |
| BTC | *Buy & hold vol-target 20%* | 0,68 | – | 14,1 | −39,8 | – | – | – | – | – | benchmark |
| ETH | *Buy & hold* | 0,68 | – | 25,9 | −79,3 | – | – | – | – | – | benchmark |
| ETH | *Buy & hold vol-target 20%* | 0,62 | – | 12,9 | −40,6 | – | – | – | – | – | benchmark |
| ETH | DONCHIAN | 0,97 | 0,85 | 15,6 | −20,5 | 19 | 52,6 | 3,76 | 0,28 | 5/7 | **WATCHLIST** |
| ETH | SMA_TREND | 0,88 | 0,64 | 15,6 | −25,8 | 52 | 25,0 | 2,59 | 0,21 | 5/7 | REJECT |
| BTC | TSMOM | 0,81 | 0,66 | 12,8 | −29,1 | 43 | 34,9 | 3,02 | 0,17 | 5/7 | REJECT |
| BTC | SMA_TREND | 0,80 | 0,62 | 13,9 | −31,5 | 62 | 22,6 | 2,28 | 0,16 | 5/7 | REJECT |
| ETH | TSMOM | 0,66 | 0,67 | 11,2 | −31,2 | 67 | 29,9 | 2,04 | 0,09 | 4/7 | REJECT |
| BTC/ETH | SMA_CROSS | 0,51 / 0,53 | 0,42 / 0,47 | 7,8 / 8,6 | −34 | 25 / 20 | | | ≤0,05 | 3/7 | REJECT |
| BTC | DONCHIAN | 0,40 | 0,29 | 5,0 | −30,6 | 26 | 30,8 | 1,64 | 0,02 | 3/7 | REJECT |
| BTC/ETH | RSI_REVERSION | 0,01 / −0,01 | < 0 | ~0 | −19 / −10 | 45 / 18 | | ~1,0 | 0,00 | 2/7 | REJECT |

Tabela completa, incluindo as variantes "+REGIME" (todas reprovadas), em `phase1_tables.md`. Os resultados por janela de 6 meses estão no JSON (`candidates[].per_fold`).

### Leitura crítica
1. **Nenhuma estratégia passou nos 7 critérios.** O DSR mais alto foi 0,28, muito abaixo de 0,95. Com 224 tentativas, um Sharpe de 0,8 a 1,0 em 6 anos é o que se espera encontrar **por sorte**.
2. **Seguir tendência reduz o risco, mas não comprovou retorno extra.** Ela corta o drawdown de −77% para −20% a −30%, e isso é real e consistente. Mas o Sharpe só fica 0,05 a 0,2 acima do buy-and-hold, e a vantagem some com custo dobrado no BTC.
3. **ETH DONCHIAN**, a melhor da lista, tem só 19 trades em 6 anos, e o walk-forward escolheu 4 conjuntos de parâmetros diferentes ao longo das 13 janelas. A amostra é pequena demais para confiar.
4. **Reversão à média (RSI) não funciona** com taxa de varejo. Tem win rate de 73%, mas o profit factor é 1,0.
5. O período fora da amostra (2020 a 2026) inclui dois grandes mercados de alta, o que favorece estratégias de tendência. O resultado pode estar otimista.

## 5. Veredito do gate da Fase 1

**RECUSO operar com dinheiro real.** Esta é exatamente a regra do prompt: *"se não bater o benchmark depois dos custos, recuse operar"*. Nenhuma estratégia bateu de forma estatisticamente confiável.

### Opções para você decidir

| Opção | O que é | Custo | Minha avaliação |
|---|---|---|---|
| **A. Fase 2 só em paper trading (recomendada)** | Construir o motor de risco, o kill switch, a execução e a revisão noturna. Rodar ETH DONCHIAN e BTC SMA_TREND em simulação por pelo menos 6 meses | Tempo de desenvolvimento, zero capital | Valida a infraestrutura, os custos reais e o slippage. **Não** prova o edge: para isso seriam necessários anos |
| B. Ampliar a pesquisa | Momentum entre as 20 maiores moedas, timeframe de 4h, carry de funding | Mais variantes, o que exige um DSR ainda mais alto | Probabilidade baixa de passar; risco de *data mining* |
| C. Parar aqui | Usar o resultado como decisão: para conta pequena, um aporte periódico (DCA) com regra de tendência para reduzir drawdown é mais honesto que um robô 24/7 | Zero | Muitas vezes é a decisão financeira certa |

### Se você aprovar a Opção A, estas regras já ficam travadas no código da Fase 2
- **Dimensionamento:** volatilidade-alvo de 10% ao ano (e não 20%), o que reduz pela metade os drawdowns da tabela (estimativa: −10% a −16%). **[ESTIMATIVA]** Ainda é preciso validar se isso fica abaixo do kill switch. Teto de 30% da conta por ativo; frações de Kelly (nunca Kelly cheio) só depois de existir histórico real.
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
