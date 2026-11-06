# Radar de ferramentas e repositórios (Operação 24 h)

Registro de tudo que foi avaliado. Status: `avaliar` → `instalado` / `descartado` / `sugerido ao Maxwell` (assinatura/cadastro).

| Data | Nome | Tipo | Para quê | Licença / custo | Status | Observação |
|---|---|---|---|---|---|---|
| 2026-11-06 | Aperivue/medsci-skills | repo GitHub (skills) | Busca de literatura no PubMed e checagem de citações para validar fatos dos vídeos | MIT, grátis | avaliar | Ler o código antes de instalar |
| 2026-11-06 | remotion-dev/template-tiktok | repo GitHub | Legendas estilo TikTok com Whisper em vídeo React (Remotion) | sem licença declarada; Remotion exige licença paga para empresas com 4+ pessoas | avaliar | Só se o pipeline atual (HTML + ffmpeg) não bastar |
| 2026-11-06 | rediumvex/ai-video-generator-claude | repo GitHub (skills) | Prompts de vídeo para Seedance no Higgsfield | MIT, grátis | avaliar | Pode melhorar as cenas geradas |
| 2026-11-06 | SamurAIGPT/AI-Faceless-Video-Generator | repo GitHub | Roteiro + voz + rosto falante por IA | MIT, grátis | descartado por ora | Sobrepõe o que já fazemos com ElevenLabs/Higgsfield |
| 2026-11-06 | ManyChat (ou automação oficial de DM da Meta) | ferramenta paga | Resposta instantânea "comente PALAVRA → DM" (hoje a nossa leva até 1 h) | plano pago | sugerido ao Maxwell | Útil quando o guia grátis estiver pronto |
| 2026-11-06 | Clipwing/skills → real-sfx (commit edbefcb) | skill Claude Code | Sound design com sons REAIS gravados: acha os momentos, coloca no frame, mixa, entrega MP4 + trilha SFX + relatório | MIT (scripts) + uisfx CC0 | instalado | `.claude/skills/real-sfx`; bibliotecas: brand/sfx-cc0 (main), brand/sfx (extra), uisfx 1.895 sons CC0 |
| 2026-11-06 | Leonxlnx/earshot v0.4.1 (commit 4ac3d2a) | CLI + skills (earshot, real-sound) | "Ouvido" do agente: descreve/compara sons, checa sync e loudness, banco de 252 SFX | MIT, grátis | instalado | `pip install --no-deps` + torch CPU; já pegou 6 arquivos "CC0" que eram só voz |
| 2026-11-06 | Freesound / Mixkit / Sonniss GDC | bancos de som reais | Ampliar a biblioteca de whoosh/impacto/riser reais | grátis (checar licença de cada um) | sugerido ao Maxwell | Downloads automáticos bloqueados aqui; baixe um pack e jogue no Google Drive, que eu importo |
| 2026-11-06 | heygen-com/hyperframes (commit 9acdce4, CLI 0.9.19) | skills + CLI | Base dos 20 efeitos virais; reverse-any-video para replicar estrutura de virais | Apache-2.0, grátis | instalado (skills) | Rodar só `npx hyperframes@0.9.19`; pular o beacon de telemetria |
| 2026-11-06 | Pack "20 AI Video Effects" (David Roberts) | prompts + templates | Galeria de efeitos (skill efeitos-virais) | uso livre | instalado (prompts) / templates pendentes | Zip no Drive não visível ao conector: Maxwell precisa abrir a pasta ou copiar o zip para o Drive dele |
| 2026-11-06 | Klint (tryklint.ai) | MCP pago | Achar Reels que fizeram 3x+ a mediana do criador, com análise de efeitos | pago | sugerido ao Maxwell | Alternativa: gpt_social já conectado |
| 2026-11-06 | GTAI-1/flow-mcp (commit 84b548f) | MCP local (Mac) | Google Flow via Claude: Veo 3.1 e Nano Banana com os créditos do plano Google AI | ISC, grátis (usa créditos Google) | auditado, aguardando instalação no Mac | Automatiza a interface do Flow (risco nos termos do Google); usar conta Google separada. Passo a passo em research/flow-mcp-instalacao.md |
