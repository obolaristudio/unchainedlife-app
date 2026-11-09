---
name: video-effects
description: Catálogo de efeitos de edição profissional para vídeos do Maxwell. Use SEMPRE que for criar, editar, montar, legendar ou finalizar qualquer vídeo para ele — especialmente para postar no Instagram (Reels/Stories), e também TikTok/Shorts — escolhendo e aplicando os efeitos que melhor se encaixam no conteúdo.
---

# Efeitos de edição de vídeo (padrão profissional)

Origem: vídeo de referência "/effects" (Claude Code, 36 efeitos — 7 demonstrados).
O comando `/effects` do vídeo é uma skill de terceiros, não nativa. Aqui cada efeito
está descrito para ser reproduzido com ferramentas próprias:
- **ffmpeg** (corte, máscara, color grade, composição, legendas)
- **Overlays em HTML/CSS animado** renderizados frame a frame com Playwright (Chromium já instalado) e compostos com ffmpeg (`overlay`, alpha via PNG sequence ou WebM VP9)
- **Segmentação de pessoa** (ex.: `rembg` / MediaPipe Selfie Segmentation) quando o efeito exige recortar a pessoa do fundo
- Alternativas hospedadas: HyperFrames (HeyGen), Higgsfield, Canva

## Os 7 efeitos

| Comando | O que faz | Quando usar |
|---|---|---|
| `glass-widgets` | Cartões de vidro fosco (glassmorphism) flutuando ao redor da pessoa: números grandes, mini-gráficos, barra de "rendering", perfil, badge 4K. Visual de dashboard. | Falar de resultados, métricas, crescimento, ferramentas, SaaS, IA. |
| `documentary` | Vira reportagem: P&B com alto contraste, halo/círculo de cor (rosa/magenta) atrás da pessoa, título condensado grande ("ONE CLIP. 36 EFFECTS. ZERO APPS."), lower third com nome + @, kicker no topo ("A NON-TECHNICAL AI SERIES · DAILY"), botão "Follow" com cursor clicando. | Abertura/gancho, autoridade, storytelling, série de conteúdo. |
| `orbit` | Cards e prints de tela (posts, apps, notebooks) orbitando em 3D ao redor da pessoa, passando na frente e atrás dela (precisa máscara). | Mostrar portfólio, provas sociais, exemplos, "olha tudo que dá pra fazer". |
| `kallaway-split` | Tela dividida: metade de cima com gráfico animado (barras crescendo, linha de média, títulos tipo "My top 7 reels *by views*"), metade de baixo a pessoa em card arredondado. | Dados, comparações, rankings, antes/depois numérico. |
| `spotlight` | Fundo escurecido, pessoa iluminada por um foco de luz, texto neon (ex. "CLAUDIT") atrás da pessoa (texto com profundidade). | Frase de impacto, revelação, momento-chave, CTA forte. |
| `checklist` | Painel escuro translúcido "Claude is editing your clip — 1 of 5" com itens que vão sendo marcados (✓ verde) sincronizados com a fala, tags à direita em mono (every frame, AI mask, depth, warm, 2160p). | Passo a passo, processos, tutoriais, listas de benefícios. |
| `timeline` | Interface de software de edição (timeline com thumbnails, trilhas de legenda/grade/sfx, waveform, barra de progresso %) acima da pessoa, título "Claude *renders it*". | Bastidores, "como eu fiz", conteúdo sobre automação/IA/produtividade. |

Elementos de suporte vistos no vídeo: transição em grade de pontos/halftone entre cenas,
selo "Edited by Claude" em pílula de vidro, botão "Abonne-toi/Inscreva-se" vermelho no CTA final,
legenda-gancho em balão branco no topo nos primeiros segundos.

