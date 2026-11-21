# Gerador dos Reels da série "um peptídeo por vídeo" (rotina madrugada 21/11/2026).
# Uso: python3 build.py <pasta> ; a pasta tem cfg.py, vwords.json, voz.wav e stock/.
import json, re, html, subprocess, sys, os, importlib.util
D = sys.argv[1]; os.chdir(D)
spec = importlib.util.spec_from_file_location('cfg', 'cfg.py'); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
T = C.T

# ---------- 1. fundo: painel nítido + mesmo clipe desfocado ----------
def bg():
    PW, PH = 1080, 1100
    for i, (a, b, c, off) in enumerate(C.SCENES):
        d = round(b - a, 3); src = f'stock/{c}.mp4'
        dur = float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',src],capture_output=True,text=True).stdout)
        loop = ['-stream_loop','-1'] if off + d > dur - 0.1 else []
        z = 'zoompan=z=\'min(1+0.0009*on,1.12)\':d=1:x=\'iw/2-(iw/zoom/2)\':y=\'ih/2-(ih/zoom/2)\':s=1080x1100:fps=30'
        fc = (f"[0:v]setpts=PTS-STARTPTS,fps=30,split[a][b];[a]crop=ih*{PW}/{PH}:ih,scale={PW}:{PH}:flags=lanczos,{z},unsharp=5:5:0.4,setsar=1[p];"
              f"[b]scale=-2:1920,crop=1080:1920,boxblur=30:3,eq=brightness=-0.22:saturation=0.8,setsar=1[bg];[bg][p]overlay=0:420,format=yuv420p")
        subprocess.run(['ffmpeg','-loglevel','error','-y',*loop,'-ss',str(off),'-t',str(d),'-i',src,'-filter_complex',fc,'-an','-c:v','libx264','-crf','17','-preset','veryfast','-r','30',f'sc_{i:02d}.mp4'],check=True)
    open('list.txt','w').write(''.join(f"file 'sc_{i:02d}.mp4'\n" for i in range(len(C.SCENES))))
    os.makedirs('hf/assets', exist_ok=True)
    subprocess.run(['ffmpeg','-loglevel','error','-y','-f','concat','-i','list.txt','-c','copy','hf/assets/bg.mp4'],check=True)

