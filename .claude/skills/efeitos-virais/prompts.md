# Prompts "do zero" (build from scratch) dos 20 efeitos

Copiados do pack de David Roberts. Todos são 1080x1920, numa timeline GSAP pausada, com render e um frame mostrado no hit.
Quando diz "Cut me out", rodar `npx hyperframes@0.9.19 remove-background` e usar a sala e o recorte como 2 camadas.
Os prompts "com template" (`node fx.mjs …`) estão no README de cada pasta do zip e no doc original.

Prompt inicial do pack: transcrever o vídeo com tempo de cada palavra (no nosso pipeline: `tx.py` / faster-whisper, que já gera words.json).

01 Orbit (cut out): On the hit word, 6 small rounded icon tiles fly in on a spiral and circle my head on a tilted ellipse at chin height, about one turn in 1.3 s, on a faint dotted path. Back-half tiles sit between background and cut-out (behind my head); front-half tiles sit above the cut-out.

02 Chat Takeover: On the hit word, shrink my full video into a rounded card on the right side of a clean chat window. A user bubble types my prompt. An assistant row answers with a short title and 3 rows, each getting a check mark at its own time. In the last 0.3 s the video card grows back to full frame.

03 Frame Escape (cut out): On the hit word, the frame becomes a photo print with a white border on a dark ground; it tilts ~6°, shrinks and drops to the lower part. My cut-out stays full size on top, so head and shoulders stand above the print's top edge. At the end the print grows back to full frame.

04 Snap Zoom: On the hit word, scale the video around the center of my face from 1.0 to ~1.38 in 3 frames with a sharp ease out. Hold, then snap back to 1.0 a quarter second before the window ends.

05 Checklist Pop: On the hit word, show small empty rings beside my head, one per item. Each ring becomes a white pill with a filled check dot and the item text on the word where I say it. Stack on the side with more room. Clear the pills at the end.

06 Headline Storm (cut out): On the hit word, white headline strips with bold black capitals and a small colored tag slam in at small angles, one every 2–3 frames, piling around my head. Strips at head height go behind the cut-out, strips under the chin in front, never covering the mouth. At the end all leave at once.

07 Zoom Portal: On the hit word, a small circle with a colored ring opens beside my head with a second live copy of my video framed close on my face. At dive_at, push the camera into the circle with strong motion blur for ~0.3 s, so the circle becomes the full frame as a close shot.

08 Growth Curve (cut out): On the hit word, replace my room with a light chart grid. A bright line draws up and right behind my cut-out and ends in a dot. A pill at top right counts from start to end value as the line climbs; the end value lands on the result word.

09 Studio Reveal (cut out): From window start, the frame goes nearly black, me dimly lit. On the hit word, a studio set lights up behind me: two angled softboxes and a lit sign above my head. Make me a little brighter after the reveal.

10 B-roll Overlay: On the hit word, shrink my video into the preview monitor of a simple editor window. Below, a timeline with a talking-head track and a B-roll track. On count_at, clips stack onto the B-roll track with a counter and the playhead moves. Last 0.3 s, the full frame slides back down from the top.

11 Paper Cutout (cut out): On the hit word, replace my room with a flat color collage (star, circle, ring, dots, diagonal stripe). Give my cut-out a thick white sticker edge.

12 Dolly Zoom (cut out + empty-room still): Empty room still as background, cut-out on top. On the hit word, scale the room up to ~1.2 around my face while the cut-out stays the same size; add slight blur and dark edges to the room. End with a white flash on the last 4 frames.

13 Magazine Cover (cut out): On the hit word, a white camera flash, and the room becomes a magazine cover: giant masthead behind my cut-out (head covers part of it), small kicker, headline beside my head, 2 cover lines on the other side, issue line, barcode, round badge. A second shorter flash in the middle.

14 Liquid Glass: On the hit word, a round clear glass lens with a bright rim slides in from the side with more room and stops over my face, magnifying and bending the picture ~1.3× at the center like a water drop. Then it slides out.

15 Zoom-Through Cut: Before the cut, push into my face up to ~1.7×, faster and faster, with growing motion blur and a short white lift at the peak; blur peak lands on the cut. After the cut the next shot opens close and settles to normal in ~0.4 s.

16 Green Screen (cut out): On the hit word, replace my room with flat chroma green behind the cut-out. On scene_at, a new background opens from behind my head (illustrated city skyline at dusk, or a given 9:16 photo).

17 Frame Break: On the hit word, freeze the frame. Crack lines draw out from one point beside my face, never on it. At break_at, the frame breaks into shards that fall and turn, revealing the live video after the cut.

18 Digital Zoom: On the hit word, a camera screen comes on (REC dot, corner brackets, time code, zoom pill). Snap to 2× on the first step word and 3× on the second, centered on my face, pill showing each value. Then snap back to 1× and remove the camera screen.

19 Phone Mockup: On the hit word, shrink my video into the screen of a phone in the middle of a clean background. A badge with the app icon and a short label lands beside the phone on the platform word. Last 0.3 s, the phone grows back to full frame.

20 Checklist: On the hit word, a dark circle grows from the center and covers the frame. On it, a recap board: big counter, short title, list in one or two columns. Rows tick off one by one and the counter counts up with each tick.

## Adaptação para B-roll (sem rosto)
Trocar "my face" pelo ponto de interesse do clipe (ex.: a mão no dinamômetro) e "cut-out" pelo objeto principal recortado com `remove-background`, ou usar o efeito só na camada de overlay.
