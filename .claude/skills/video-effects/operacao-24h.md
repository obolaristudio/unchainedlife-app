# Operação 24 h — @obolari_academy (missão do Maxwell, 06/11/2026)

Objetivo: transformar o perfil numa máquina de crescer seguidores com conteúdo de qualidade sobre **peptídeos, longevidade, vitaminas e bem-estar**, sempre educativo e baseado em evidência. Esta é a ordem de prioridade quando houver conflito: **Regra nº 1 (conta segura) > qualidade/fato correto > volume**.

## Quem faz o quê (tarefas agendadas)
| Tarefa | Quando | O que faz |
|---|---|---|
| Rotina Madrugada Peptídeos | todo dia ~04:47 BRT | pesquisa virais + notícias/estudos da semana → produz **2 Reels + 1 carrossel** → fila de publicação |
| Respostas comentários Instagram | de hora em hora (08:00–23:59 BRT) | publica o que está na fila no horário, responde comentários, avisa casos sensíveis |
| Revisão semanal de crescimento | segunda ~08:47 BRT | lê métricas, ranqueia posts, ajusta temas/horários/ganchos e manda relatório |

## Linha editorial (mix semanal)
- **50 % peptídeos** (série "um peptídeo por vídeo", mito × verdade, comparativos).
- **30 % longevidade** (sono, músculo e envelhecimento, VO2máx, glicose/insulina, inflamação, jejum — sempre com o que a ciência mostra).
- **20 % vitaminas e bem-estar** (vitamina D, magnésio, ômega-3, creatina, B12, colágeno, probióticos — o que é, para que serve segundo estudos, quem costuma ter deficiência, quando falar com o médico). **Sem dose individual**: no máximo citar a recomendação oficial de ingestão diária (RDA/ANVISA) quando for o ponto do vídeo.
- Fontes de pesquisa diárias: virais (TikTok/Instagram via gpt_social e yt-dlp), PubMed/estudos novos, FDA/Anvisa/EMA, notícias de saúde confiáveis (NIH, Harvard Health, Examine, The Lancet, NEJM). Registrar em `research/usados.md`.

## Formatos que fazem crescer
1. **Reels** (2/dia): estrutura do viral + camadas (cenas Higgsfield/Buzzy, imagens CC0, cards, transições, SFX, música, legenda palavra a palavra).
2. **Carrossel** (1/dia): 6–8 slides 1080×1350 no visual da marca, gerados em HTML→PNG (sem custo de crédito): capa com gancho, 4–6 slides de conteúdo (lista, mito × fato, comparação), slide final com aviso + "Salve e comente". Carrossel gera salvamentos e compartilhamentos, que puxam alcance. Publicar como `media_type CAROUSEL` (containers filhos `is_carousel_item`).
3. Ganchos que mais retêm: pergunta no 1º segundo, mito × verdade, "o que ninguém te conta sobre…", número grande, identidade ("Você que tem mais de 40…").
4. CTA de comentário sempre (pergunta aberta). Palavra-chave só com guia próprio aprovado.

## Orçamento de créditos (avisar o Maxwell antes de acabar)
- Higgsfield: ~6 créditos por clipe. **Reaproveitar a biblioteca de clipes** já gerados (pasta de clipes no ramo `media`) + imagens/vídeos CC0 antes de gerar novos; meta ≤ 5 clipes novos por dia. Alertar quando o saldo < 150.
- ElevenLabs: narração com **1 versão** (`generations_count: 1`) nas rotinas para economizar; efeitos sonoros já estão em `brand/sfx/`. Se der erro de saldo, parar e avisar.
- Buzzy e Captions: sem consulta de saldo; erro de crédito = parar e avisar.

## Deixar de seguir (só manual)
A API do Instagram não permite seguir/deixar de seguir nem listar quem a conta segue; automação não oficial viola os termos e pode derrubar a conta. O Maxwell faz no app: Perfil → Seguindo → "Menos interagidos" → até ~50–100 por dia, mantendo ~50 perfis relevantes (especialistas de evidência, parceiros, referências de nicho).
