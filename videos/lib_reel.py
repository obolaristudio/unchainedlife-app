# Montagem padrão dos Reels de peptídeo (painel 1080x1100 nítido + fundo desfocado,
# cards da marca, legenda palavra a palavra, carimbo surpresa, contador, CTA).
# Uso: from lib_reel import build_bg, build_html  (ver videos/argireline/gen.py)
import subprocess, json, re, html, os

PW, PH = 1080, 1100


def build_bg(scenes, stock, out_dir):
    """scenes: [[ini, fim, id_mixkit, offset, centro_x|None], ...]"""
    parts = []
    for i, (a, b, c, off, cx) in enumerate(scenes):
        d = round(b - a, 3); src = f'{stock}/{c}.mp4'
        w, h = map(int, subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v', '-show_entries',
                                        'stream=width,height', '-of', 'csv=p=0', src],
                                       capture_output=True, text=True).stdout.strip().split(','))
        if cx is None or h > w:
            panel = f'scale={PW}:-2,crop={PW}:{PH}'
        else:
            cw = round(h * PW / PH); x = int(max(0, min(w - cw, w * cx - cw / 2)))
            panel = f'crop={cw}:{h}:{x}:0,scale={PW}:{PH}:flags=lanczos,unsharp=5:5:0.5'
        # deriva lenta de zoom dentro da cena (padrão Maxwell)
        zoom = f",zoompan=z='min(1+0.0009*on,1.06)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={PW}x{PH}:fps=30"
        fc = (f"[0:v]setpts=PTS-STARTPTS,fps=30,split[a][b];[a]{panel}{zoom},setsar=1[p];"
              f"[b]scale=-2:1920,crop=1080:1920,boxblur=30:3,eq=brightness=-0.2:saturation=0.8,setsar=1[bg];"
              f"[bg][p]overlay=0:420,format=yuv420p")
        o = f'{out_dir}/sc_{i:02d}.mp4'
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-ss', str(off), '-t', str(d), '-i', src,
                        '-filter_complex', fc, '-an', '-c:v', 'libx264', '-crf', '16', '-preset', 'veryfast',
                        '-r', '30', o], check=True)
        parts.append(o)
    open(f'{out_dir}/list.txt', 'w').write(''.join(f"file '{p}'\n" for p in parts))
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', f'{out_dir}/list.txt',
                    '-c', 'copy', f'{out_dir}/bg.mp4'], check=True)


def caption_groups(W, rep, merges=()):
    words = []; skip = set()
    for i, w in enumerate(W):
        if i in skip: continue
        t = rep.get(w['w'], w['w'])
        n = W[i + 1]['w'] if i + 1 < len(W) else ''
        for (x, y, z) in merges:
            if t == x and n == y: t = z; skip.add(i + 1)
        words.append({'w': t, 's': w['s']})
    groups = []; cur = []
    for w in words:
        cur.append(w)
        if len(cur) == 3 or re.search(r'[,.?!:]$', w['w']): groups.append(cur); cur = []
    if cur: groups.append(cur)
    return groups


