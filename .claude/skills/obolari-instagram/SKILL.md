---
name: obolari-instagram
description: Manual-mestre da Operação 24 h do Instagram @obolari_academy (Maxwell Obolari). Use SEMPRE que o Maxwell pedir qualquer coisa do Instagram dele — criar/postar Reels ou carrosséis, pesquisar virais, analisar perfis, responder comentários, legendas, bio, crescimento de seguidores, guia/PDF, automação de DM, créditos das ferramentas — ou quando uma tarefa agendada da operação rodar. Diz o que fazer, em que ordem, com quais ferramentas e onde estão as regras detalhadas.
---

# Operação 24 h — @obolari_academy

**Missão (pedido do Maxwell, 06/11/2026):** assumir o Instagram e transformá-lo numa máquina de ganhar seguidores, com conteúdo de qualidade sobre **peptídeos, longevidade, vitaminas e bem-estar**. Prioridade em conflito: **conta segura > fato correto > qualidade > volume**.

## 1. Antes de qualquer coisa, leia (pasta `.claude/skills/video-effects/`)
| Arquivo | Para quê |
|---|---|
| `SKILL.md` | Regra nº 1 (conta segura), padrão de edição, aviso final, fechamento, padrão de produção, ferramentas |
| `operacao-24h.md` | Linha editorial, formatos, orçamento de créditos, divisão das tarefas |
| `rotina-madrugada.md` | Passo a passo da produção diária (pesquisa → 2 Reels + 1 carrossel → fila) |
| `respostas-comentarios.md` | Publicação da fila, respostas a comentários, revisão semanal |
| `referencias.md` | Perfis analisados (ex.: @anacapozzoli) e como aplicar |
| `perfil-obolari.md` | Bio, nome, @, capas, grid, destaques |
| `/brand/paleta.md` | Identidade visual (cores, fontes, música) |

## 2. Regras que nunca mudam (resumo)
1. **Conta segura:** sem dose, protocolo, aplicação, compra/venda, promessa de resultado, antes/depois, conteúdo de terceiros. O Maxwell já perdeu uma conta de 14 mil seguidores.
2. **Fatos checados** em fonte primária (FDA, Anvisa, PubMed, NEJM etc.) antes de narrar. Nunca afirmar algo sem fonte com a voz dele; propor versão corrigida.
3. **Viral = estrutura, não cópia:** reaproveitar gancho, ordem e ritmo. Roteiro, imagem e áudio sempre originais.
4. **Aviso final obrigatório** (uma frase, tom calmo): "Conteúdo educativo. Não é recomendação médica nem sugestão de uso." Sem repetir "não é aprovado, não use".
5. **Marca:** sempre "Obolari Academy" (nunca "Obolari Labs"). @ = obolari_academy.
6. **Sempre pedir para comentar** (pergunta aberta). "Comente PALAVRA" só com material próprio aprovado pelo Maxwell.
7. **Mínimo 4 h entre posts**; horários de pico padrão 12:10 e 20:10 no horário de Nova York (ET), escolhidos para pegar EUA + Brasil; o Maxwell mora nos EUA (fuso Leste). Revisados semanalmente.
8. **Visual:** pode variar um pouco, mas na mesma paleta e sequência (sem poluição). Em todo vídeo, usar cores de atenção animadas no meio — principalmente **vermelho** em palavra/número/seta/círculo — seguindo `/brand/paleta.md` (seção "Evolução visual").
9. **Créditos:** avisar o Maxwell quando Higgsfield < 150 ou houver erro de saldo em ElevenLabs/Buzzy/Captions.

## 2.1 Antena ligada
Notícias e estudos todo dia; GitHub e novas ferramentas todo domingo. Pode instalar repositório que agregue (com as travas de segurança de `operacao-24h.md`); ferramenta paga/cadastro → avisar o Maxwell. Registro em `research/ferramentas.md`.

## 3. Ferramentas e IDs
| Uso | Ferramenta | Detalhe |
|---|---|---|
| Voz do Maxwell | ElevenLabs | voice "Maxwell Obolari", `voice_id OzlrOiSmF6F4M3mkabDT`, modelo `eleven_v4`; nas rotinas, 1 versão |
| Efeitos sonoros | arquivos | `brand/sfx/` (impact, whoosh, pop, ding) |
| Cenas em movimento | Higgsfield (`kling3_0` std, 9:16, 5 s, sem som ≈ 6 créditos) e Buzzy AI (`Seedance 2.5` / `Kling 3.0`, 720p) | reaproveitar biblioteca de clipes antes de gerar |
| Imagens livres | Openverse | `https://api.openverse.org/v1/images/?q=<termo>&license=cc0,pdm` |
| Legendas | próprias (whisper palavra a palavra) | Captions só legenda vídeos gerados dentro dele |
| Pesquisa de virais | gpt_social (`analyze_creator`, `analyze_post`, `list_creator_videos`), yt-dlp + faster-whisper, WebSearch | |
| Publicar / comentários / DM | Composio, toolkit `instagram`, conta `obolari_academy`, `ig_user_id 28819342257765111` | Reels: `INSTAGRAM_POST_IG_USER_MEDIA` (REELS) → `INSTAGRAM_POST_IG_USER_MEDIA_PUBLISH` → `INSTAGRAM_GET_IG_MEDIA` (permalink e conferir legenda). Mensagens: a conexão tem permissão de DM |
| Hospedar mídia pública | Buzzy `upload_file` + `confirm_file_upload` (res-prod.buzzy.now) ou jsDelivr do ramo `media` | |
| Fila de publicação | `fila.json` no ramo `media` | itens `pendente` → `publicado` com permalink |
| Drive | Google Drive | PDFs do Maxwell (ver pendências) |