## Como escolher (regra de decisão)
1. **0–3 s (gancho):** `documentary` ou legenda-gancho + zoom leve. Nunca começar sem texto na tela.
2. **Corpo:** casar efeito com o tipo de fala — números → `kallaway-split`/`glass-widgets`; passos → `checklist`; exemplos/provas → `orbit`; processo → `timeline`.
3. **Ponto alto / frase-chave:** `spotlight`.
4. **Final:** CTA (seguir/inscrever/link) com botão animado.
5. Máximo 1 efeito pesado a cada ~4–6 s; entre eles, cortes secos + legenda. Não empilhar efeitos só por empilhar — cada um precisa reforçar o que está sendo dito.
6. Sempre adaptar os textos dos widgets ao conteúdo real do vídeo (dados, nome, @ do Maxwell), nunca deixar texto genérico de exemplo.

## Padrão de qualidade (todo vídeo)
- Destino padrão: Instagram Reels. Duração ideal 15–45 s; capa (thumbnail) com texto legível no grid 4:5 central; sugerir legenda do post + 3–5 hashtags junto com o vídeo.
- 1080×1920, 30 fps, H.264 alta qualidade (CRF ≤ 18), áudio AAC 192k, loudness ~-14 LUFS.
- Cortar pausas e respiros; legendas sincronizadas palavra a palavra (transcrever com faster-whisper), fonte sans bold, palavras-chave destacadas em cor.
- Color grade quente e consistente; manter rosto sempre em área segura (fora dos 15% inferiores e da lateral direita onde ficam botões do app).
- Antes de entregar: gerar contact sheet de frames e revisar visualmente; apontar ao Maxwell quais efeitos usei e por quê.
- Transições de zoom (pedido do Maxwell, padrão em todo vídeo): entrada de cena com zoom 1.22→1 + leve blur, punch-in de ~9% nas palavras de impacto, deriva lenta de zoom dentro da cena, whoosh bem baixo na troca de cena.
- Música de fundo sempre, bem baixinha: instrumental (ElevenLabs Music, conferir que não tem vocal), ~15 dB abaixo da voz, com ducking (sidechaincompress) e fade in/out.
- Entrega dupla: SendUserFile a partir de `videos/` no projeto + página Artifact privada com o vídeo embutido (data URI, < 16 MB) e a legenda com botão de copiar.
- Conteúdo de saúde: checar fatos antes de narrar; nunca gravar com a voz do Maxwell afirmações falsas ou que incentivem uso de substância não aprovada — propor versão corrigida (formato "mito ou verdade" funciona bem).
- Sempre disponibilizar o vídeo final no chat (SendUserFile, display render) para o Maxwell assistir e aprovar ANTES de qualquer publicação. Nunca publicar sem aprovação explícita.

## Regra nº 1: conta segura (prioridade acima de engajamento)
O Maxwell já perdeu uma conta com 14 mil seguidores por violar políticas sem saber. Todo vídeo, legenda, capa e hashtag passa por este checklist ANTES de ser entregue. Se algum item falhar, corrigir ou avisar — nunca entregar "para testar".

**Tom obrigatório:** ensino. Explicar o que é, como funciona, o que a ciência diz. Nunca prometer resultado (peso, músculo, cura, dinheiro, prazo).

**Bloqueia na hora (não produzir):**
- Instrução de dose, diluição, aplicação ou protocolo de medicamento/substância — principalmente injetável ou não aprovada pela Anvisa.
- Venda, preço, "onde comprar", "chama no direct", link de fornecedor de medicamento, peptídeo, hormônio, suplemento.
- Promessa de resultado ("perca X kg", "ganhe massa", "substitui hormônio", "cura").
- Antes/depois de corpo, foco em partes do corpo, ou conteúdo que faça a pessoa se sentir mal com o próprio corpo.
- Afirmações de saúde falsas ou sem fonte (checar fatos antes de narrar).
- Música, imagem, logo ou vídeo de terceiros sem direito de uso; reupload de vídeo de outro criador.
- Engajamento artificial: "comenta X que eu te mando", sorteio sem regras, pedir curtida em troca de algo.

