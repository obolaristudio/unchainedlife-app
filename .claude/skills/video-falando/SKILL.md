---
name: video-falando
description: Edição de vídeos do Maxwell FALANDO para a câmera (talking head) no estilo "palavra atrás da cabeça" + legendas sincronizadas no quadro exato + camadas 3D + SFX, adaptado do guia de Shaan Johari (@viashaan, "How I edited my captions reel with AI"). Use SEMPRE que o Maxwell mandar um vídeo dele gravado falando (selfie, celular, câmera) para virar Reel/Short, junto com video-effects e efeitos-virais.
---

# Vídeo do Maxwell falando → Reel

Fonte: https://ruby-cotija-fb5.notion.site/How-I-edited-my-captions-reel-with-AI-40b28691eca381a3ad10cbc917160c2d (Shaan Johari, @viashaan). Analisado e adaptado em 07/11/2026.

## A técnica (o que faz o vídeo parecer "editado por profissional")
Cada quadro é uma pilha, de trás para frente:
1. **Fundo** (a sala original, ou um cenário trocado);
2. **Palavras atrás** do Maxwell (a palavra-chave gigante);
3. **O Maxwell recortado** (máscara com borda suave, quadro a quadro);
4. **Palavras na frente** (legendas pequenas, até 3 palavras por vez).
Uma câmera virtual se move levemente pela pilha inteira: o texto fica em 3D, não colado na tela.

## Fluxo (rodar sempre nesta ordem)
1. **Receber o vídeo** e perguntar (ou escolher): a palavra que vai atrás da cabeça (número ou o assunto da frase) e nomes de marcas/substâncias para grafar certo (ex.: GHK-Cu, semaglutida, Mounjaro).
2. **Áudio limpo**: opcional Adobe Podcast (grátis, Maxwell sobe); senão ffmpeg (`highpass=80,afftdn,loudnorm`).
3. **Transcrição com tempo de cada palavra**: já temos `tx.py` (faster-whisper "small", áudio decodificado com ffmpeg 16 kHz mono para numpy, NUNCA passar caminho de arquivo; `word_timestamps`, sem initial prompt). Mostrar o texto ao Maxwell e esperar o OK. Depois **ajustar o início de cada palavra ao pico do áudio** (o whisper costuma adiantar ~0,1 s). Legenda 3 quadros atrasada já incomoda.
4. **Recorte do Maxwell**: `rembg` com `birefnet-portrait` (CPU, ~1 GB de modelo, alguns segundos por quadro) ou `npx hyperframes@0.9.19 remove-background` (skill media-use). Guardar a máscara alfa com borda suave (cabelo). Avisar o tempo antes de começar.
5. **Palavra atrás da cabeça**:
   - fonte de impacto em CAIXA ALTA (nossa marca: **Bricolage Grotesque 800**; alternativa do guia: Anton), branca, ~85% da largura;
   - achar o topo da cabeça pela máscara (só nos 40% centrais da largura, para mão levantada não contar);
   - a cabeça cobre ~60% da altura das letras e pelo menos 15% delas; se cobrir menos (boné), descer a palavra;
   - entra no quadro em que ele fala: escala 80%→100% em 6 quadros com ~5% de overshoot; depois fica parada;
   - **cor de destaque** (vermelho #E53935 ou lime #CBEF4B) só na palavra mais importante do vídeo.
6. **Legendas na frente**: Inter Bold (ou Bricolage 700), ~7% da largura, sombra escura suave, até 3 palavras por grupo, quebradas em pausas naturais, cada palavra aparece no seu tempo; ficam entre **15% e 65% da altura** (o terço de baixo é da legenda/botões do Instagram, e a lateral direita dos botões); nunca repetir a palavra gigante.
7. **Câmera virtual**: leve push-in/drift (2–4%) na pilha inteira; punch-in nas palavras fortes (ver `efeitos-virais`: 04 Snap Zoom, 13 Magazine Cover, 08 Growth Curve, 05 Checklist Pop funcionam ainda melhor com o recorte).
8. **Som**: cada coisa que se move na tela ganha um som (whoosh na palavra que entra, tick/pop nas legendas-chave), baixo e sob a voz. Usar skills `real-sfx` + `earshot`; master -14 LUFS.
9. **Storyboard antes**: um quadro parado por frase (PNG) para o Maxwell aprovar o estilo, depois o render completo.
10. **Notas no quadro**: o Maxwell aponta "essa palavra entra atrasada", "essa maior e atrás da cabeça"; mudar só o que ele pediu e reexportar.
11. **Exportar** H.264 no tamanho e fps originais, preservando as cores (usar as configs de cor do próprio vídeo ao extrair/remontar quadros) + um PNG de checagem com a palavra gigante.
12. Aviso obrigatório no fim e na legenda (Regra nº 1 e "não é recomendação médica nem sugestão de uso").

## Como o Maxwell deve gravar (mandar para ele antes)
- Celular **na vertical**, travado (tripé), cabeça e ombros no centro, **espaço acima da cabeça** (é onde a palavra senta).
- Microfone de lapela; nada de suporte de microfone na frente (aparece no recorte).
- **Luz no rosto e no cabelo**, roupa que contraste com o fundo (camiseta escura em sala escura quebra o recorte).
- Segurar ~2 s parado depois de uma frase que vai ganhar efeito.
- Para efeitos que precisam da sala vazia (Dolly Zoom), sair do quadro 5 s no fim, gravando.
- Takes curtos: o guia usou ~1.000 quadros (≈33 s); dá para juntar takes.

## Estilo Obolari (regras que vão se acumulando)
- 2 fontes, não 10: Bricolage 800 para a palavra que importa, Inter/Bricolage 700 para o resto.
- 1 cor de destaque por frase; o resto branco.
- Texto fora do terço inferior e da lateral direita.
- Quando o Maxwell aprovar algo ("gostei disso"), **anotar aqui como regra nova** para o estilo crescer de vídeo para vídeo.

## Ferramentas
- Grátis/instaladas: faster-whisper (tx.py), ffmpeg, HyperFrames 0.9.19 (render das camadas, remove-background), real-sfx/earshot, Playwright.
- A instalar na primeira vez (com aviso ao Maxwell, ~1,5 GB): `rembg[cpu]` + modelo `birefnet-portrait`, numa venv dentro da pasta do projeto.
- Pagas, opcionais (sugerir, não assinar sozinho): **Beeble** (troca a sala e reilumina a pessoa), **Adobe Podcast** (limpeza de voz; tem plano grátis).
- Remotion (usado no guia) exige licença para empresas com 4+ pessoas; nós usamos HyperFrames + ffmpeg, que fazem o mesmo papel.
