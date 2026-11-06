# Operação 24 h — @obolari_academy (missão do Maxwell, 06/11/2026)

Objetivo: transformar o perfil numa máquina de crescer seguidores com conteúdo de qualidade sobre **peptídeos, longevidade, vitaminas e bem-estar**, sempre educativo e baseado em evidência. Esta é a ordem de prioridade quando houver conflito: **Regra nº 1 (conta segura) > qualidade/fato correto > volume**.

## Quem faz o quê (tarefas agendadas)
| Tarefa | Quando | O que faz |
|---|---|---|
| Rotina Madrugada Peptídeos | todo dia ~04:47 BRT | pesquisa virais + notícias/estudos da semana → produz **2 Reels + 1 carrossel** → fila de publicação |
| Respostas comentários Instagram | de hora em hora (08:00–23:59 BRT) | publica o que está na fila no horário, responde comentários, avisa casos sensíveis |
| Revisão semanal de crescimento | segunda ~08:47 BRT | lê métricas, ranqueia posts, ajusta temas/horários/ganchos e manda relatório |

## Linha editorial (mix semanal)
- **40 % peptídeos** (seguir as regras de alcance de `perfil-obolari.md`) (série "um peptídeo por vídeo", mito × verdade, comparativos).
- **35 % longevidade** (sono, músculo e envelhecimento, VO2máx, glicose/insulina, inflamação, jejum — sempre com o que a ciência mostra).
- **25 % vitaminas e bem-estar** (vitamina D, magnésio, ômega-3, creatina, B12, colágeno, probióticos — o que é, para que serve segundo estudos, quem costuma ter deficiência, quando falar com o médico). **Sem dose individual**: no máximo citar a recomendação oficial de ingestão diária (RDA/ANVISA) quando for o ponto do vídeo.
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

## Antena ligada: notícias, GitHub e ferramentas (pedido do Maxwell, 06/11/2026)
- **Todo dia (rotina da madrugada):** varrer o que saiu sobre peptídeos, longevidade, vitaminas e bem-estar — estudos novos (PubMed), decisões FDA/Anvisa/EMA, notícias confiáveis e virais — e usar no conteúdo do dia. Novidade grande (aprovação, estudo de fase 3, alerta de segurança) = prioridade de pauta.
- **Todo domingo (rotina da madrugada):** varrer o GitHub (`gh api -X GET search/repositories`, ordenar por estrelas, só repositórios ativos nos últimos 6 meses) e a web por repositórios e ferramentas que melhorem a operação (edição de vídeo, legendas, pesquisa científica, automação de Instagram, análise de métricas). Registrar tudo em `research/ferramentas.md`.
- **Pode instalar repositório** quando agregar, com estas travas de segurança: licença compatível (MIT/Apache/BSD etc.); projeto mantido e com reputação (estrelas, contribuidores); **ler o código antes de rodar**; instalar em pasta separada; versão fixa (commit/tag); nunca dar senhas, tokens ou acesso à conta do Instagram a código de terceiros; nada que automatize seguir/deixar de seguir, curtir em massa ou burlar o Instagram. Registrar em `research/ferramentas.md` como `instalado`.
- **Ferramenta paga ou que exige cadastro:** não assinar. Avisar o Maxwell com nome, link, para que serve, preço e o ganho esperado; ele faz a assinatura. Registrar como `sugerido ao Maxwell`.
