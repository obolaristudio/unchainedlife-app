# Rotina da madrugada: pesquisa → 2 vídeos originais → publicação automática

Pedido do Maxwell. Roda todo dia de madrugada (America/Sao_Paulo) por tarefa agendada, sem ninguém acompanhando.
Modo escolhido pelo Maxwell: **100% automático, 2 vídeos por dia**. Seguir também o SKILL.md desta pasta.
A "Regra nº 1: conta segura" do SKILL.md é trava obrigatória: vídeo que falhar em qualquer item NÃO é publicado.

0. **Idiomas (preferência do Maxwell):** priorizar criadores em **inglês** (e espanhol) com conteúdo baseado em evidência, porque costumam ter afirmações mais precisas e com fonte. Usar criadores brasileiros só como termômetro do que está em alta aqui. Transcrever no idioma original, traduzir para o português e adaptar à linguagem do público brasileiro (não traduzir literalmente). Checar cada número/afirmação na fonte citada (estudo, FDA, EMA) antes de usar. **Público duplo (Brasil + Estados Unidos):** todo vídeo que citar substância, peptídeo ou remédio deve trazer o status regulatório **nos dois países — FDA (EUA) e Anvisa (Brasil)** — na narração ou na tela, de forma clara e curta (ex.: "Nos EUA, a FDA… No Brasil, a Anvisa…"). Checar a posição atual de cada agência no dia (fontes oficiais: fda.gov e gov.br/anvisa) e nunca supor que o status é igual nos dois países. Na legenda do post, repetir o status das duas agências em uma linha.
**Formato fixo (pedido do Maxwell): série educativa "um peptídeo por vídeo".** Cada vídeo explica UM peptídeo, só para esclarecer. Estrutura (45–60 s):
   1. Gancho: o nome do peptídeo + a dúvida/mito mais comum sobre ele (vinda da pesquisa de virais).
   2. O que é (em linguagem simples).
   3. Como age no corpo (mecanismo, sem exagero).
   4. O que a ciência mostra de fato — separar estudo em humanos x em animais/laboratório, e dizer o tamanho/qualidade da evidência.
   5. Status regulatório: FDA (EUA) e Anvisa (Brasil).
   6. O que ainda não se sabe / riscos conhecidos.
   7. Fechamento: "Conteúdo educativo. Fale com um médico." + "Qual peptídeo você quer que eu explique no próximo?"
   Proibido: dose, protocolo, onde comprar, promessa de resultado, antes/depois. Fila e histórico da série em `research/peptideos.md` (não repetir peptídeo já explicado; priorizar o que está em alta na pesquisa de virais). Os 2 vídeos do dia são 2 peptídeos diferentes.
1. **Pesquisa de virais (tema: peptídeos).** Serve para descobrir QUAIS peptídeos estão em alta e quais dúvidas/mitos o público tem — não para copiar o tema do vídeo. Lista de criadores: `research/criadores.md` + novos achados por WebSearch. Para cada criador: `gpt_social.analyze_creator(instagram, username)` → `get_analysis_status` → `list_creator_videos`; ranquear vídeos dos últimos 30 dias por visualizações/engajamento. Escolher os **3 mais virais** sobre peptídeos ainda não usados (`research/usados.md`). Fallback: yt-dlp (pausas se der 429) + faster-whisper.
2. **Transcrever os 3** e extrair gancho, estrutura, tema e afirmações. Nunca reutilizar imagem, áudio ou texto deles: só referência.
3. **2 roteiros originais** no formato fixo acima, tom de ensino. Checar cada afirmação de saúde em fontes confiáveis (FDA, Anvisa, PubMed). Se o viral espalha mito, preferir "mito ou verdade" corrigindo. Sem dose, sem venda, sem promessa.
4. **Produção** conforme SKILL.md: voz "Maxwell Obolari" (ElevenLabs, voice_id OzlrOiSmF6F4M3mkabDT, eleven_v4); música instrumental baixinha com ducking; transições de zoom; gráficos/ícones próprios; legenda palavra a palavra; aviso "Conteúdo educativo. Fale com um médico." na tela final; capa. Revisar contact sheet.
5. **Checagem de políticas** item a item. Falhou → não publicar e registrar o motivo.
6. **Horários:** ler `online_followers` das insights (Composio, toolkit instagram, conta obolari_academy) e escolher 2 picos. Considerar que parte do público está nos EUA (fuso de Nova York, 1–2 h atrás de Brasília): se as insights mostrarem picos separados, escolher um horário que pegue os dois países. Sem dados: 12:10 e 19:40 (Brasília). Mínimo 4 h entre os dois.
7. **Hospedagem:** commit do MP4 e da capa no ramo `media` e usar `https://cdn.jsdelivr.net/gh/obolaristudio/unchainedlife-app@<commit>/<arquivo>` (confirmar `content-type: video/mp4`).
8. **Agendar:** `send_later` na própria sessão em cada horário. Ao disparar: INSTAGRAM_CREATE_MEDIA_CONTAINER (reel, share_to_feed=true, video_url, cover_url, caption) → INSTAGRAM_GET_POST_STATUS até FINISHED → INSTAGRAM_CREATE_POST → INSTAGRAM_GET_IG_MEDIA (permalink).
9. **Relatório da manhã:** os 3 virais (link + por que viralizaram), os 2 vídeos, horários, "Checagem de políticas: OK" ou o que foi bloqueado, créditos gastos. Depois de publicar, o link de cada post. Registrar os virais em `research/usados.md`.
10. Se algo travar (Instagram desconectado, créditos, download), não inventar resultado: parar aquele vídeo e explicar o que o Maxwell precisa fazer.