CSS = '''
@font-face{font-family:"Bric";src:url("assets/fonts/Bricolage-800.ttf");font-weight:800}
@font-face{font-family:"Bric";src:url("assets/fonts/Bricolage-700.ttf");font-weight:700}
*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1920px;overflow:hidden;background:#0E0E0E}
#root{position:relative;width:1080px;height:1920px;font-family:"Bric",sans-serif;color:#fff;overflow:hidden}
#bg{position:absolute;inset:0;width:1080px;height:1920px;object-fit:cover;z-index:1}
#shade{position:absolute;left:0;top:420px;width:1080px;height:1100px;z-index:2;background:linear-gradient(rgba(0,0,0,0) 55%,rgba(0,0,0,.6) 100%)}
#tsh{position:absolute;left:0;top:0;width:1080px;height:430px;z-index:3;background:rgba(0,0,0,.55)} #bsh{position:absolute;left:0;top:1520px;width:1080px;height:400px;z-index:3;background:rgba(0,0,0,.6)}
#frame{position:absolute;inset:26px;z-index:9;border:4px solid #CBEF4B;border-radius:34px;box-shadow:0 0 0 40px #0E0E0E}
#tag{position:absolute;z-index:9;top:80px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:16px;font-weight:700;font-size:26px;letter-spacing:8px}
#tag .d{width:18px;height:18px;border-radius:50%;background:#CBEF4B;box-shadow:0 0 14px #CBEF4B}#tag .c{color:#CBEF4B}
.hd{position:absolute;z-index:6;left:40px;right:40px;top:150px;height:260px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.hd .s{font-weight:700;font-size:42px;color:#F2EFE6}
.hd .m{font-weight:800;font-size:80px;line-height:1;letter-spacing:-2px}
.hd .m span,.hd .s span{color:#CBEF4B}
.cap{position:absolute;z-index:6;left:60px;right:60px;top:1555px;text-align:center;font-weight:800;font-size:60px;line-height:1.1;letter-spacing:-1px;text-shadow:0 4px 18px rgba(0,0,0,.8)}
.cap .k{color:#141414;background:#CBEF4B;padding:0 10px;border-radius:10px;text-shadow:none}
.ov{position:absolute;z-index:5;left:60px;right:60px;top:1200px;text-align:center}
.pill{display:inline-block;background:rgba(14,14,14,.86);border:3px solid #CBEF4B;font-weight:800;font-size:44px;padding:12px 28px;border-radius:18px}
.pill b{color:#CBEF4B} .pill.v{border-color:#B388FF} .pill.v b{color:#B388FF}
.big{font-weight:800;font-size:150px;line-height:1;text-shadow:0 10px 40px rgba(0,0,0,.6)} .big span{color:#CBEF4B}
.chips{display:flex;flex-direction:column;gap:16px;align-items:center}
.beads{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;background:rgba(14,14,14,.82);padding:18px;border-radius:22px;max-width:900px;margin:0 auto}
.beads i{display:block;width:62px;height:62px;border-radius:50%;box-shadow:inset -6px -6px 0 rgba(0,0,0,.2)}
.stamp{position:absolute;z-index:7;left:0;right:0;top:820px;text-align:center}
.stamp span{display:inline-block;background:#CBEF4B;color:#141414;font-weight:800;font-size:150px;padding:6px 40px;border-radius:24px;transform:rotate(-4deg);box-shadow:0 20px 60px rgba(0,0,0,.6)}
.stamp.r span{background:#141414;color:#fff;border:8px solid #E53935}
#flash{position:absolute;inset:0;z-index:8;background:#fff;opacity:0}
#cta{position:absolute;z-index:6;left:0;right:0;top:1230px;text-align:center}
#cta span{display:inline-block;background:#CBEF4B;color:#141414;font-weight:800;font-size:62px;padding:18px 46px;border-radius:60px;box-shadow:0 0 50px rgba(203,239,75,.6)}
#foot{position:absolute;z-index:9;top:1800px;left:0;right:0;text-align:center;font-weight:700;font-size:20px;letter-spacing:2px;color:rgba(255,255,255,.75)}
'''

BEAD_COLORS = ['#E53935', '#F4C430', '#CBEF4B', '#4FC3F7', '#B388FF']


