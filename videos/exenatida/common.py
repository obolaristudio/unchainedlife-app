import json,re,html,os,shutil
CSS='''@font-face{font-family:"Bric";src:url("assets/Bric-Bold.ttf");font-weight:800}
*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1920px;overflow:hidden;background:#0E0E0E}
#root{position:relative;width:1080px;height:1920px;font-family:"Bric",sans-serif;font-weight:800;color:#fff;overflow:hidden}
#bg{position:absolute;inset:0;width:1080px;height:1920px;object-fit:cover;z-index:1}
#shade{position:absolute;left:0;top:420px;width:1080px;height:1100px;z-index:2;background:linear-gradient(rgba(0,0,0,0) 55%,rgba(0,0,0,.6) 100%)}
#tsh{position:absolute;left:0;top:0;width:1080px;height:430px;z-index:3;background:rgba(0,0,0,.55)} #bsh{position:absolute;left:0;top:1520px;width:1080px;height:400px;z-index:3;background:rgba(0,0,0,.6)}
#frame{position:absolute;inset:26px;z-index:9;border:4px solid #CBEF4B;border-radius:34px;box-shadow:0 0 0 40px #0E0E0E}
#tag{position:absolute;z-index:9;top:80px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:16px;font-size:26px;letter-spacing:8px}
#tag .d{width:18px;height:18px;border-radius:50%;background:#CBEF4B;box-shadow:0 0 14px #CBEF4B}#tag .c{color:#CBEF4B}
.hd{position:absolute;z-index:6;left:40px;right:40px;top:150px;height:260px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.hd .s{font-size:42px;color:#F2EFE6}
.hd .m{font-size:80px;line-height:1;letter-spacing:-2px}
.hd .m span,.hd .s span{color:#CBEF4B}
.cap{position:absolute;z-index:6;left:60px;right:60px;top:1555px;text-align:center;font-size:60px;line-height:1.1;letter-spacing:-1px;text-shadow:0 4px 18px rgba(0,0,0,.8)}
.cap .k{color:#CBEF4B}
.ov{position:absolute;z-index:5;left:60px;right:60px;top:1200px;text-align:center}
.pill{display:inline-block;background:rgba(14,14,14,.86);border:3px solid #CBEF4B;font-size:44px;padding:12px 28px;border-radius:18px}
.pill b{color:#CBEF4B} .pill.v{border-color:#7B5CFF} .pill.v b{color:#B9A8FF} .pill.o{border-color:#FF8A3D} .pill.o b{color:#FF8A3D}
.big{font-size:150px;line-height:1;text-shadow:0 10px 40px rgba(0,0,0,.6)}
.chips{display:flex;flex-direction:column;gap:16px;align-items:center}
.beads{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;background:rgba(14,14,14,.82);padding:18px;border-radius:22px;max-width:900px;margin:0 auto}
.beads i{display:block;width:56px;height:56px;border-radius:50%;box-shadow:inset -6px -6px 0 rgba(0,0,0,.2)}
.stamp{position:absolute;z-index:7;left:0;right:0;top:820px;text-align:center}
.stamp span{display:inline-block;background:#CBEF4B;color:#141414;font-size:130px;padding:6px 40px;border-radius:24px;transform:rotate(-4deg);box-shadow:0 20px 60px rgba(0,0,0,.6)}
#flash{position:absolute;inset:0;z-index:8;background:#fff;opacity:0}
#cta{position:absolute;z-index:6;left:0;right:0;top:1230px;text-align:center}
#cta span{display:inline-block;background:#CBEF4B;color:#141414;font-size:70px;padding:18px 46px;border-radius:60px;box-shadow:0 0 50px rgba(203,239,75,.6)}
#foot{position:absolute;z-index:9;top:1800px;left:0;right:0;text-align:center;font-size:20px;letter-spacing:2px;color:rgba(255,255,255,.75)}
#handle{position:absolute;z-index:9;top:1420px;left:0;right:0;text-align:center}
#handle span{display:inline-block;background:#141414;color:#CBEF4B;font-size:36px;padding:10px 28px;border-radius:40px;border:2px solid #CBEF4B}
'''
def hd(id,a,b,inner): return f'<div id="{id}" class="clip hd" data-start="{a}" data-duration="{round(b-a,2)}">{inner}</div>'
def ov(id,a,b,inner,top=None):
    st=f' style="top:{top}px"' if top else ''
    return f'<div id="{id}" class="clip ov" data-start="{a}" data-duration="{round(b-a,2)}"{st}>{inner}</div>'
