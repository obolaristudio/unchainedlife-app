---
name: olhos
description: Faz o Claude assistir um vídeo de verdade, e não só ler a transcrição. Baixa o vídeo (link ou arquivo), tira quadros em intervalos, monta folhas com o horário escrito em cada quadro, transcreve a fala no seu computador e responde citando o segundo exato. Use quando a pessoa digitar /olhos, mandar um vídeo ou link (Instagram, TikTok, YouTube) e pedir para analisar, resumir, modelar a edição, achar um momento ou descrever o que aparece na tela.
argument-hint: "[link ou arquivo do vídeo] [sua pergunta]"
---

# Olhos

> **Instalação.** Se a pessoa colou o link deste arquivo e pediu para instalar:
>
> 1. Salve este arquivo como `~/.claude/skills/olhos/SKILL.md`, com o conteúdo exato (não use um resumo):
>    - Mac, Linux ou Windows com Git Bash:
>      `mkdir -p ~/.claude/skills/olhos && curl -fsSL https://cdn.aysllan.com/skills/olhos/SKILL.md -o ~/.claude/skills/olhos/SKILL.md`
>    - Windows PowerShell:
>      `New-Item -ItemType Directory -Force "$HOME\.claude\skills\olhos" | Out-Null; Invoke-WebRequest "https://cdn.aysllan.com/skills/olhos/SKILL.md" -OutFile "$HOME\.claude\skills\olhos\SKILL.md"`
> 2. Confira que o arquivo salvo começa com `---`.
> 3. Veja se `ffmpeg`, `yt-dlp` e `uv` estão instalados. Se faltar algum, peça permissão e instale:
>    - Mac: `brew install ffmpeg yt-dlp uv`
>    - Windows: `winget install Gyan.FFmpeg yt-dlp.yt-dlp astral-sh.uv`
>    - Linux: pelo gerenciador de pacotes, ou `pipx install yt-dlp` e o instalador do uv (astral.sh/uv).
> 4. Diga à pessoa: "Pronto! Agora digite /olhos com o link ou o arquivo do vídeo e a sua pergunta. Exemplo: /olhos https://www.instagram.com/reel/... o que acontece na tela em cada parte?". Se /olhos não aparecer, peça para ela rodar /reload-skills ou abrir uma conversa nova.
> 5. Pare aqui.

Pedido da pessoa: $ARGUMENTS

A transcrição só conta o que foi **dito**. Tudo o que aparece na tela (o texto, a edição, a interface, o gesto, o produto) fica de fora. Esta skill faz o Claude **ver** o vídeo: ele folheia o vídeo como uma tira de filme, com o horário escrito em cada quadro, junta com o que foi falado e responde apontando o segundo exato. Tudo roda no computador da pessoa, sem serviço pago.

## 1. Preparar

- **Faltou o vídeo?** Responda só: "Me manda o link ou o arquivo do vídeo e o que você quer saber dele." e pare.
- **Faltou a pergunta?** Use: "o que acontece no vídeo, parte por parte, e o que aparece na tela em cada momento".
- Crie a pasta `olhos/{nome-curto}/` na pasta onde o Claude Code está aberto. Tudo vai para lá.
- Confira `ffmpeg`, `yt-dlp` (só para links) e `uv`. Se faltar, peça permissão e instale como no bloco de instalação.

## 2. Pegar o vídeo

- **Link:** `yt-dlp -f "bv*[height<=1080]+ba/b" --merge-output-format mp4 -o "olhos/{nome}/video.mp4" "LINK"`
  - Só vídeos públicos, para a pessoa analisar. Não republique o vídeo de ninguém.
  - Se o yt-dlp falhar (vídeo privado, site bloqueando), peça à pessoa o arquivo.
- **Arquivo:** use o próprio arquivo, sem copiar.
- Duração: `ffprobe -v error -show_entries format=duration -of csv=p=0 VIDEO`

## 3. Tirar os quadros

Escolha o intervalo pela duração (no máximo uns 120 quadros, ou 8 folhas):

| Duração | Um quadro a cada |
|---|---|
| até 1 minuto | 1 segundo |
| até 3 minutos | 2 segundos |
| até 10 minutos | 5 segundos |
| até 30 minutos | 15 segundos |
| mais que isso | duração ÷ 120 |

Se a pergunta for sobre um trecho ("o que acontece no minuto 4"), tire os quadros só desse trecho, mais apertado (a cada 0,5 s), com `-ss INICIO -to FIM` antes do `-i`.

```
ffmpeg -v error -i VIDEO -vf "fps=1/INTERVALO,scale=360:-2" -q:v 3 "olhos/{nome}/quadros/q_%05d.jpg"
```

Vídeo deitado (16:9): use `scale=480:-2`.

## 4. Montar as folhas com o horário

Salve este script como `olhos/{nome}/folhas.py`, sem mudar nada:

```python
# folhas.py: monta folhas de contato com o tempo escrito em cada quadro.
# Uso: python folhas.py PASTA_DOS_QUADROS INTERVALO_EM_SEGUNDOS PASTA_DE_SAIDA [INICIO_EM_SEGUNDOS]
import glob
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

pasta, intervalo, saida = sys.argv[1], float(sys.argv[2]), Path(sys.argv[3])
inicio = float(sys.argv[4]) if len(sys.argv) > 4 else 0.0
saida.mkdir(parents=True, exist_ok=True)
quadros = sorted(glob.glob(f"{pasta}/q_*.jpg"))
COLS, LINHAS, MARGEM = 4, 4, 8
POR_FOLHA = COLS * LINHAS
try:
    fonte = ImageFont.load_default(size=26)
except TypeError:
    fonte = ImageFont.load_default()


def hms(seg):
    seg = int(round(seg))
    h, m, s = seg // 3600, seg % 3600 // 60, seg % 60
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


if not quadros:
    sys.exit("nenhum quadro encontrado")
w, h = Image.open(quadros[0]).size
for n in range(0, len(quadros), POR_FOLHA):
    grupo = quadros[n:n + POR_FOLHA]
    linhas = (len(grupo) + COLS - 1) // COLS
    folha = Image.new("RGB", (COLS * (w + MARGEM) + MARGEM, linhas * (h + MARGEM) + MARGEM), "white")
    d = ImageDraw.Draw(folha)
    for i, arq in enumerate(grupo):
        x = MARGEM + (i % COLS) * (w + MARGEM)
        y = MARGEM + (i // COLS) * (h + MARGEM)
        folha.paste(Image.open(arq).convert("RGB"), (x, y))
        rotulo = hms(inicio + (n + i) * intervalo)
        caixa = d.textbbox((0, 0), rotulo, font=fonte)
        d.rectangle([x, y, x + caixa[2] + 14, y + caixa[3] + 10], fill="black")
        d.text((x + 7, y + 4), rotulo, fill="white", font=fonte)
    nome = saida / f"folha_{n // POR_FOLHA + 1:02d}.jpg"
    folha.save(nome, quality=85)
    print(nome)
```

Rode:

```
uvx --python 3.12 --with pillow python "olhos/{nome}/folhas.py" "olhos/{nome}/quadros" INTERVALO "olhos/{nome}/folhas" [INICIO]
```

Cada folha tem 16 quadros, em ordem, com o horário no canto de cada um.

## 5. Ouvir (transcrever no computador)

- **Mac com chip Apple:** `uvx --python 3.12 --from mlx-whisper mlx_whisper VIDEO --model mlx-community/whisper-large-v3-turbo --output-format json --output-dir "olhos/{nome}"`
- **Outros computadores:** `uvx --python 3.12 --from openai-whisper whisper VIDEO --model turbo --output_format json --output_dir "olhos/{nome}"`
- Sem `--language`: o Whisper descobre o idioma sozinho.
- Na primeira vez ele baixa o modelo de voz (alguns minutos). Avise a pessoa.
- **Vídeo sem fala?** Pule este passo.
- **A pergunta é sobre som ou edição** (efeitos, cortes, música)? Gere também o gráfico do som: `ffmpeg -v error -i VIDEO -lavfi "showspectrumpic=s=1800x500:legend=1:scale=log:fscale=log" "olhos/{nome}/som.png"`. Batidas e efeitos aparecem como riscos verticais; graves fortes, como manchas embaixo.

## 6. Assistir

1. Abra as folhas **em ordem** e olhe cada quadro: o que está na tela, o texto escrito, o enquadramento, o que mudou desde o quadro anterior.
2. Junte com a transcrição pelo horário.
3. Escreva `olhos/{nome}/linha-do-tempo.md`, com uma linha por momento: `mm:ss | o que aparece na tela | o que é dito`.
4. **Precisa ver um detalhe de perto** (um texto pequeno, uma tela)? Tire o quadro em tamanho real naquele segundo e abra: `ffmpeg -v error -ss SEGUNDOS -i VIDEO -frames:v 1 "olhos/{nome}/zoom_SEGUNDOS.jpg"`

## 7. Responder

- Responda à pergunta citando o horário de cada coisa: "em 00:12 aparece...".
- Quando algo acontece entre dois quadros, diga o intervalo ("entre 00:12 e 00:14").
- No fim, diga onde estão as folhas e a linha do tempo, e ofereça olhar mais de perto qualquer trecho.

## Regras

- **Nunca invente** o que não está nos quadros ou na fala. Se não deu para ver (quadro borrado, texto pequeno), diga isso e tire o quadro em tamanho real.
- **Cada folha gasta uso do seu plano do Claude.** Para vídeos longos, comece com poucas folhas e aprofunde só no trecho que importa. Peça confirmação antes de passar de 10 folhas.
- **Vídeos de outras pessoas** servem para estudar, não para republicar.
