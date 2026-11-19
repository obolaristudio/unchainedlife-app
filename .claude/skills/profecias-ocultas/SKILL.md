---
name: profecias-ocultas
description: Linha editorial do segundo Instagram do Maxwell, sobre profecias bíblicas e o que está acontecendo "por trás" do mundo (tecnologia, poder, controle) enquanto as pessoas estão de olhos fechados. Use SEMPRE que o Maxwell mandar um link de Reel neste formato ou pedir vídeo de profecia, teoria, sinais do fim, marca da besta, controle global etc. Não usar as regras da Obolari Academy (peptídeos) aqui.
---

# Vídeos de profecias e coisas ocultas (perfil separado da Obolari)

**Pedido do Maxwell (19/11/2026):** o perfil é sobre profecias bíblicas e o oculto que está acontecendo no mundo, com o ser humano de olhos fechados. Ir direto ao ponto, com convicção, e **entregar o conteúdo**. Não diluir o tema com ressalvas.

## Tom
- Convicto e de alerta: "os sinais estão aí", "abra os olhos", "a Bíblia já avisou".
- Sem frases que enfraqueçam a mensagem ("é só uma teoria", "pode não ser"). No máximo uma pergunta provocativa no final.
- Linguagem simples, frases curtas, suspense crescente.
- Versículos citados com capítulo e versículo certos (ARC/ACF).
- Fatos do mundo real (empresas, datas, números, falas de pessoas públicas) precisam estar **corretos**, com fonte anotada. A interpretação profética é livre e forte; o fato não é inventado. Um fato errado derruba a credibilidade do perfil.

## Fluxo para cada link
1. Baixar (`yt-dlp`) → transcrever (faster-whisper, áudio em PCM via ffmpeg) → contact sheet a cada 4 s.
2. Mapear a estrutura: gancho → virada → "salve o vídeo" → regra/princípio → cenário atual (fatos) → ligação com a profecia → objeção respondida com versículo → fechamento → CTA.
3. Roteiro novo com a mesma estrutura e o mesmo ritmo (texto, imagens e áudio originais). De 60 a 90 s.
4. Voz: ElevenLabs, voice "Maxwell Obolari" `OzlrOiSmF6F4M3mkabDT`, `eleven_v4`, 1 versão → `silenceremove` + `atempo=1.07`.
5. Cenas: Higgsfield `gpt_image_2_6` (9:16, cinematográfico escuro com vermelho) + `kling3_0` 5 s nas 5–6 cenas-chave. Não usar o rosto de pessoas reais; usar símbolos (chip, marca na mão/testa, filas, telas, Bíblia à luz de vela).
6. Montagem: `build.py` (`.claude/skills/profecias-ocultas/build.py`, trocar a lista `cuts` e os `card(...)` a cada vídeo): legenda palavra a palavra Inter ExtraBold com palavras-chave em vermelho `#E53935`, títulos no topo nos pontos-chave, whoosh nos cortes, riser + impacto na virada profética, trilha sombria baixa com ducking, -14 LUFS, 1080×1920.
7. Entregar o MP4 + legenda do post (gancho, 2–3 linhas, versículo, pergunta, 5 hashtags). Não postar sem o Maxwell pedir.

## CTA padrão
Pergunta aberta ligada ao tema ("Você aceitaria a marca para poder trabalhar?"), ou "compartilhe com quem precisa abrir os olhos".
