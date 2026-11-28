import json, re, subprocess, sys, os
from PIL import Image, ImageDraw, ImageFont
cfg = json.load(open(sys.argv[1]))
N = cfg['name']; D = f'out_{N}'; os.makedirs(D, exist_ok=True)
W = json.load(open(cfg['words']))
for i, w in enumerate(W):
    w['w'] = cfg.get('fix', {}).get(w['w'], w['w'])
T = round(float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',cfg['voice']],capture_output=True,text=True).stdout)+0.8, 2)
PX, PY, PW, PH = 40, 430, 1000, 1080
FB = '/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf'
FM = '/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf'

# ---------- base canvas (brand notebook) ----------
im = Image.new('RGB', (1080, 1920), '#F2EFE6'); d = ImageDraw.Draw(im)
for x in range(0, 1080, 40): d.line([(x, 0), (x, 1920)], fill='#E6E3DA', width=1)
for y in range(0, 1920, 40): d.line([(0, y), (1080, y)], fill='#E6E3DA', width=1)
d.line([(28, 120), (28, 1920)], fill='#D9503F', width=3)
d.rectangle([0, 0, 1080, 110], fill='#2B2B2B')
f1 = ImageFont.truetype(FB, 26)
d.ellipse([40, 44, 62, 66], fill='#CBEF4B'); d.text((76, 40), 'OBOLARI ACADEMY', font=f1, fill='#F2EFE6')
s = cfg['serie']; tw = d.textlength(s, font=f1); d.text((1040 - tw, 40), s, font=f1, fill='#CBEF4B')
d.rounded_rectangle([PX + 14, PY + 14, PX + PW + 14, PY + PH + 14], 22, fill='#141414')
d.rounded_rectangle([PX - 4, PY - 4, PX + PW + 4, PY + PH + 4], 24, fill='#141414')
f2 = ImageFont.truetype(FB, 22)
t = 'CONTEÚDO EDUCATIVO · NÃO É RECOMENDAÇÃO MÉDICA'
d.rectangle([60, 1838, 66, 1866], fill='#D9503F'); d.text((80, 1838), t, font=f2, fill='#555555')
im.save(f'{D}/base.png')
mask = Image.new('L', (PW, PH), 0); ImageDraw.Draw(mask).rounded_rectangle([0, 0, PW - 1, PH - 1], 22, fill=255); mask.save(f'{D}/mask.png')

# ---------- panel clips ----------
sc = cfg['scenes']; parts = []
for i, (a, c, off) in enumerate(sc):
    b = sc[i + 1][0] if i + 1 < len(sc) else T
    dur = round(b - a, 3); out = f'{D}/p{i:02d}.mp4'
    z = "1+0.22*max(0\\,1-t/0.45)+0.04*t/%s" % dur
    vf = (f"setpts=PTS-STARTPTS,fps=30,scale={PW}:{PH}:force_original_aspect_ratio=increase,crop={PW}:{PH},"
          f"scale=w='trunc({PW}*({z})/2)*2':h='trunc({PH}*({z})/2)*2':eval=frame,crop={PW}:{PH},"
          f"eq=saturation=1.08:contrast=1.04,colorbalance=rs=0.04:bs=-0.03,setsar=1,format=yuv420p")
    if not os.path.exists(out):
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-ss', str(off), '-stream_loop', '-1', '-i', f'stock/{c}.mp4', '-t', str(dur), '-vf', vf, '-an', '-c:v', 'libx264', '-crf', '17', '-preset', 'veryfast', out], check=True)
    parts.append(out)
open(f'{D}/list.txt', 'w').write(''.join(f"file '{os.path.basename(p)}'\n" for p in parts))
subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', f'{D}/list.txt', '-c', 'copy', f'{D}/panel.mp4'], check=True)

# ---------- ASS ----------
def ts(x):
    x = max(0, x); h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    return f"{h}:{m:02d}:{s:05.2f}"
LIME = '&H004BEFCB&'; BLK = '&H00141414&'; CREAM = '&H00E6EFF2&'; RED = '&H003F50D9&'; ORG = '&H003D8AFF&'; BLUE = '&H00FF7B3D&'
hdr = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: H,Inter Display,78,{BLK},{BLK},{BLK},&H00000000,1,0,0,0,100,100,-1,0,1,0,0,8,50,50,150,1
Style: P,Inter Display,60,{BLK},{BLK},{LIME},{BLK},1,0,0,0,100,100,0,0,3,14,0,8,50,50,320,1
Style: C,Inter Display,52,{CREAM},{CREAM},{BLK},{BLK},1,0,0,0,100,100,0,0,3,16,0,2,80,80,520,1
Style: K,Inter Display,64,{BLK},{BLK},{BLK},&H00000000,1,0,0,0,100,100,-1,0,1,0,0,8,60,60,1590,1
Style: S,Inter Display,120,{BLK},{BLK},{LIME},{BLK},1,0,0,0,100,100,0,0,3,26,0,5,50,50,0,1
Style: F,Inter Display,60,&H00FFFFFF&,&H00FFFFFF&,&H00FFFFFF&,&H00000000,1,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
ev = []
def E(a, b, st, txt, layer=1): ev.append(f"Dialogue: {layer},{ts(a)},{ts(b)},{st},,0,0,0,,{txt}")
# headers
for a, b, l1, pill in cfg['headers']:
    E(a, b, 'H', r"{\fad(120,80)\t(0,250,\fscx100\fscy100)\fscx112\fscy112}" + l1)
    if pill: E(a + 0.15, b, 'P', r"{\fad(100,80)\fscx60\fscy60\t(0,220,\fscx100\fscy100)\frz-2}" + pill)
# cards on panel (bottom area of panel, stacked)
for c in cfg['cards']:
    a, b, txt = c[0], c[1], c[2]; col = c[3] if len(c) > 3 else 'lime'; y = c[4] if len(c) > 4 else 0
    cc = {'lime': LIME, 'blue': BLUE, 'org': ORG, 'red': RED, 'white': CREAM}[col]
    mv = 520 + y
    E(a, b, 'C', r"{\fad(80,120)\move(1300,%d,540,%d,0,260)\an2\1c%s}" % (1920 - mv, 1920 - mv, cc) + txt, 3)
# stamps (surprise)
for a, b, txt, col in cfg.get('stamps', []):
    cc = {'lime': LIME, 'red': RED}[col]
    fg = BLK if col == 'lime' else '&H00FFFFFF&'
    E(a, b, 'S', r"{\pos(540,960)\frz-6\3c%s\1c%s\fscx260\fscy260\t(0,180,\fscx100\fscy100)\fad(0,120)}" % (cc, fg) + txt, 4)
# counters
for a, dur, n0, n1, fmt, b in cfg.get('counters', []):
    steps = 14
    for k in range(steps):
        v = n0 + (n1 - n0) * (1 - (1 - (k + 1) / steps) ** 2)
        t0 = a + dur * k / steps; t1 = a + dur * (k + 1) / steps if k < steps - 1 else b
        E(t0, t1, 'S', r"{\pos(540,820)\3c%s\1c%s}" % (BLK, LIME) + fmt.format(f"{round(v):,}".replace(',', '.')), 4)
# flashes at scene cuts
for a, *_ in sc[1:]:
    E(a, a + 0.18, 'F', r"{\pos(0,0)\fad(0,160)\alpha&H70&\p1}m 0 0 l 1080 0 1080 1920 0 1920{\p0}", 5)
E(0, 0.3, 'F', r"{\pos(0,0)\fad(0,280)\alpha&H30&\p1}m 0 0 l 1080 0 1080 1920 0 1920{\p0}", 5)
# captions: groups of up to 3 words
groups = []; cur = []
for w in W:
    cur.append(w)
    if len(cur) == 3 or re.search(r'[,.?!:]$', w['w']): groups.append(cur); cur = []
if cur: groups.append(cur)
KEY = set(cfg.get('keys', []))
for gi, g in enumerate(groups):
    gend = groups[gi + 1][0]['s'] if gi + 1 < len(groups) else T
    for j, w in enumerate(g):
        a = w['s']; b = g[j + 1]['s'] if j + 1 < len(g) else gend
        txt = ''
        for k, x in enumerate(g):
            word = x['w']
            if k == j:
                txt += r"{\bord10\3c%s\fscx108\fscy108}%s{\bord0\fscx100\fscy100}" % (LIME, word)
            elif word.strip('.,?!:').lower() in KEY:
                txt += r"{\1c%s}%s{\1c%s}" % (RED, word, BLK)
            else:
                txt += word
            txt += ' '
        E(a, b, 'K', txt.strip(), 2)
# end screen handle
E(T - 4.2, T, 'P', r"{\pos(540,1480)\an5\fad(200,0)\3c&H00141414&\1c%s}@obolari_academy" % LIME, 6)
open(f'{D}/ov.ass', 'w').write(hdr + '\n'.join(ev) + '\n')

# ---------- SFX/music mix ----------
cuts = [a for a, *_ in sc[1:]]
inputs = ['-i', cfg['voice'], '-i', cfg['music'], '-i', '/home/user/unchainedlife-app/brand/sfx/impact.mp3']
flt = []; mix = ['[v]', '[m]', '[imp]']
flt.append('[0:a]aresample=44100,volume=1.0,asplit=2[v][vsc]')
flt.append(f"[1:a]aresample=44100,atrim=0:{T},volume=0.16,afade=t=in:d=1.5,afade=t=out:st={T-2.5}:d=2.5[m0]")
flt.append('[m0][vsc]sidechaincompress=threshold=0.04:ratio=6:attack=20:release=400[m]')
flt.append('[2:a]volume=0.35[imp]')
idx = 3
for k, c in enumerate(cuts):
    inputs += ['-i', '/home/user/unchainedlife-app/brand/sfx/whoosh.mp3']
    flt.append(f'[{idx}:a]volume=0.18,adelay={int(c*1000)-120}|{int(c*1000)-120}[w{k}]'); mix.append(f'[w{k}]'); idx += 1
for k, c in enumerate([x[0] for x in cfg['cards']] + [x[0] for x in cfg.get('stamps', [])]):
    snd = 'pop.mp3' if k < len(cfg['cards']) else 'impact.mp3'
    inputs += ['-i', f'/home/user/unchainedlife-app/brand/sfx/{snd}']
    flt.append(f'[{idx}:a]volume={0.16 if snd=="pop.mp3" else 0.3},adelay={int(c*1000)}|{int(c*1000)}[s{k}]'); mix.append(f'[s{k}]'); idx += 1
flt.append(''.join(mix) + f'amix=inputs={len(mix)}:normalize=0:duration=first,apad=whole_dur={T},atrim=0:{T},loudnorm=I=-14:TP=-1.5:LRA=11[a]')
open(f'{D}/af.txt', 'w').write(';\n'.join(flt))

# ---------- final render ----------
fc = (f"[1:v]format=yuva420p[pp];[2:v]format=gray[mk];[pp][mk]alphamerge[pm];[0:v][pm]overlay={PX}:{PY}:shortest=1,"
      f"ass={D}/ov.ass:fontsdir=/usr/share/fonts/opentype/inter,format=yuv420p[vout]")
cmd = ['ffmpeg', '-loglevel', 'error', '-y', '-loop', '1', '-framerate', '30', '-t', str(T), '-i', f'{D}/base.png', '-i', f'{D}/panel.mp4', '-loop', '1', '-i', f'{D}/mask.png'] + inputs + \
      ['-filter_complex', fc + ';' + ';'.join(f.replace('[0:a]', '[3:a]', 1) if False else f for f in []) , ]
# build audio separately for clarity
subprocess.run(['ffmpeg', '-loglevel', 'error', '-y'] + inputs + ['-filter_complex_script', f'{D}/af.txt', '-map', '[a]', '-c:a', 'pcm_s16le', f'{D}/mix.wav'], check=True)
subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-loop', '1', '-framerate', '30', '-t', str(T), '-i', f'{D}/base.png', '-i', f'{D}/panel.mp4', '-loop', '1', '-framerate', '30', '-t', str(T), '-i', f'{D}/mask.png', '-i', f'{D}/mix.wav',
                '-filter_complex', fc, '-map', '[vout]', '-map', '3:a', '-t', str(T), '-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-r', '30', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', f'{D}/reel.mp4'], check=True)
print('done', T)
