---
name: efeitos-virais
description: Galeria dos 20 efeitos de vídeo virais (prompt pack "20 AI Video Effects", de David Roberts, feito em HyperFrames + GSAP) adaptada para os Reels da Obolari Academy. Use SEMPRE que for criar ou editar um vídeo do Maxwell, junto com video-effects, para escolher 2 a 4 efeitos de destaque que combinem com as falas do roteiro (número, lista, revelação, mito, estudo, app). Diz qual efeito usar em qual tipo de frase, a janela de tempo, se precisa recortar a pessoa, e traz o prompt de construção de cada um.
---

# Galeria de efeitos virais (20 efeitos)

Fonte: "20 AI Video Effects: the prompt pack", de David Roberts (@davi.d_roberts), uso livre nos próprios vídeos.
Doc original: https://docs.google.com/document/d/1zXh7Vit_cF0gxdp-BstDUwQoHHSijxnZHA5arEdjL04
Templates (zip `20-ai-video-effects.zip`): https://drive.google.com/drive/folders/1CVhyDTQRG7_sjCPmWWsE48CPlEMIgywn.
Ainda não importados: quando estiverem em `vendor/fx/`, use `node fx.mjs list|prepare|render|splice` como no README do pack.

Prompts completos ("com template" e "do zero") de cada efeito: `prompts.md`, nesta pasta.

## Regras de uso (Obolari)
1. **2 a 4 efeitos por Reel**, cada um numa fala que pede o efeito. Nunca efeito sem motivo.
2. Todos seguem a paleta da marca (`brand/paleta.md`): lime #CBEF4B, tinta #141414, creme, vermelho de atenção #D9503F/#E53935. Um efeito "vermelho" por momento de atenção.
3. Continuam valendo a Regra nº 1 (sem dose, seringa, frasco, antes/depois) e o aviso final obrigatório.
4. Cada efeito leva som: whoosh na entrada, hit no impacto, click/pop nos itens. Use as skills real-sfx e earshot.
5. Uma timeline GSAP pausada por efeito, para que todo frame renderize igual. Antes de entregar, mostrar um frame no momento do hit.
6. HyperFrames: usar a versão **fixada** `hyperframes@0.9.19` (nunca `@latest`). Pular o "usage beacon" (`npx hyperframes events`), porque é telemetria e não precisamos.

## Formato atual vs. formato "talking head"
Hoje os Reels usam narração com a voz clonada sobre B-roll (Higgsfield/Buzzy) + overlay HTML.
- ✅ **Funcionam já no formato atual:** 04, 05, 06*, 08*, 10, 13*, 15, 17, 18, 19, 20. (*Sem recorte: aplicar sobre o B-roll, com o título atrás do objeto principal quando o clipe permitir.)
- 🎥 **Precisam do Maxwell filmado (rosto, 9:16, câmera fixa, microfone de lapela, roupa que contraste com o fundo):** 01, 02, 03, 07, 09, 11, 12, 14, 16. É o maior ganho de autoridade possível: vale sugerir 1 vídeo por semana com ele falando.

## Mapa rápido: frase do roteiro → efeito
| Frase do roteiro | Efeito | Janela | Recorta a pessoa |
|---|---|---|---|
| Nomeia 3+ ferramentas, apps ou nutrientes | 01 Orbit | 1,8–3,2 s | sim |
| "Perguntei para a IA…" | 02 Chat Takeover | 2,5–5 s | não |
| "Sair da curva", "ir além" | 03 Frame Escape | 1,5–2,6 s | sim |
| **Uma palavra de impacto: número, "nunca", "zero"** | **04 Snap Zoom** (escala 1,38) | 0,8–2,5 s | não |
| **Lista de 2–4 itens** | **05 Checklist Pop** | 1,5–4,5 s | não |
| **Notícia/hype: "todo mundo está falando"** | **06 Headline Storm** (manchetes reais, com fonte) | 2–4 s | sim/B-roll |
| Mudança de seção: "agora a parte 2" | 07 Zoom Portal | 1,6–3,5 s | não |
| **Resultado com número: "+16%", "de 1 para 10"** | **08 Growth Curve** (contador) | 2–4,5 s | sim/B-roll |
| Revelação: "o segredo é…" | 09 Studio Reveal | 1,6–3 s | sim |
| "Editei / fiz 20…" | 10 B-roll Overlay | 1,8–4 s | não |
| Fala pessoal leve: "sinceramente" | 11 Paper Cutout | 1,5–2,8 s | sim |
| Percepção: "espera…", "o problema é…" | 12 Dolly Zoom | 1,4–3 s | sim (precisa de 5 s de sala vazia) |
| **Estudo de caso / dica numerada** | **13 Magazine Cover** (masthead "OBOLARI") | 1,8–3,2 s | sim/B-roll |
| Nome de ferramenta, "olhe de perto" | 14 Liquid Glass | 1,4–3 s | não |
| **Corte real entre falas** | **15 Zoom-Through Cut** | 1–2 s | não |
| Lugar/contexto: "imagine que você está…" | 16 Green Screen | 2,2–4,2 s | sim |
| **Mito a quebrar: "pare de fazer isso"** | **17 Frame Break** | 1,2–2,4 s | não |
| **"Olhe mais de perto" com 2 palavras fortes** | **18 Digital Zoom** (REC, 1×→2×→3×) | 1,6–3,5 s | não |
| Nome de app/rede: "no Instagram", "no celular" | 19 Phone Mockup | 1,2–3,5 s | não |
| **Recapitulação: "esses são os 3 pilares"** | **20 Checklist** (contador + lista) | 2–4,5 s | não |

