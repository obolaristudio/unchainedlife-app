---
name: profecias-ocultas
description: Linha editorial do perfil "Obolari Teorias" do Maxwell — vídeos apocalípticos sobre o Apocalipse, a volta de Jesus, a besta, o anticristo e o que está acontecendo "por trás" do mundo (tecnologia, poder, controle) enquanto as pessoas estão de olhos fechados. Use SEMPRE que o Maxwell mandar um link de Reel para recriar, pedir vídeo de profecia, teoria, sinais do fim, marca da besta, controle global, ou capas/legendas para o Obolari Teorias. Não usar as regras da Obolari Academy (peptídeos) aqui.
---

# Obolari Teorias — vídeos apocalípticos (perfil separado da Obolari Academy)

**Pedido do Maxwell (19 e 20/11/2026):** todo vídeo deste perfil tem **tom apocalíptico**: Apocalipse, volta de Jesus, a besta, o anticristo, o engano do fim dos tempos. Ir direto ao ponto, com convicção, e **entregar o conteúdo**. Não diluir com ressalvas.

## Regras fixas (sempre)
1. **Tom apocalíptico em todo vídeo.** Ligar o assunto do link (tecnologia, famosos, poder, dinheiro, natureza) ao fim dos tempos: besta, anticristo, marca, engano, volta de Jesus.
2. **Base bíblica em todo vídeo.** Pesquisar e acrescentar passagens que se aplicam ao tema (ARC/ACF). Citar o texto na narração.
3. **Fechamento com a referência.** No final, a narração diz onde está na Bíblia: "Está escrito em [Livro], capítulo X, versículo Y". A referência também aparece como título na tela.
4. **Recriar, não copiar.** Mesma estrutura, gancho e ritmo do vídeo de referência; roteiro, imagens e áudio novos, com a voz do Maxwell.
5. **Capas em vermelho e preto.** Fundo escuro, título branco Inter Black em caixa alta, 1–2 palavras em vermelho brilhante (`#FF2D2D` com brilho), selo vermelho no topo do título (ex.: "APOCALIPSE 13"), sub-linha curta. Entregar 3 opções + recomendação.
6. **Legenda do post** pronta: gancho = texto da capa, 3–5 linhas, versículo por extenso, pergunta, "salve e envie", 10 hashtags e, na última linha, `obolari teorias`.

## Tom
- Convicto e de alerta: "a máscara caiu", "os sinais estão aí", "abra os olhos", "a Bíblia avisou".
- Sem frases que enfraqueçam ("é só uma teoria", "pode não ser").
- Frases curtas, linguagem simples, suspense crescente até a virada bíblica.
- **Fatos do mundo real sempre corretos** (datas, números, empresas, falas de pessoas públicas), checados com WebSearch e fonte anotada. A leitura profética é livre e forte; o fato não se inventa. Sobre pessoas reais: mostrar o que elas fizeram e disseram e ligar à profecia; não afirmar como fato crime ou pacto que não existe (risco de processo e de derrubada do post).

## Versículos mais usados
- Apocalipse 13:3 ("toda a terra se maravilhou após a besta"), 13:16-17 (marca na mão direita ou na testa; ninguém compra ou vende).
- 2 Coríntios 11:14 (Satanás se transfigura em anjo de luz). Mateus 24:24 (falsos cristos e falsos profetas enganariam, se possível, os escolhidos).
- Efésios 6:12 (principados, potestades, príncipes das trevas). Romanos 1:20 (a criação revela o Criador).
- 2 Tessalonicenses 2:3-4 e 2:9-10 (o homem do pecado, sinais e prodígios de mentira). Daniel 12:4 (a ciência se multiplicará). 1 João 2:18 (muitos anticristos).

## Fluxo para cada link
1. Baixar (`yt-dlp`) → transcrever (faster-whisper, áudio em PCM via ffmpeg; script `tx.py`/`txw.py`) → contact sheet a cada 3–4 s. Se o Instagram bloquear (limite sem login), tentar `gpt_social analyze_post`; se falhar, avisar e pedir o MP4.
2. Mapear a estrutura: gancho → autoridade/números → "quase ninguém percebeu" → fatos → padrão do sistema → virada bíblica → fechamento com referência → CTA.
3. Checar cada fato (WebSearch). Corrigir o que estiver errado no original.
4. Roteiro de 80–100 s. Voz: ElevenLabs "Maxwell Obolari" `OzlrOiSmF6F4M3mkabDT`, `eleven_v4`, 1 versão → `silenceremove` + `atempo=1.07` → transcrição palavra a palavra; corrigir palavras erradas no `words.json`.
5. Cenas: Higgsfield `gpt_image_2_6` 9:16, cinematográfico escuro com vermelho → `kling3_0` 5 s em todas as cenas (≈6 créditos cada). Evitar pessoas sem camisa (filtro bloqueia).
6. **Pessoas públicas:** usar fotos reais com licença livre do Wikimedia Commons (API `generator=search`, uma busca por vez — a API limita pedidos seguidos). Montar vertical 1080×1920: fundo desfocado + recorte 4:5 + crédito pequeno ("Foto: Autor, licença"). Nunca usar foto de agência/Google (risco de direitos autorais). Créditos também na legenda do post.
7. Montagem: `build.py` desta pasta (trocar `cuts`, `RED`, `card(...)`, `sfx`): legenda palavra a palavra Inter ExtraBold com palavras-chave em vermelho, títulos no topo, whoosh nos cortes, riser + impacto na virada bíblica, trilha sombria baixa com ducking, -14 LUFS, 1080×1920.
8. Revisar contact sheet → entregar MP4 (SendUserFile) + legenda; capas (3) quando pedir. Não postar sem o Maxwell pedir.

## CTA padrão
Pergunta aberta que provoca ("Você aceitaria o chip?", "Você ainda deixa seus filhos assistirem?") + "compartilha com quem precisa acordar".