# ---------- 2. composição HTML ----------
def comp():
    W = json.load(open('vwords.json'))
    words = [{'w': C.REP.get(w['w'], w['w']), 's': w['s']} for w in W]
    groups, cur = [], []
    for w in words:
        cur.append(w)
        if len(cur) == 3 or re.search(r'[,.?!:]$', w['w']): groups.append(cur); cur = []
    if cur: groups.append(cur)
    caps, js = [], []
    for gi, g in enumerate(groups):
        a = g[0]['s']; b = groups[gi+1][0]['s'] if gi+1 < len(groups) else T - 0.1
        sp = ''.join(f'<span class="{"k" if re.sub(r"[,.?!:]","",w["w"]).lower() in C.KEY else ""}" id="c{gi}_{j}">{html.escape(w["w"])}</span> ' for j, w in enumerate(g))
        caps.append(f'<div id="cg{gi}" class="clip cap" data-start="{a:.2f}" data-duration="{b-a:.2f}"><div class="cb">{sp}</div></div>')
        for j, w in enumerate(g):
            js.append(f'tl.fromTo("#c{gi}_{j}",{{opacity:0.3}},{{opacity:1,duration:0.08}},{w["s"]:.2f});')
            js.append(f'tl.fromTo("#c{gi}_{j}",{{backgroundColor:"rgba(203,239,75,0)"}},{{backgroundColor:"rgba(203,239,75,1)",duration:0.05}},{w["s"]:.2f});')
            nxt = g[j+1]['s'] if j+1 < len(g) else b
            js.append(f'tl.to("#c{gi}_{j}",{{backgroundColor:"rgba(203,239,75,0)",duration:0.05}},{max(w["s"]+0.06,nxt-0.03):.2f});')
    hds = ''.join(f'<div id="h{i}" class="clip hd" data-start="{a}" data-duration="{round(b-a,2)}"><div class="m">{m}</div>{f"<div class=s>{s}</div>" if s else ""}</div>' for i, (a, b, m, s) in enumerate(C.HEADS))
    ovs = []
    for i, (a, b, items) in enumerate(C.OVER):
        inner = ''.join(f'<span class="pill" id="o{i}_{j}">{t}</span>' for j, (t, _) in enumerate(items))
        ovs.append(f'<div id="o{i}" class="clip ov" data-start="{a}" data-duration="{round(b-a,2)}"><div class="chips">{inner}</div></div>')
        for j, (t, ts) in enumerate(items):
            js.append(f'tl.fromTo("#o{i}_{j}",{{opacity:0,x:220}},{{opacity:1,x:0,duration:0.35,ease:"back.out(1.8)"}},{ts});')
    bigs = []
    for i, (a, b, txt, cnt) in enumerate(C.BIGS):
        bigs.append(f'<div id="g{i}" class="clip big" data-start="{a}" data-duration="{round(b-a,2)}"><span>{txt}</span></div>')
        js.append(f'tl.fromTo("#g{i} span",{{scale:2.4,opacity:0}},{{scale:1,opacity:1,duration:0.3,ease:"power4.out"}},{a});')
        js.append(f'tl.fromTo("#flash",{{opacity:0.55}},{{opacity:0,duration:0.25}},{a});')
        if cnt:
            n, ta = cnt
            js.append(f'tl.fromTo("#g{i}_n",{{textContent:0}},{{textContent:{n},duration:1.3,ease:"power2.out",snap:{{textContent:1}}}},{ta});')
    st = []
    for i, (a, b, txt) in enumerate(C.STAMPS):
        st.append(f'<div id="s{i}" class="clip stamp" data-start="{a}" data-duration="{round(b-a,2)}"><span>{txt}</span></div>')
        js.append(f'tl.fromTo("#s{i} span",{{scale:3,opacity:0}},{{scale:1,opacity:1,duration:0.25,ease:"power3.in"}},{a+0.03});')
        js.append(f'tl.fromTo("#bg",{{x:0}},{{x:-30,duration:0.05,yoyo:true,repeat:5}},{a});')
        js.append(f'tl.fromTo("#bg",{{filter:"grayscale(0) brightness(1)"}},{{filter:"grayscale(1) brightness(0.6)",duration:0.15}},{a});')
        js.append(f'tl.to("#bg",{{filter:"grayscale(0) brightness(1)",duration:0.2}},{b-0.2});')
        js.append(f'tl.fromTo("#flash",{{opacity:0.8}},{{opacity:0,duration:0.3}},{a});')
    for h in range(len(C.HEADS)):
        a = C.HEADS[h][0]
        js.append(f'tl.fromTo("#h{h}",{{y:30,opacity:0}},{{y:0,opacity:1,duration:0.3,ease:"power3.out"}},{a});')
    for s in C.SCENES[1:]:
        js.append(f'tl.fromTo("#flash",{{opacity:0.22}},{{opacity:0,duration:0.18}},{s[0]});')
        js.append(f'tl.fromTo("#bg",{{scale:1.14,filter:"blur(6px)"}},{{scale:1,filter:"blur(0px)",duration:0.45,ease:"power3.out"}},{s[0]});')
    js += C.EXTRA_JS
    cta_a = C.CTA
    H = f'''<!doctype html><html lang="pt-BR"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script><style>
@font-face{{font-family:"Bric";src:url("assets/Bric.ttf")}}
*{{margin:0;padding:0;box-sizing:border-box}}html,body{{width:1080px;height:1920px;overflow:hidden;background:#0E0E0E}}
#root{{position:relative;width:1080px;height:1920px;font-family:"Bric",sans-serif;font-weight:800;color:#fff;overflow:hidden}}
#bg{{position:absolute;inset:0;width:1080px;height:1920px;object-fit:cover;z-index:1}}
#tsh{{position:absolute;left:0;top:0;width:1080px;height:430px;z-index:3;background:rgba(0,0,0,.5)}} #bsh{{position:absolute;left:0;top:1500px;width:1080px;height:420px;z-index:3;background:rgba(0,0,0,.55)}}
#frame{{position:absolute;inset:26px;z-index:9;border:4px solid #CBEF4B;border-radius:34px;box-shadow:0 0 0 40px #0E0E0E}}
#tag{{position:absolute;z-index:9;top:80px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:16px;font-size:26px;letter-spacing:6px;font-family:"DejaVu Sans Mono",monospace;font-weight:700}}
#tag .d{{width:18px;height:18px;border-radius:50%;background:#CBEF4B;box-shadow:0 0 14px #CBEF4B}}#tag .c{{color:#CBEF4B}}
.hd{{position:absolute;z-index:6;left:50px;right:50px;top:150px;height:260px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}}
.hd .s{{font-size:42px;color:#F2EFE6;margin-top:10px}}
.hd .m{{font-size:78px;line-height:1.02;letter-spacing:-2px}} .hd span{{color:#CBEF4B}}
.cap{{position:absolute;z-index:6;left:50px;right:50px;top:1540px;text-align:center}}
.cb{{display:inline-block;background:#F2EFE6;color:#141414;border:4px solid #141414;border-radius:18px;padding:10px 18px;font-size:58px;line-height:1.15;box-shadow:8px 8px 0 #141414}}
.cb span{{padding:0 6px;border-radius:8px}} .cb .k{{color:#2E7D32}}
.ov{{position:absolute;z-index:5;left:50px;right:50px;top:1140px;text-align:center}}
.chips{{display:flex;flex-direction:column;gap:16px;align-items:center}}
.pill{{display:inline-block;background:rgba(14,14,14,.88);border:3px solid #CBEF4B;font-size:44px;padding:12px 28px;border-radius:18px}} .pill b{{color:#CBEF4B}}
.big{{position:absolute;z-index:6;left:0;right:0;top:820px;text-align:center}} .big span{{display:inline-block;font-size:150px;line-height:1;text-shadow:0 10px 40px rgba(0,0,0,.7);letter-spacing:-3px}} .big b{{color:#CBEF4B}}
.stamp{{position:absolute;z-index:7;left:0;right:0;top:820px;text-align:center}} .stamp span{{display:inline-block;background:#CBEF4B;color:#141414;font-size:120px;padding:6px 40px;border-radius:24px;transform:rotate(-4deg);box-shadow:0 20px 60px rgba(0,0,0,.6);white-space:nowrap}}
#flash{{position:absolute;inset:0;z-index:8;background:#fff;opacity:0}}
#cta{{position:absolute;z-index:6;left:0;right:0;top:1180px;text-align:center}} #cta span{{display:inline-block;background:#CBEF4B;color:#141414;font-size:54px;line-height:1.15;padding:18px 40px;max-width:900px;border-radius:60px;box-shadow:0 0 50px rgba(203,239,75,.6)}}
#handle{{position:absolute;z-index:6;left:0;right:0;top:1420px;text-align:center}} #handle span{{display:inline-block;background:#141414;color:#CBEF4B;font-size:40px;padding:10px 28px;border-radius:40px;border:3px solid #CBEF4B}}
#foot{{position:absolute;z-index:9;top:1810px;left:0;right:0;text-align:center;font-size:20px;letter-spacing:2px;color:rgba(255,255,255,.8);font-family:"DejaVu Sans Mono",monospace}}
#vs{{position:absolute;z-index:7;left:0;right:0;top:820px;text-align:center}} #vs span{{display:inline-block;background:#CBEF4B;color:#141414;font-size:118px;white-space:nowrap;padding:10px 40px;border-radius:28px;transform:rotate(-3deg);box-shadow:0 20px 60px rgba(0,0,0,.6)}}
{C.CSS}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{T}" data-width="1080" data-height="1920">
<video id="bg" class="clip" data-start="0" data-duration="{T}" src="assets/bg.mp4" muted></video>
<div id="tsh" class="clip" data-start="0" data-duration="{T}"></div><div id="bsh" class="clip" data-start="0" data-duration="{T}"></div>
<div id="vs" class="clip" data-start="0" data-duration="{C.VS_END}"><span>Você sabia? 🤔</span></div>
{hds}
{''.join(ovs)}
{''.join(bigs)}
{''.join(st)}
{C.HTML_EXTRA}
<div id="cta" class="clip" data-start="{cta_a}" data-duration="{round(T-cta_a,2)}"><span>Qual peptídeo eu explico no próximo? 💬</span></div>
<div id="handle" class="clip" data-start="{cta_a+0.4}" data-duration="{round(T-cta_a-0.4,2)}"><span>@obolari_academy</span></div>
{chr(10).join(caps)}
<div id="flash" class="clip" data-start="0" data-duration="{T}"></div>
<div id="frame" class="clip" data-start="0" data-duration="{T}"></div>
<div id="tag" class="clip" data-start="0" data-duration="{T}"><span class="d"></span>OBOLARI ACADEMY<span class="c">· PEPTÍDEOS · {C.SERIE}</span></div>
<div id="foot" class="clip" data-start="0" data-duration="{T}">CONTEÚDO EDUCATIVO · NÃO É RECOMENDAÇÃO MÉDICA</div>
</div><script>
window.__timelines=window.__timelines||{{}};
const tl=gsap.timeline({{paused:true}});
tl.set("#flash",{{opacity:0}},0);
tl.fromTo("#flash",{{opacity:0.6}},{{opacity:0,duration:0.25}},0);
tl.fromTo("#vs span",{{scale:2.6,opacity:0}},{{scale:1,opacity:1,duration:0.3,ease:"power4.out"}},0.02);
tl.to("#vs",{{opacity:0,y:-40,duration:0.15}},{C.VS_END-0.15});
tl.fromTo("#cta span",{{scale:0.6,opacity:0}},{{scale:1,opacity:1,duration:0.4,ease:"back.out(2.2)"}},{cta_a});
tl.to("#cta span",{{scale:1.05,duration:0.45,yoyo:true,repeat:3,ease:"sine.inOut"}},{cta_a+0.5});
tl.fromTo("#handle span",{{y:40,opacity:0}},{{y:0,opacity:1,duration:0.3}},{cta_a+0.4});
{chr(10).join(js)}
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
    os.makedirs('hf/assets', exist_ok=True)
    open('hf/index.html', 'w').write(H)
    subprocess.run(['cp', '../_shared/Bric.ttf', 'hf/assets/Bric.ttf'])
    print('comp ok', len(groups))

# ---------- 3. áudio: voz + música com ducking + SFX ----------
def audio():
    sfx = '../../brand/sfx/'
    cues = [(s[0], 'whoosh', 0.22) for s in C.SCENES[1:]]
    cues += [(ts, 'pop', 0.35) for (_, _, items) in C.OVER for (_, ts) in items]
    cues += [(a, 'impact', 0.5) for (a, _, _) in C.STAMPS] + [(0.0, 'impact', 0.45)]
    cues += [(a, 'ding', 0.35) for (a, _, _, _) in C.BIGS]
    cues.sort()
    ins = ['-i', 'voz.wav', '-stream_loop', '-1', '-i', f'../_shared/{C.MUSIC}']
    fc = []
    for i, (t, n, v) in enumerate(cues):
        ins += ['-i', f'{sfx}{n}.mp3']
        fc.append(f'[{i+2}:a]volume={v},adelay={int(t*1000)}|{int(t*1000)}[x{i}]')
    fc.append(f'[1:a]atrim=0:{T},volume=0.22,afade=t=in:d=1.5,afade=t=out:st={T-2.5}:d=2.5[mu]')
    fc.append('[0:a]asplit[v1][v2]')
    fc.append('[mu][v2]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[md]')
    fc.append(''.join(f'[x{i}]' for i in range(len(cues))) + f'amix=inputs={len(cues)}:normalize=0[sx]')
    fc.append(f'[v1][md][sx]amix=inputs=3:normalize=0,apad,atrim=0:{T},loudnorm=I=-14:TP=-1[out]')
    subprocess.run(['ffmpeg','-loglevel','error','-y',*ins,'-filter_complex',';'.join(fc),'-map','[out]','-ar','48000','-c:a','pcm_s16le','mix.wav'],check=True)
    print('audio ok', len(cues))

for step in sys.argv[2:] or ['bg', 'comp', 'audio']:
    globals()[step]()