def build(d,T,serie,fixes,merges,KEY,body,slides,js_extra,noflash=()):
    W=json.load(open(f'{d}/vwords.json'))
    words=[];skip=set()
    for i,w in enumerate(W):
        if i in skip: continue
        t=fixes.get(w['w'],w['w']); n=W[i+1]['w'] if i+1<len(W) else ''
        if (t,n) in merges: t=merges[(t,n)]; skip.add(i+1)
        words.append({'w':t,'s':w['s']})
    groups=[];cur=[]
    for w in words:
        cur.append(w)
        if len(cur)==3 or re.search(r'[,.?!:]$',w['w']): groups.append(cur);cur=[]
    if cur: groups.append(cur)
    caps=[];js=[]
    norm=lambda s: re.sub(r'[,.?!:]','',s).lower()
    keys={norm(k) for k in KEY}
    for gi,g in enumerate(groups):
        a=g[0]['s']; b=groups[gi+1][0]['s'] if gi+1<len(groups) else T-0.05
        spans=''.join(f'<span class="{"k" if norm(w["w"]) in keys else ""}" id="c{gi}_{j}">{html.escape(w["w"])}</span> ' for j,w in enumerate(g))
        caps.append(f'<div id="cg{gi}" class="clip cap" data-start="{a:.2f}" data-duration="{b-a:.2f}">{spans}</div>')
        for j,w in enumerate(g): js.append(f'tl.fromTo("#c{gi}_{j}",{{opacity:0.25,y:8}},{{opacity:1,y:0,duration:0.12}},{w["s"]:.2f});')
    S=json.load(open(f'{d}/scenes.json'))
    flash=''.join(f'tl.fromTo("#flash",{{opacity:0.3}},{{opacity:0,duration:0.18,immediateRender:false}},{s[0]});\n' for s in S[1:] if s[0] not in noflash)
    # zoom transitions on bg each scene: punch 1.22->1 quick
    zoom=''.join(f'tl.fromTo("#bg",{{scale:1.12,filter:"blur(6px)"}},{{scale:1,filter:"blur(0px)",duration:0.35,ease:"power3.out",immediateRender:false}},{s[0]});\n' for s in S[1:] if s[0] not in noflash)
    sl=''.join(f'tl.fromTo("{i}",{{opacity:0,x:200}},{{opacity:1,x:0,duration:0.35,ease:"back.out(1.8)"}},{t});\n' for i,t in slides)
    H=f'''<!doctype html><html lang="pt-BR"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script><style>{CSS}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{T}" data-width="1080" data-height="1920">
<video id="bg" class="clip" data-start="0" data-duration="{T}" src="assets/bg.mp4" muted></video>
<div id="shade" class="clip" data-start="0" data-duration="{T}"></div>
<div id="tsh" class="clip" data-start="0" data-duration="{T}"></div><div id="bsh" class="clip" data-start="0" data-duration="{T}"></div>
{body}
{chr(10).join(caps)}
<div id="flash" class="clip" data-start="0" data-duration="{T}"></div>
<div id="frame" class="clip" data-start="0" data-duration="{T}"></div>
<div id="tag" class="clip" data-start="0" data-duration="{T}"><span class="d"></span>OBOLARI ACADEMY<span class="c">· {serie}</span></div>
<div id="foot" class="clip" data-start="0" data-duration="{T}">@OBOLARI_ACADEMY · CONTEÚDO EDUCATIVO · NÃO É RECOMENDAÇÃO MÉDICA</div>
</div><script>
window.__timelines=window.__timelines||{{}};
const tl=gsap.timeline({{paused:true}});
tl.set("#flash",{{opacity:0}},0);
tl.fromTo("#flash",{{opacity:0.5}},{{opacity:0,duration:0.25}},0.0);
tl.fromTo("#bg",{{scale:1.22}},{{scale:1,duration:0.6,ease:"power3.out"}},0);
{flash}{zoom}{sl}{js_extra}
{chr(10).join(js)}
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
    os.makedirs(f'{d}/hf/assets',exist_ok=True)
    shutil.copy('/mnt/skills/examples/canvas-design/canvas-fonts/BricolageGrotesque-Bold.ttf',f'{d}/hf/assets/Bric-Bold.ttf')
    if not os.path.exists(f'{d}/hf/assets/bg.mp4'): os.link(f'{d}/bg.mp4',f'{d}/hf/assets/bg.mp4')
    open(f'{d}/hf/index.html','w').write(H); print('ok',len(groups))
