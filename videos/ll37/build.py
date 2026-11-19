# Gerador compartilhado dos Reels da série "um peptídeo por vídeo" (19/11/2026).
# Uso: python3 build.py <pasta_do_video>   (a pasta tem cfg.py, voz.wav, vwords.json)
import json, re, html, subprocess, sys, os, importlib.util
D = os.path.abspath(sys.argv[1]); os.chdir(D)
spec = importlib.util.spec_from_file_location('cfg', 'cfg.py'); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
STOCK = '/tmp/stock'; os.makedirs('hf/assets/fonts', exist_ok=True)
for f in ['Bricolage-700.ttf', 'Bricolage-800.ttf']:
    subprocess.run(['cp', f'/tmp/hfa/fonts/{f}', 'hf/assets/fonts/'], check=True)
T = C.T

# ---------- fundo: painel nítido + mesmo clipe desfocado ----------
if not os.path.exists('hf/assets/bg.mp4') or '--bg' in sys.argv:
    PW, PH = 1080, 1100; parts = []
    for i, (a, b, c, off) in enumerate(C.SCENES):
        d = round(b - a, 3); src = f'{STOCK}/{c}.mp4'
        w, h = map(int, subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v', '-show_entries', 'stream=width,height', '-of', 'csv=p=0', src], capture_output=True, text=True).stdout.strip().split(','))
        panel = f'scale={PW}:-2,crop={PW}:{PH}' if h > w else f'scale=-2:{PH},crop={PW}:{PH}'
        # zoom de entrada 1.22 -> 1 em 0.4 s + deriva lenta
        z = f"zoompan=z='if(lt(on,12),1.22-0.22*on/12,1+0.0006*(on-12))':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={PW}x{PH}:fps=30"
        fc = (f"[0:v]setpts=PTS-STARTPTS,fps=30,split[a][b];[a]{panel},{z},setsar=1[p];"
              f"[b]scale=-2:1920,crop=1080:1920,boxblur=30:3,eq=brightness=-0.2:saturation=0.8,setsar=1[bg];[bg][p]overlay=0:420,format=yuv420p")
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-stream_loop', '-1', '-ss', str(off), '-t', str(d), '-i', src, '-filter_complex', fc, '-an', '-r', '30', '-c:v', 'libx264', '-crf', '17', '-preset', 'veryfast', f'/tmp/sc_{os.path.basename(D)}_{i:02d}.mp4'], check=True)
        parts.append(f"file '/tmp/sc_{os.path.basename(D)}_{i:02d}.mp4'\n")
    open('/tmp/list_%s.txt' % os.path.basename(D), 'w').write(''.join(parts))
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', '/tmp/list_%s.txt' % os.path.basename(D), '-c', 'copy', 'hf/assets/bg.mp4'], check=True)
    print('bg ok')

# ---------- legendas palavra a palavra ----------
W = json.load(open('vwords.json'))
words = []
P = getattr(C, 'PAIRS', {})
i = 0; W2 = []
while i < len(W):
    if i + 1 < len(W) and (W[i]['w'], W[i+1]['w']) in P:
        W2.append({'w': P[(W[i]['w'], W[i+1]['w'])], 's': W[i]['s']}); i += 2
    else: W2.append(W[i]); i += 1
for w in W2:
    t = C.REP.get(w['w'], w['w'])
    if t == '' : continue
    if words and t.startswith('+'): words[-1]['w'] += t[1:]; continue
    words.append({'w': t, 's': w['s']})
groups = []; cur = []
for w in words:
    cur.append(w)
    if len(cur) == 3 or re.search(r'[,.?!:]$', w['w']): groups.append(cur); cur = []
if cur: groups.append(cur)
norm = lambda s: re.sub(r'[^\wÀ-ú%-]', '', s).lower()
KEY = {norm(k) for k in C.KEY}
caps = []; js = []
for gi, g in enumerate(groups):
    a = g[0]['s']; b = groups[gi + 1][0]['s'] if gi + 1 < len(groups) else T - 0.1
    spans = ''.join(f'<span class="{"k" if norm(w["w"]) in KEY else ""}" id="c{gi}_{j}">{html.escape(w["w"])}</span> ' for j, w in enumerate(g))
    caps.append(f'<div id="cg{gi}" class="clip cap" data-start="{a:.2f}" data-duration="{max(0.1,b-a):.2f}">{spans}</div>')
    for j, w in enumerate(g): js.append(f'tl.fromTo("#c{gi}_{j}",{{opacity:0.25,y:8}},{{opacity:1,y:0,duration:0.12}},{w["s"]:.2f});')

def hd(id, a, b, inner): return f'<div id="{id}" class="clip hd" data-start="{a}" data-duration="{round(b-a,2)}">{inner}</div>'
body = []
for i, (a, b, inner) in enumerate(C.HEADS): body.append(hd(f'h{i}', a, b, inner))
for i, (a, b, items, top) in enumerate(C.OVS):
    pills = ''.join(f'<span class="pill{" v" if it[1].startswith("!") else ""}" id="o{i}_{j}">{it[1].lstrip("!")}</span>' for j, it in enumerate(items))
    body.append(f'<div class="clip ov" data-start="{a}" data-duration="{round(b-a,2)}" style="top:{top}px"><div class="chips">{pills}</div></div>')
    for j, it in enumerate(items): js.append(f'tl.fromTo("#o{i}_{j}",{{opacity:0,x:200}},{{opacity:1,x:0,duration:0.35,ease:"back.out(1.8)"}},{it[0]});')
for i, (a, b, txt, top, size) in enumerate(C.BIGS):
    body.append(f'<div id="bg{i}" class="clip ov" data-start="{a}" data-duration="{round(b-a,2)}" style="top:{top}px"><div class="big" style="font-size:{size}px">{txt}</div></div>')
    js.append(f'tl.fromTo("#bg{i} .big",{{scale:2.2,opacity:0}},{{scale:1,opacity:1,duration:0.3,ease:"power4.out"}},{a});')
for (sel, a, dur, frm, to) in C.COUNTERS:
    js.append(f'tl.fromTo("{sel}",{{textContent:{frm}}},{{textContent:{to},duration:{dur},ease:"power2.out",snap:{{textContent:1}}}},{a});')
# contas de colar (aminoácidos)
if C.BEADS:
    a, b, n = C.BEADS
    cols = ['#CBEF4B', '#F4C430', '#4FC3F7', '#B388FF', '#FF8A65']
    beads = ''.join(f'<i id="bd{i}" style="background:{cols[i%5]}"></i>' for i in range(n))
    body.append(f'<div class="clip ov" data-start="{a}" data-duration="{round(b-a,2)}" style="top:1150px"><div class="beads">{beads}</div></div>')
    for i in range(n): js.append(f'tl.fromTo("#bd{i}",{{scale:0}},{{scale:1,duration:0.18,ease:"back.out(3)"}},{a+0.1+i*min(0.08,2.0/n):.2f});')
# carimbo surpresa (freeze)
sa, stxt = C.STAMP
body.append(f'<div id="stamp" class="clip" data-start="{sa}" data-duration="1.3"><span>{stxt}</span></div>')
H = f'''<!doctype html><html lang="pt-BR"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script><style>
@font-face{{font-family:"Bric";src:url("assets/fonts/Bricolage-800.ttf");font-weight:800}}
@font-face{{font-family:"Bric";src:url("assets/fonts/Bricolage-700.ttf");font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}html,body{{width:1080px;height:1920px;overflow:hidden;background:#0E0E0E}}
#root{{position:relative;width:1080px;height:1920px;font-family:"Bric",sans-serif;color:#fff;overflow:hidden}}
#bgv{{position:absolute;inset:0;width:1080px;height:1920px;object-fit:cover;z-index:1}}
#shade{{position:absolute;left:0;top:420px;width:1080px;height:1100px;z-index:2;background:linear-gradient(rgba(0,0,0,0) 55%,rgba(0,0,0,.6) 100%)}}
#tsh{{position:absolute;left:0;top:0;width:1080px;height:430px;z-index:3;background:rgba(0,0,0,.55)}} #bsh{{position:absolute;left:0;top:1520px;width:1080px;height:400px;z-index:3;background:rgba(0,0,0,.6)}}
#frame{{position:absolute;inset:26px;z-index:9;border:4px solid #CBEF4B;border-radius:34px;box-shadow:0 0 0 40px #0E0E0E}}
#tag{{position:absolute;z-index:9;top:80px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:16px;font-weight:700;font-size:26px;letter-spacing:8px}}
#tag .d{{width:18px;height:18px;border-radius:50%;background:#CBEF4B;box-shadow:0 0 14px #CBEF4B}}#tag .c{{color:#CBEF4B}}
.hd{{position:absolute;z-index:6;left:40px;right:40px;top:150px;height:260px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}}
.hd .s{{font-weight:700;font-size:42px;color:#F2EFE6}}
.hd .m{{font-weight:800;font-size:78px;line-height:1.02;letter-spacing:-2px}}
.hd .m span,.hd .s span{{color:#CBEF4B}}
.cap{{position:absolute;z-index:6;left:60px;right:60px;top:1555px;text-align:center;font-weight:800;font-size:60px;line-height:1.1;letter-spacing:-1px;text-shadow:0 4px 18px rgba(0,0,0,.8)}}
.cap .k{{color:#CBEF4B}}
.ov{{position:absolute;z-index:5;left:60px;right:60px;top:1200px;text-align:center}}
.chips{{display:flex;flex-direction:column;gap:16px;align-items:center}}
.pill{{display:inline-block;background:rgba(14,14,14,.86);border:3px solid #CBEF4B;font-weight:800;font-size:44px;padding:12px 28px;border-radius:18px}}
.pill b{{color:#CBEF4B}} .pill.v{{border-color:#B388FF}} .pill.v b{{color:#B388FF}}
.big{{font-weight:800;font-size:150px;line-height:1;text-shadow:0 10px 40px rgba(0,0,0,.7)}} .big b{{color:#CBEF4B}}
.beads{{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;background:rgba(14,14,14,.82);padding:18px;border-radius:22px;max-width:820px;margin:0 auto}} .beads i{{display:block;width:58px;height:58px;border-radius:50%;box-shadow:inset -6px -6px 0 rgba(0,0,0,.2)}}
#stamp{{position:absolute;z-index:7;left:0;right:0;top:820px;text-align:center}}
#stamp span{{display:inline-block;background:#CBEF4B;color:#141414;font-weight:800;font-size:130px;padding:6px 40px;border-radius:24px;transform:rotate(-4deg);box-shadow:0 20px 60px rgba(0,0,0,.6)}}
#vs{{position:absolute;z-index:7;left:0;right:0;top:820px;text-align:center}}
#vs span{{display:inline-block;background:#CBEF4B;color:#141414;font-weight:800;font-size:118px;white-space:nowrap;padding:10px 40px;border-radius:28px;transform:rotate(-3deg);box-shadow:0 20px 60px rgba(0,0,0,.6)}}
#flash{{position:absolute;inset:0;z-index:8;background:#fff;opacity:0}}
#cta{{position:absolute;z-index:6;left:0;right:0;top:1230px;text-align:center}}
#cta span{{display:inline-block;background:#CBEF4B;color:#141414;font-weight:800;font-size:60px;padding:18px 46px;border-radius:60px;box-shadow:0 0 50px rgba(203,239,75,.6)}}
#handle{{position:absolute;z-index:6;left:0;right:0;top:1380px;text-align:center}}
#handle span{{display:inline-block;background:#141414;color:#CBEF4B;font-weight:700;font-size:34px;padding:10px 30px;border-radius:40px;border:2px solid #CBEF4B}}
#foot{{position:absolute;z-index:9;top:1800px;left:0;right:0;text-align:center;font-weight:700;font-size:20px;letter-spacing:2px;color:rgba(255,255,255,.75)}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{T}" data-width="1080" data-height="1920">
<video id="bgv" class="clip" data-start="0" data-duration="{T}" src="assets/bg.mp4" muted></video>
<div id="shade" class="clip" data-start="0" data-duration="{T}"></div>
<div id="tsh" class="clip" data-start="0" data-duration="{T}"></div><div id="bsh" class="clip" data-start="0" data-duration="{T}"></div>
<div id="vs" class="clip" data-start="0" data-duration="1.1"><span>Você sabia? 🤔</span></div>
{chr(10).join(body)}
<div id="cta" class="clip" data-start="{C.CTA}" data-duration="{round(T-C.CTA,2)}"><span>{C.CTA_TXT}</span></div>
<div id="handle" class="clip" data-start="{C.CTA}" data-duration="{round(T-C.CTA,2)}"><span>@obolari_academy</span></div>
{chr(10).join(caps)}
<div id="flash" class="clip" data-start="0" data-duration="{T}"></div>
<div id="frame" class="clip" data-start="0" data-duration="{T}"></div>
<div id="tag" class="clip" data-start="0" data-duration="{T}"><span class="d"></span>OBOLARI ACADEMY<span class="c">· {C.SERIES}</span></div>
<div id="foot" class="clip" data-start="0" data-duration="{T}">@OBOLARI_ACADEMY · CONTEÚDO EDUCATIVO · NÃO É RECOMENDAÇÃO MÉDICA</div>
</div><script>
const tl=gsap.timeline({{paused:true}});
tl.set("#flash",{{opacity:0}},0);
tl.fromTo("#flash",{{opacity:0.6}},{{opacity:0,duration:0.25}},0);
tl.fromTo("#vs span",{{scale:2.6,opacity:0}},{{scale:1,opacity:1,duration:0.3,ease:"power4.out"}},0.02);
tl.to("#vs",{{opacity:0,y:-40,duration:0.15}},0.95);
'''
for i, (a, b, inner) in enumerate(C.HEADS):
    H += f'tl.fromTo("#h{i}",{{y:30,opacity:0}},{{y:0,opacity:1,duration:0.3,ease:"power3.out"}},{a});\n'
for (a, b, c, off) in C.SCENES[1:]:
    if abs(a - sa) > 0.05: H += f'tl.fromTo("#flash",{{opacity:0.22}},{{opacity:0,duration:0.18}},{a});\n'
for t in C.PUNCH:  # punch-in de ~9% nas palavras de impacto
    H += f'tl.fromTo("#bgv",{{scale:1.09}},{{scale:1,duration:0.45,ease:"power2.out"}},{t});\n'
H += f'''tl.fromTo("#bgv",{{x:0}},{{x:-30,duration:0.05,yoyo:true,repeat:5}},{sa});
tl.fromTo("#bgv",{{filter:"grayscale(0) brightness(1)"}},{{filter:"grayscale(1) brightness(0.55)",duration:0.15}},{sa});
tl.to("#bgv",{{filter:"grayscale(0) brightness(1)",duration:0.2}},{sa+1.2});
tl.fromTo("#flash",{{opacity:0.8}},{{opacity:0,duration:0.3}},{sa});
tl.fromTo("#stamp span",{{scale:3,opacity:0}},{{scale:1,opacity:1,duration:0.25,ease:"power3.in"}},{sa+0.05});
tl.fromTo("#cta span",{{scale:0.6,opacity:0}},{{scale:1,opacity:1,duration:0.4,ease:"back.out(2.2)"}},{C.CTA});
tl.fromTo("#handle span",{{y:40,opacity:0}},{{y:0,opacity:1,duration:0.35}},{C.CTA+0.3});
tl.to("#cta span",{{scale:1.06,duration:0.45,yoyo:true,repeat:3,ease:"sine.inOut"}},{C.CTA+0.5});
''' + '\n'.join(js) + '''
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
open('hf/index.html', 'w').write(H); print('html ok', len(groups))

# ---------- áudio: voz + música baixinha com ducking + SFX ----------
sfx = '/home/user/unchainedlife-app/brand/sfx'
cues = [(0.0, 'impact', 0.5), (sa, 'impact', 0.55)] + [(a, 'whoosh', 0.22) for (a, b, c, o) in C.SCENES[1:] if abs(a - sa) > 0.05]
cues += [(it[0], 'pop', 0.25) for (_, _, items, _) in C.OVS for it in items] + [(a, 'ding', 0.3) for (a, *_r) in C.BIGS] + [(C.CTA, 'ding', 0.35)]
inp = ['-i', 'voz.wav', '-stream_loop', '-1', '-i', C.MUSIC]
fl = [f'[1:a]atrim=0:{T},afade=t=in:d=1.5,afade=t=out:st={T-2.5}:d=2.5,volume=0.22[m]', '[0:a]asplit=2[v1][v2]', '[m][v2]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=300[md]']
mix = ['[v1]', '[md]']
for k, (t, n, vol) in enumerate(cues):
    inp += ['-i', f'{sfx}/{n}.mp3']; idx = k + 2
    fl.append(f'[{idx}:a]volume={vol},adelay={int(t*1000)}|{int(t*1000)}[s{k}]'); mix.append(f'[s{k}]')
fl.append(''.join(mix) + f'amix=inputs={len(mix)}:normalize=0:duration=first,atrim=0:{T},loudnorm=I=-14:TP=-1.0:LRA=11[out]')
subprocess.run(['ffmpeg', '-loglevel', 'error', '-y'] + inp + ['-filter_complex', ';'.join(fl), '-map', '[out]', '-ar', '48000', 'mix.wav'], check=True)
print('mix ok')
