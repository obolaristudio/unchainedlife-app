# trader/

Pasta de trabalho do Day Trader skill pack (11 skills em `.claude/skills/trader-*`).
Cada skill lê e grava aqui (plan.json, orders.json, portfolio.json, state/).

Fluxo de um trade:
scanner -> news -> entry -> exit -> timemachine -> budget -> risk -> broker

Config SEC (necessário para /trader-news e /trader-analyst): edite `config.json`.
