# Rotina madrugada 25/11/2026

- Publicados na fila: `glu/` (Glucagon, 77 s) e `cic/` (Ciclosporina, 80 s). Reel final: `*/reel.mp4`; capa: `*/capa.jpg`; legenda: `*/legenda.txt`.
- `ins/` (Insulina) e `tb4/` (Timosina β4 / TB-500) foram produzidos e DESCARTADOS: os dois peptídeos já tinham sido publicados (02/11 e 01/11). Ficam só os roteiros/specs.
- Pipeline: `mkbg.py <dir>` (cenas Mixkit 1080x1920, painel + fundo desfocado, zoom lento) → `gen.py <dir>` (HyperFrames: títulos, cards, contadores, carimbo surpresa, legenda palavra a palavra, de `spec_<dir>.py`) → `npx hyperframes render` → `mix.py <dir> <trilha Mixkit>` (voz + música com ducking + SFX de `brand/sfx`, −14 LUFS, H.264 ≤ 1,5 Mbps para caber no jsDelivr). Capas: `capa.cjs`.
- Voz: ElevenLabs "Maxwell Obolari" (eleven_v4), 1 take; silêncios cortados e atempo 1,10.
