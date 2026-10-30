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
- Link no chat (pedido do Maxwell, todo pedido de vídeo): ao terminar, escrever o link do vídeo na resposta final do chat, clicável. Vale para a página Artifact e para qualquer link gerado por ferramenta externa (Higgsfield, HyperFrames, ElevenLabs, Canva etc.). Se houver mais de um, listar todos com uma linha dizendo o que é cada um.
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