def build_html(cfg, out_path):
    T = cfg['T']; groups = cfg['groups']; KEY = cfg['key']
    caps = []; js = []
    for gi, g in enumerate(groups):
        a = g[0]['s']; b = groups[gi + 1][0]['s'] if gi + 1 < len(groups) else T - 0.1
        spans = ''.join(f'<span class="{"k" if re.sub(r"[,.?!:]$", "", w["w"]).lower() in KEY else ""}" id="c{gi}_{j}">{html.escape(w["w"])}</span> ' for j, w in enumerate(g))
        caps.append(f'<div id="cg{gi}" class="clip cap" data-start="{a:.2f}" data-duration="{b - a:.2f}">{spans}</div>')
        for j, w in enumerate(g):
            js.append(f'tl.fromTo("#c{gi}_{j}",{{opacity:0.25,y:8}},{{opacity:1,y:0,duration:0.12}},{w["s"]:.2f});')
    body = []
    for (hid, a, b, inner) in cfg['heads']:
        body.append(f'<div id="{hid}" class="clip hd" data-start="{a}" data-duration="{round(b - a, 2)}">{inner}</div>')
        js.append(f'tl.fromTo("#{hid}",{{y:30,opacity:0,scale:1.15}},{{y:0,opacity:1,scale:1,duration:0.32,ease:"power3.out"}},{a});')
    for (oid, a, b, inner, top, pops) in cfg['ovs']:
        body.append(f'<div id="{oid}" class="clip ov" data-start="{a}" data-duration="{round(b - a, 2)}" style="top:{top}px">{inner}</div>')
        if not pops:
            js.append(f'tl.fromTo("#{oid}",{{opacity:0,scale:0.7}},{{opacity:1,scale:1,duration:0.3,ease:"back.out(2)"}},{a});')
        for (sel, t, kind) in pops:
            if kind == 'slide':
                js.append(f'tl.fromTo("{sel}",{{opacity:0,x:200}},{{opacity:1,x:0,duration:0.35,ease:"back.out(1.8)"}},{t});')
            elif kind == 'slam':
                js.append(f'tl.fromTo("{sel}",{{scale:2.4,opacity:0}},{{scale:1,opacity:1,duration:0.35,ease:"power4.out"}},{t});')
                js.append(f'tl.fromTo("#flash",{{opacity:0.5}},{{opacity:0,duration:0.25}},{t});')
            elif kind == 'beads':
                n = int(sel)
                for i in range(n):
                    js.append(f'tl.fromTo("#{oid} i:nth-child({i + 1})",{{scale:0}},{{scale:1,duration:0.16,ease:"back.out(3)"}},{t + i * 0.07:.2f});')
            elif kind.startswith('count:'):
                js.append(f'tl.fromTo("{sel}",{{textContent:0}},{{textContent:{kind[6:]},duration:1.1,ease:"power2.out",snap:{{textContent:1}}}},{t});')
            elif kind == 'fade':
                js.append(f'tl.fromTo("{sel}",{{opacity:0,y:20}},{{opacity:1,y:0,duration:0.3}},{t});')
    for (sid, a, b, text, red) in cfg['stamps']:
        body.append(f'<div id="{sid}" class="clip stamp{" r" if red else ""}" data-start="{a}" data-duration="{round(b - a, 2)}"><span>{text}</span></div>')
        js.append(f'tl.fromTo("#{sid} span",{{scale:3,opacity:0}},{{scale:1,opacity:1,duration:0.25,ease:"power3.in"}},{a + 0.05});')
        js.append(f'tl.fromTo("#flash",{{opacity:0.8}},{{opacity:0,duration:0.3}},{a});')
        js.append(f'tl.fromTo("#bg",{{x:0}},{{x:-28,duration:0.05,yoyo:true,repeat:5}},{a});')
        js.append(f'tl.fromTo("#bg",{{filter:"grayscale(0) brightness(1)"}},{{filter:"grayscale(1) brightness(0.6)",duration:0.15}},{a});')
        js.append(f'tl.to("#bg",{{filter:"grayscale(0) brightness(1)",duration:0.2}},{b - 0.1});')
    for s_ in cfg['scenes'][1:]:
        if s_[0] not in [st[1] for st in cfg['stamps']]:
            js.append(f'tl.fromTo("#flash",{{opacity:0.28}},{{opacity:0,duration:0.18}},{s_[0]});')
    for t in cfg.get('punch', []):
        js.append(f'tl.fromTo("#bg",{{scale:1}},{{scale:1.09,duration:0.12,yoyo:true,repeat:1,ease:"power2.out"}},{t});')
    ca = cfg['cta_at']
    body.append(f'<div id="cta" class="clip" data-start="{ca}" data-duration="{round(T - ca, 2)}"><span>{cfg["cta"]}</span></div>')
    js.append(f'tl.fromTo("#cta span",{{scale:0.6,opacity:0}},{{scale:1,opacity:1,duration:0.4,ease:"back.out(2.2)"}},{ca});')
    js.append(f'tl.to("#cta span",{{scale:1.06,duration:0.45,yoyo:true,repeat:3,ease:"sine.inOut"}},{ca + 0.5});')
    H = f'''<!doctype html><html lang="pt-BR"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script><style>{CSS}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{T}" data-width="1080" data-height="1920">
<video id="bg" class="clip" data-start="0" data-duration="{T}" src="assets/bg.mp4" muted></video>
<div id="shade" class="clip" data-start="0" data-duration="{T}"></div>
<div id="tsh" class="clip" data-start="0" data-duration="{T}"></div><div id="bsh" class="clip" data-start="0" data-duration="{T}"></div>
{chr(10).join(body)}
{chr(10).join(caps)}
<div id="flash" class="clip" data-start="0" data-duration="{T}"></div>
<div id="frame" class="clip" data-start="0" data-duration="{T}"></div>
<div id="tag" class="clip" data-start="0" data-duration="{T}"><span class="d"></span>OBOLARI ACADEMY<span class="c">· {cfg["serie"]}</span></div>
<div id="foot" class="clip" data-start="0" data-duration="{T}">@OBOLARI_ACADEMY · CONTEÚDO EDUCATIVO · NÃO É RECOMENDAÇÃO MÉDICA</div>
</div><script>
window.__timelines=window.__timelines||{{}};
const tl=gsap.timeline({{paused:true}});
tl.set("#flash",{{opacity:0}},0);
{chr(10).join(js)}
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    open(out_path, 'w').write(H)


def beads(n):
    return '<div class="beads">' + ''.join(f'<i style="background:{BEAD_COLORS[i % 5]}"></i>' for i in range(n)) + '</div>'
