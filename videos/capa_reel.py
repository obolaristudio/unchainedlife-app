# Capa 1080x1920 (área segura 4:5 no centro): frame do vídeo + título grande da marca.
# uso: python3 capa_reel.py video.mp4 segundo "LINHA1" "LINHA2 (verde)" "rodapé" saida.jpg fontes_dir
import sys, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter
v, t, l1, l2, sub, out, fd = sys.argv[1:8]
subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-ss', t, '-i', v, '-frames:v', '1', '/tmp/_f.png'], check=True)
im = Image.open('/tmp/_f.png').convert('RGB')
ov = Image.new('RGBA', im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
d.rectangle([0, 0, 1080, 1920], fill=(0, 0, 0, 90))
im = Image.alpha_composite(im.convert('RGBA'), ov); d = ImageDraw.Draw(im)
F = lambda s: ImageFont.truetype(f'{fd}/Bricolage-800.ttf', s)
def center(txt, y, f, fill, box=None):
    w = d.textlength(txt, font=f); x = (1080 - w) / 2
    if box: d.rounded_rectangle([x - 30, y - 10, x + w + 30, y + f.size + 24], 26, fill=box)
    d.text((x, y), txt, font=f, fill=fill)
center('OBOLARI ACADEMY · PEPTÍDEOS', 560, F(34), (203, 239, 75))
s = 120
while d.textlength(l1, font=F(s)) > 960: s -= 6
center(l1, 650, F(s), 'white')
s2 = 130
while d.textlength(l2, font=F(s2)) > 900: s2 -= 6
center(l2, 650 + s + 40, F(s2), (20, 20, 20), box=(203, 239, 75))
center(sub, 650 + s + s2 + 130, F(50), 'white')
im.convert('RGB').save(out, quality=92); print('capa ok')