**Cuidados (pode, com ajuste):**
- Citar nome de remédio (Ozempic, Mounjaro) só em contexto educativo/histórico, sem marca visual (logo/embalagem).
- Aviso fixo em conteúdo de saúde: "Conteúdo educativo. Fale com um médico." — na tela e na legenda.
- Hashtags: só educativas e do tema. Evitar tags de emagrecimento/estética/biohacking em conteúdo com remédio (público e moderação mais restritos); nunca hashtags banidas ou de spam; máx. ~10.
- Linguagem de alerta forte ("mata") só quando é fato educativo e com contexto.

**No relatório de entrega**, sempre incluir uma linha "Checagem de políticas: OK" ou listar o que foi ajustado.

## Identidade visual Obolari Academy (todo vídeo)
- Seguir **`brand/paleta.md`** à risca (cores exatas, estilo "caderno" creme com verde-limão, cards com borda preta e sombra dura, rótulos mono). Isso substitui o visual escuro/rosa/amarelo usado nos primeiros vídeos.
- **Assinatura discreta:** barra grafite do topo com "● OBOLARI ACADEMY" pequeno (fonte mono, ~24 px) + a série à direita ("PEPTÍDEOS · GHK-Cu"). Na tela final, pílula preta "@obolari_academy" em verde-limão, pequena.
- **Feed limpo:** mesma paleta e mesmo layout em todos os vídeos e capas, para o grid ficar uniforme.
- Legendas palavra a palavra: texto preto sobre faixa off-white com borda preta, palavra falada destacada em caixa verde-limão.

## Ferramentas de geração (pedido do Maxwell, nov/2026 — padrão em todo vídeo novo)
Objetivo: vídeos mais dinâmicos, com movimento real, e não só cards animados. Usar as três ferramentas em conjunto:

| Ferramenta | Conector | Papel no vídeo |
|---|---|---|
| **Higgsfield** | `mcp__higgsfield__*` | B-roll cinematográfico e cenas em movimento (texto→vídeo, imagem→vídeo), motion control, reframe 9:16, upscale. Antes de entregar, rodar `virality_predictor` no corte final. Para escolher o modelo, usar `models_explore` com `action:'recommend'`; para vídeos com várias etapas, chamar `get_workflow_instructions` primeiro. |
| **Buzzy AI** | `mcp__buzzy_ia__*` | Clipes de storyboard/história e cenas de produto. Fluxo: `load_workflow` (catálogo) → skill certa → `create_project` → `generate_image`/`generate_video`, com resolução, proporção e duração copiadas de `list_model` → `get_task` até concluir → `merge_videos`. |
| **Captions** | `mcp__Captions__*` | Legenda animada final no estilo do app Captions (`captions_list_caption_templates` → `captions_add_captions`). Exige conexão única em app.mcp.ai. Se não estiver conectado, usar as legendas próprias (whisper palavra a palavra) e avisar. |

**Montagem padrão:**
1. Narração com a voz do Maxwell: ElevenLabs "Maxwell Obolari", `voice_id OzlrOiSmF6F4M3mkabDT`, modelo `eleven_v4`.
2. Gancho de 0 a 3 s com B-roll forte (Higgsfield).
3. Corpo: B-roll de Higgsfield ou Buzzy a cada 3–5 s, intercalado com os cards da marca (dados, checklist, gráfico). Os dados continuam nos cards, porque os textos gerados por IA saem errados.
4. Legendas pelo Captions.
5. Música baixinha com ducking.
6. Identidade Obolari na barra do topo e na tela final.

**Custo:** as três cobram créditos. Antes de gerar, pedir a estimativa (estimate/quote), informar o total previsto ao Maxwell e não gerar variações extras sem pedir.

**Regra nº 1 também vale para imagens geradas:**
- Nada de corpo antes/depois nem de foco em partes do corpo.
- Nada de seringa, caneta ou aplicação de medicamento.
- Nada de embalagem ou logo de remédio.
- Avatar de IA não pode se passar por médico nem por paciente real.
- Pessoas geradas só em cenas neutras: cozinha, prato, caminhada, academia, exame de sangue genérico.