Em negrito: os que mais combinam com o nosso conteúdo (estudos, números, mitos, listas).

## Combinações prontas por tipo de Reel
- **Estudo científico** (ex.: força de preensão): 04 no número do gancho → 13 na revista/estudo ("THE LANCET · 2015") → 08 no resultado (+16%) → 20 na recapitulação.
- **Mito ou verdade** (ex.: MOTS-c): 17 Frame Break no "mito" → 05 nos achados → 18 no "olhe mais de perto em humanos" → 20 no veredito.
- **Notícia de peptídeo/longevidade**: 06 com manchetes reais (sempre com fonte na tela) → 04 no dado-chave → 15 nas trocas de assunto.
- **Lista/dicas** (vitaminas, hábitos): 05 em cada item → 20 no final.

## Ferramentas instaladas
- Skills HyperFrames (Apache-2.0, commit 9acdce4): `hyperframes`, `hyperframes-cli`, `media-use` (transcrição, remoção de fundo, mídia), `reverse-any-video` (reconstruir a estrutura de um viral em camadas editáveis; útil para "replicar a estrutura").
- **CLI instalado e testado (06/11/2026)**: `npx -y hyperframes@0.9.19 init|check|render`. Permissão no `.claude/settings.json` só para essa versão; telemetria desligada (HYPERFRAMES_NO_TELEMETRY=1, DO_NOT_TRACK=1). Render 1080x1920 de 6 s em ~18 s.
- Fluxo: `init <dir> --skip-skills --skill=hyperframes` → copiar clipe para `assets/` e fontes para `assets/fonts/` → escrever `index.html` (root com `data-width=1080 data-height=1920`, clips com `class="clip" data-start data-duration`, timeline GSAP pausada em `window.__timelines["main"]`) → `check --json` → `render -o x.mp4 -q delivery`.
- Modelo pronto (04 Snap Zoom + 08 Growth Curve): `modelos/snapzoom-growthcurve/index.html`.
- Para juntar com nosso pipeline: renderizar o trecho do efeito e substituir o segmento correspondente no `bg.mp4` (ou renderizar o overlay inteiro com `--format mov` para ter transparência).
- Achar novos efeitos: o pack sugere o Klint (tryklint.ai), um MCP pago de dados sociais. Está registrado como sugestão em `research/ferramentas.md`; não foi instalado.

## Formato 2: pôster animado 3D (inspirado em @hnrlabs) — piloto 07/11/2026
- 12 s, 1 plano, sem narração. Fluxo: imagem herói 3D (Higgsfield `gpt_image_2_6`, 9:16, fundo preto, espaço livre no topo 35% e rodapé 20%, sem texto/seringa/frasco) → animação 12 s (Higgsfield `kling3_0`, start_image = job da imagem, sound off, push-in lento + "acender" o tecido) → texto fixo via HyperFrames (`modelos/poster-3d/index.html`: selo OBOLARI ACADEMY | CATEGORIA, título gigante com brilho na cor do tema, subtítulo 1 linha, rótulo + benefício no rodapé, "Entenda na legenda 👇", @, aviso) → música -6 dB + whoosh/shimmer/riser/impact (earshot) → -14 LUFS.
- Todo o conteúdo vai na legenda longa (seções com emoji, "Vale saber" com as limitações, CTA comentário + GUIA + salvar, aviso).
- Custo: 1 imagem + 1 clipe de 12 s no Higgsfield. Comparar desempenho com o Reel narrado antes de escalar.
