# Pipeline da rotina da madrugada (20/11/2026)
Por vídeo, uma pasta de trabalho com `voice.wav` (ElevenLabs, silenceremove + atempo 1.07), `vwords.json` (wh.py, faster-whisper small) e `cfg.py` (exemplos em `videos/teriparatida/cfg.py` e `videos/afamelanotida/cfg.py`: títulos por seção, overlays chips/big/bars/count/stamp/cta e clipes Mixkit por seção).
1. `python3 scrape.py <termos>` lista clipes Mixkit ainda não usados (filtra `research/clipes-usados.md`); baixar em `stock/<id>.mp4`.
2. `python3 gen.py <pasta>` → `hf/index.html` (copiar Bricolage-700/800.ttf para `hf/assets/fonts`).
3. `python3 mkbg.py <pasta>` → `hf/assets/bg.mp4` (painel 1080×1100 + fundo desfocado + zoom de entrada).
4. `python3 mix.py <pasta> <musica.mp3>` → `mix.wav` (voz + música com ducking + SFX de `brand/sfx`).
5. `npx hyperframes render . -o ../silent.mp4` dentro de `hf/` (rodar em background; um render por vez), depois mux com CRF 23/maxrate 1.5M (< 20 MB por causa do jsDelivr).
6. `capa.js` gera a capa a partir de `ph.jpg` + `capa.json`.