## Nome da marca (regra fixa, pedido do Maxwell em nov/2026)
Todo vídeo e material usa **"Obolari Academy"**: narração ("conteúdo educativo da Obolari Academy"), créditos na tela, aviso fixo, legenda do post, PDFs e documentos. **Nunca usar "Obolari Labs"**, para não confundir o público. Os vídeos de resistência à insulina e de amilina (nov/2026) ainda citam "Obolari Labs"; corrigir se o Maxwell pedir.

## Fechamento sem exagero (pedido do Maxwell, 06/11/2026)
No final do vídeo e da legenda: só "Conteúdo educativo" + "Converse com o seu médico" + a pergunta de engajamento. NÃO repetir "não é aprovado", "não pode ser usado", "não use" etc. O status regulatório, quando entrar, vai uma única vez, no corpo do vídeo, de forma neutra e curta (ex.: "a FDA aprovou para tal grupo"). As travas da Regra nº 1 continuam (sem dose, compra, promessa).

## Padrão de produção (pedido do Maxwell, 06/11/2026 — vale para todo vídeo)
- **Estrutura do viral:** sempre identificar a estrutura que fez o viral funcionar (tipo de gancho, ordem dos blocos, ritmo, virada, CTA) e reconstruir o vídeo com ESSA estrutura. Roteiro, imagens e áudio são sempre originais (nunca copiar fala, vídeo ou imagem do criador).
- **Camadas obrigatórias:** cenas em movimento (Higgsfield/Buzzy) + imagens de banco livre (Openverse com licença CC0/PDM: `https://api.openverse.org/v1/images/?q=<termo>&license=cc0,pdm`; registrar a fonte) + cards da marca + transições com zoom + efeitos sonoros + música baixinha + legenda palavra a palavra.
- **Kit de efeitos sonoros** em `brand/sfx/` (ElevenLabs): `impact.mp3` no gancho, `whoosh.mp3` em cada troca de cena, `pop.mp3` quando um card aparece, `ding.mp3` em checklist/dado-chave. Script de mixagem de referência: aplicar com volumes ~0,2–0,55 abaixo da voz.
- **NUNCA repetir vídeo ou imagem** (pedido do Maxwell, 07/11/2026): cada Reel usa clipes e imagens inéditos, gerados para ele. Antes de usar um clipe, conferir em `research/clipes-usados.md`; depois de publicar, registrar ali os arquivos/IDs usados.
- **Ritmo:** cenas de ~3,5 s em velocidade normal; nada de acelerar os clipes (o formato "acelerado" ficou rápido demais).
- **Banco de ganchos:** antes de escrever qualquer roteiro, escolher o gancho em `ganchos.md` (40 ganchos por gatilho psicológico, adaptados ao nicho) e registrar lá qual funcionou.
- **Galeria de efeitos virais (obrigatória em todo Reel):** ler `.claude/skills/efeitos-virais/SKILL.md` e escolher 2 a 4 dos 20 efeitos conforme as falas do roteiro (número → Snap Zoom/Growth Curve, lista → Checklist Pop, mito → Frame Break, estudo → Magazine Cover, recapitulação → Checklist).
- **Skills de som instaladas (usar em todo vídeo):**
  1. **real-sfx** (`.claude/skills/real-sfx`): sons gravados reais. Fluxo: cue sheet a partir da timeline JSON do vídeo → `from_cues.py` → `mix.py` → `critique.py`. Bibliotecas: `brand/sfx-cc0` (main), `brand/sfx` (extra) e uisfx (1.895 cues CC0; packs `cinematic`, `glass`, `soft`, `minimal`…).
  2. **earshot** (CLI `earshot`): antes de usar qualquer som novo, `earshot describe arquivo` / `earshot match arquivo "descrição"`; no final, `earshot timeline video.mp4` para conferir sync e loudness. Banco próprio: `earshot sfx list` / `earshot sfx render <id>`.
  3. **real-sound**: referência de mixagem/master (-14 LUFS, -1 dBTP) e créditos.
  - Entregar sempre: MP4, WAV só dos SFX, cue sheet e créditos (`brand/sfx-cc0/CREDITOS.csv`).
  - Container novo? Reinstalar: `pip install scipy soundfile soxr librosa pyloudnorm scikit-learn pillow matplotlib transformers && pip install torch --index-url https://download.pytorch.org/whl/cpu && git clone https://github.com/Leonxlnx/earshot /tmp/earshot && pip install --no-deps /tmp/earshot`.