## 4. Fluxo de um conteúdo (Reel)
1. Pesquisar viral/estudo → anotar estrutura e fatos com fonte.
2. Roteiro original 45–70 s: gancho forte no 1º segundo → explicação → dado/estudo → pontos de atenção → aviso final → pergunta para comentar.
3. Narração (ElevenLabs) → tirar pausas (`silenceremove`, atempo ~1.07) → transcrever (faster-whisper) → alinhar com o roteiro.
4. Cenas (Higgsfield/Buzzy/CC0) + cards da marca (HTML → PNG com Playwright) + zoom/transições + SFX + música baixinha com ducking + legenda palavra a palavra; -14 LUFS, 1080×1920.
5. Revisar quadros (contact sheet) e checagem de políticas.
6. Capa limpa (título no topo, palavra em verde-limão, selo "PEPTÍDEOS · EP. N") e legenda do post (estrutura em `referencias.md`, aviso, pergunta, até 5 hashtags do tema, sem tags de emagrecimento em post com remédio).
7. Hospedar, colocar na `fila.json` com horário de pico e mandar o arquivo ao Maxwell (SendUserFile). Ele não precisa aprovar, mas sempre recebe.
8. Depois de publicado: conferir legenda e mandar o link.

## 5. Tarefas agendadas
| Tarefa | Quando | Observação |
|---|---|---|
| Rotina Madrugada Peptídeos | diário ~04:47 BRT | criada fora daqui; o texto dela ainda cita send_later (não existe em sessão agendada) — vale a regra dos arquivos: usar a fila |
| Respostas comentários Instagram | de hora em hora, 08:00–23:59 | publica a fila, responde comentários, revisão semanal às segundas |
| "Revisão semanal de crescimento" (avulsa) | desativada | ficou sem conector; revisão foi para a rotina de hora em hora |

## 6. O que só o Maxwell pode fazer
- Editar bio, nome e @ (a API não permite). Texto pronto em `perfil-obolari.md`.
- Deixar de seguir: manual, 50–100/dia em Seguindo → "Menos interagidos", até ficar ~50 perfis relevantes. Nunca automatizar.
- Aprovar gastos grandes e liberar o formato "comente PALAVRA".

## 6.1 Loja e materiais (Gumroad)
- Plataforma de hospedagem e venda: **Gumroad** (conectado na Composio; a API não cria produtos — o Maxwell cria pelo app/site com os pacotes em `materiais/gumroad/`).
- Loja: hoje `2913514266881.gumroad.com` → trocar usuário para **obolariacademy** e ligar o domínio **obolariacademy.com** (registrado na GoDaddy em 06/11/2026, 3 anos, renovação automática) como domínio personalizado.
- Guia grátis = produto US$ 0+ em `/l/guia` (captura e-mail). Quando estiver no ar, trocar o link da automação "GUIA" (respostas-comentarios.md) e da bio.
- Gumroad também serve de página de venda do material pago; site próprio só se precisar de página longa.

## 7. Pendências (atualizar esta lista)
- [x] Guia em PDF original (`materiais/Guia-dos-Peptideos-Obolari-Academy.pdf`, link público em `respostas-comentarios.md`) + automação "comente GUIA" ativa na rotina de hora em hora. **Nunca** usar o "Peptide pdf ebook.pdf" do Drive (licença de terceiro, com doses).
- [ ] Usar "comente GUIA" nos próximos vídeos/legendas; trocar a última linha da bio quando o Maxwell atualizar.
- [ ] Maxwell: criar o produto grátis no Gumroad com `materiais/gumroad/`, trocar usuário da loja, ligar obolariacademy.com ao Gumroad (DNS na GoDaddy) e criar e-mail contato@obolariacademy.com.
- [ ] Capas dos destaques (Comece aqui, Peptídeos A–Z, Mito ou verdade, Perguntas, Guia grátis).
- [ ] Arquivar a Amilina repetida de menor alcance.
- [ ] Maxwell colar a bio/nome novos e começar o "deixar de seguir".

## Efeitos e som (desde 06/11/2026)
- Vídeo do Maxwell falando para a câmera: skill `video-falando` (palavra atrás da cabeça, legendas no quadro exato, camadas 3D).
- Efeitos visuais: skill `efeitos-virais` (20 efeitos HyperFrames, 2 a 4 por Reel).
- Som: skills `real-sfx` + `earshot` (ver video-effects).
- Horários de pico no fuso de Nova York (12:10 e 20:10 ET).

## Espelhar no YouTube Shorts (pedido do Maxwell em 06/11/2026)
- Todo Reel publicado no Instagram também vai para o YouTube como Short (Composio, toolkit youtube, `YOUTUBE_MULTIPART_UPLOAD_VIDEO`, privacyStatus public, categoryId 27 Educação). Título até 100 caracteres com #Shorts; descrição = legenda do Instagram adaptada ("comente GUIA" vira "link do guia no perfil"), com o aviso médico.
- **Conta correta:** `youtube_lipan-coco` (conectada pelo Maxwell em 07/11 para o canal Obolari Academy; confirmar o nome do canal no primeiro uso; `youtube_gane-teeth` não tem canal). NUNCA usar `youtube_tapis-toyer` (canal OliBari Kids, infantil). A `youtube_gane-teeth` deu "quotaExceeded" ao listar o canal em 06/11; confirmar com `YOUTUBE_LIST_CHANNELS mine=true` que é o canal da Obolari Academy antes do primeiro upload.
- Upload só uma vez por vídeo (reexecutar cria vídeo duplicado); guardar o videoId na fila.json (`youtube_id`).
