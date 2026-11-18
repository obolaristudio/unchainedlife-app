# trading_agent: agente de trading cripto (Crypto.com, spot, long-only)

Construído em fases, com aprovação do Maxwell a cada gate. **Status: Fase 1 concluída; nenhum dinheiro real.**

- Relatório da Fase 1 (veredito, tabela, riscos): [`reports/PHASE1_REPORT.md`](reports/PHASE1_REPORT.md)
- Reproduzir:
  ```bash
  cd trading_agent
  pip install -r requirements.txt
  pytest                 # 13 testes (look-ahead, custos, limites, folds, dados)
  python research.py     # baixa dados públicos, roda walk-forward e gera reports/
  ```

Regras permanentes: a IA sugere, o código decide; limites e kill switch ficam no código; fail closed; o agente nunca saca nem altera os próprios limites; nenhuma mudança é aplicada sem aprovação.