- **Retenção:** algo visual novo a cada 2–4 s; padrões que prendem: pergunta no 1º segundo, "mito ou verdade", número grande na tela, checklist, contraste lado a lado, veredito final.
- **CTA de comentário em todo vídeo e legenda** (pergunta aberta, ex.: "Qual peptídeo eu explico no próximo? Comenta aqui"), nunca palavra-chave em troca de algo.
- **Captions:** o conector só legenda vídeos gerados dentro dele (sem upload de vídeo externo); usar quando houver vídeo de avatar/Mirage, senão legenda própria.
- **Créditos:** antes de cada produção checar saldo (Higgsfield `balance`; ElevenLabs pelo custo das gerações) e avisar o Maxwell quando qualquer ferramenta estiver acabando (Higgsfield < 150 créditos, ou qualquer erro de saldo em ElevenLabs, Buzzy ou Captions).

## Referências de perfis
Antes de planejar série, gancho, capa, bio ou destaques, ler `referencias.md` desta pasta (perfis analisados e como aplicar).

## Aviso final obrigatório (pedido do Maxwell, 06/11/2026 — substitui o fechamento anterior)
Todo vídeo, legenda, PDF e material termina com um aviso curto de que **não é recomendação médica nem sugestão de uso**. Tom calmo, uma frase só, sem dramatizar e sem "não é aprovado / não use".
- Vídeo (tela final + narração): "Conteúdo educativo. Não é recomendação médica nem sugestão de uso."
- Legenda: "⚠️ Conteúdo educativo: não é recomendação médica nem sugestão de uso. Converse com o seu médico."
- PDF/material: rodapé em todas as páginas com a mesma frase.
- Ajustar o tom ao perfil/público em que o conteúdo for publicado (ver ajustes de perfil que o Maxwell enviar), mantendo sempre o sentido "não é recomendação médica nem sugestão de uso".

## Perfil
Padrão de bio, nome, capa e grid em `perfil-obolari.md` desta pasta.

## Operação 24 h
Missão, linha editorial, formatos, orçamento de créditos e divisão das tarefas em `operacao-24h.md` desta pasta.

## Regra do Maxwell (08/11/2026): vídeos de receita gravados por ele
- Manter o vídeo ORIGINAL contínuo (sem cortes, sem acelerar, sem zoom/desfoque nas trocas).
- Nome de cada item AO LADO do item: etiqueta lime + linha fina + ponto no item, aparecendo quando ele mostra o ingrediente.
- NÃO usar "texto atrás dos objetos" com recorte por cor/IA em vídeo de cozinha: falha (vidro, mãos) e ele reprovou.
- Modelo pronto: videos/cha-roma/gen2.py.

## Regra do Maxwell (09/11/2026): imagens REAIS, não "cara de IA"
- Para notícia/estudo: preferir vídeos reais de banco (Mixkit: assets.mixkit.co/videos/<id>/<id>-720.mp4, licença livre; Wikimedia Commons). Pexels/Pixabay pedem chave de API.
- Clipes horizontais: painel central nítido (1080x1100, y=420) + mesmo clipe desfocado ao fundo; título em cima, legenda sincronizada embaixo. Modelo: videos/vrx-0075/ (scenes.py + gen.py).
- Nunca usar clipe com seringa/frasco aplicando (Regra nº 1).
