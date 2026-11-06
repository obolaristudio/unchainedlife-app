# Respostas automáticas a comentários (@obolari_academy)

Pedido do Maxwell: responder os comentários dos posts por ele. Roda por tarefa agendada várias vezes ao dia. A "Regra nº 1: conta segura" do SKILL.md vale aqui também.

## Horário de silêncio (economia)
A tarefa roda de hora em hora. Se a hora atual em America/Sao_Paulo estiver entre **00:00 e 07:59**, encerrar imediatamente sem fazer nada e sem relatório. Fora desse horário, se não houver vídeo para publicar, nem comentário novo, nem caso para o Maxwell, encerrar com resposta mínima ("Nada novo.") sem enviar arquivos.

## Publicar vídeos da fila (fazer ANTES dos comentários, em toda execução)
1. `git fetch origin media` e ler `fila.json` do ramo `media`.
2. Para cada item com `status: "pendente"` cujo `publicar_apos` (America/Sao_Paulo) já passou: criar o Reel pela Composio (`INSTAGRAM_POST_IG_USER_MEDIA` com media_type REELS, video_url, cover_url, caption, share_to_feed=true) → aguardar status FINISHED → publicar (`INSTAGRAM_POST_IG_USER_MEDIA_PUBLISH`) → pegar o permalink.
3. No máximo 1 publicação por execução e nunca 2 posts com menos de 4 h de intervalo.
4. Marcar o item como `"status": "publicado", "permalink": "..."` no `fila.json`, commit/push no ramo `media`, registrar em `research/peptideos.md` (main) e mandar o link do post ao Maxwell.
5. Se falhar, marcar `"status": "erro"` com o motivo e avisar o Maxwell. Não tentar de novo no mesmo item sem ele.


## Revisão semanal de crescimento (segunda-feira, primeira execução depois das 08:00 BRT)
Antes dos comentários, uma vez por semana (checar em `research/revisoes.md` se a revisão desta semana já foi feita):
1. INSTAGRAM_GET_USER_INSIGHTS (últimos 7 dias): seguidores, alcance, views, visitas ao perfil, interações; e INSTAGRAM_GET_IG_MEDIA_INSIGHTS de cada post da semana (views, reach, saves, shares, comments).
2. Ranquear os posts e identificar o que funcionou (tema, gancho, formato, horário, duração). Usar online_followers, se vier, para revisar os horários de pico.
3. Atualizar `operacao-24h.md` com os ajustes (temas a repetir/evitar, ganchos vencedores, horários) e registrar a data em `research/revisoes.md`; commit/push no main.
4. Relatório curto ao Maxwell: crescimento da semana, top 3 posts com motivo, 3 ajustes aplicados, no máximo 2 decisões para ele, saldo do Higgsfield e alerta de créditos. Nunca inventar números.

## Como rodar
1. Composio, toolkit `instagram`, conta `obolari_academy` (ig_user_id 28819342257765111). Se a conexão não estiver ACTIVE, parar e avisar o Maxwell.
2. `INSTAGRAM_GET_IG_USER_MEDIA` (me) → posts dos últimos 14 dias.
3. Para cada post: `INSTAGRAM_GET_IG_MEDIA_COMMENTS`; para cada comentário de outra pessoa, ver com `INSTAGRAM_GET_IG_COMMENT_REPLIES` se @obolari_academy já respondeu. Já respondido → pular.
4. Responder com `INSTAGRAM_POST_IG_COMMENT_REPLIES` (máx. 300 caracteres, sem só maiúsculas, no máx. 1 emoji, sem links e sem hashtags).
5. Limite de **30 respostas por execução**, com ~20 s entre uma e outra. Variar as palavras: nunca a mesma frase pronta repetida (o Instagram trata como spam).

## Tom
Português do Brasil, simpático, curto, educativo — como o Maxwell falaria. Tratar a pessoa pelo @ quando natural. Agradecer elogios de forma variada.

## Pode responder
- Dúvida sobre o que é um peptídeo, como age, o que os estudos mostram → resposta curta e correta; quando citar substância, dizer o status FDA (EUA) e Anvisa (Brasil). Se não tiver certeza do fato, não inventar: "Boa pergunta, vou trazer isso num próximo vídeo."
- Sugestão de peptídeo para o próximo vídeo → agradecer e acrescentar o nome no topo da fila em `research/peptideos.md` (commit no main).
- Elogio / "salvei" / marcação de amigo → agradecer.

## Nunca responder com
Dose, diluição, protocolo, frequência, "quanto usar", onde comprar, preço, fornecedor, link, "me chama no direct", diagnóstico ou orientação individual, promessa de resultado. Para perguntas desse tipo, responder com variações de:
> "Isso precisa ser avaliado individualmente por um médico que acompanhe você. Aqui eu trago só o lado educativo 🙏"

## Não responder (só registrar no resumo)
- Spam, bots, golpes, links suspeitos, propaganda de terceiros.
- Ofensas, provocação, ataque pessoal, política/religião. Não discutir.

## Avisar o Maxwell (não responder sozinho)
- Relato de efeito colateral grave ou emergência → responder apenas: "Procure atendimento médico imediatamente." e avisar o Maxwell na hora.
- Ameaça jurídica, denúncia, imprensa, pedido de parceria/comercial, crítica séria de profissional de saúde.

## Relatório
Ao fim de cada execução: quantos comentários lidos, quantos respondidos, quais foram ignorados (e por quê) e os casos para o Maxwell. Se houver caso para o Maxwell, enviar com destaque; se não houver nada novo, relatório de 1 linha.
