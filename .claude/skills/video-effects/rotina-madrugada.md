# Rotina da madrugada: pesquisa → 2 vídeos originais → publicação automática

Pedido do Maxwell. Roda todo dia de madrugada (America/Sao_Paulo) por tarefa agendada, sem ninguém acompanhando.
Modo escolhido pelo Maxwell: **100% automático, 2 vídeos por dia**. Seguir também o SKILL.md desta pasta.
A "Regra nº 1: conta segura" do SKILL.md é trava obrigatória: vídeo que falhar em qualquer item NÃO é publicado.

1. **Pesquisa de virais (tema: peptídeos).** Lista de criadores: `research/criadores.md` + novos achados por WebSearch. Para cada criador: `gpt_social.analyze_creator(instagram, username)` → `get_analysis_status` → `list_creator_videos`; ranquear vídeos dos últimos 30 dias por visualizações/engajamento. Escolher os **3 mais virais** sobre peptídeos ainda não usados (`research/usados.md`). Fallback: yt-dlp (pausas se der 429) + faster-whisper.
2. **Transcrever os 3** e extrair gancho, estrutura, tema e afirmações. Nunca reutilizar imagem, áudio ou texto deles: só referência.
3. **2 roteiros originais**, 45–60 s, tom de ensino. Checar cada afirmação de saúde em fontes confiáveis (FDA, Anvisa, PubMed). Se o viral espalha mito, preferir "mito ou verdade" corrigindo. Sem dose, sem venda, sem promessa.
4. **Produção** conforme SKILL.md: voz "Maxwell Obolari" (ElevenLabs, voice_id OzlrOiSmF6F4M3mkabDT, eleven_v4); música instrumental baixinha com ducking; transições de zoom; gráficos/ícones próprios; legenda palavra a palavra; aviso "Conteúdo educativo. Fale com um médico." na tela final; capa. Revisar contact sheet.
5. **Checagem de políticas** item a item. Falhou → não publicar e registrar o motivo.
6. **Horários:** ler `online_followers` das insights (Composio, toolkit instagram, conta obolari_academy) e escolher 2 picos. Sem dados: 12:10 e 19:40 (Brasília). Mínimo 4 h entre os dois.
7. **Hospedagem:** commit do MP4 e da capa no ramo `media` e usar `https://cdn.jsdelivr.net/gh/obolaristudio/unchainedlife-app@<commit>/<arquivo>` (confirmar `content-type: video/mp4`).
8. **Agendar:** `send_later` na própria sessão em cada horário. Ao disparar: INSTAGRAM_CREATE_MEDIA_CONTAINER (reel, share_to_feed=true, video_url, cover_url, caption) → INSTAGRAM_GET_POST_STATUS até FINISHED → INSTAGRAM_CREATE_POST → INSTAGRAM_GET_IG_MEDIA (permalink).
9. **Relatório da manhã:** os 3 virais (link + por que viralizaram), os 2 vídeos, horários, "Checagem de políticas: OK" ou o que foi bloqueado, créditos gastos. Depois de publicar, o link de cada post. Registrar os virais em `research/usados.md`.
10. Se algo travar (Instagram desconectado, créditos, download), não inventar resultado: parar aquele vídeo e explicar o que o Maxwell precisa fazer.
