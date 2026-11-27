import json,re,html,subprocess,sys,os
v=sys.argv[1]; C=json.load(open(f'{v}/cfg.json')); T=C['T']
W=json.load(open(f'{v}/words_fix.json'))
os.makedirs(f'{v}/hf/assets',exist_ok=True)
# --- fundo: cenas ---
PW,PH=1080,1100; CL='clips'
for i,(a,b,c,off,cx) in enumerate(C['scenes']):
    d=round(b-a,3); assert off+d<=5.87+0.01, (v,i,off,d)
    cw=round(768*PW/PH); x=int(max(0,min(1366-cw,1366*cx-cw/2)))
    fc=(f"[0:v]setpts=PTS-STARTPTS,fps=30,split[a][b];[a]crop={cw}:768:{x}:0,scale={PW}:{PH}:flags=lanczos,unsharp=5:5:0.4,setsar=1[p];"
        f"[b]scale=-2:1920,crop=1080:1920,boxblur=30:3,eq=brightness=-0.22:saturation=0.8,setsar=1[bg];[bg][p]overlay=0:420,format=yuv420p")
    subprocess.run(['ffmpeg','-loglevel','error','-y','-ss',str(off),'-t',str(d),'-i',f'{CL}/c{c}.mp4','-filter_complex',fc,'-an','-c:v','libx264','-crf','16','-preset','veryfast',f'{v}/sc_{i:02d}.mp4'],check=True)
open(f'{v}/list.txt','w').write(''.join(f"file 'sc_{i:02d}.mp4'\n" for i in range(len(C['scenes']))))
subprocess.run(['ffmpeg','-loglevel','error','-y','-f','concat','-i',f'{v}/list.txt','-c','copy',f'{v}/hf/assets/bg.mp4'],check=True)
for f in ['Bric-700.ttf','Bric-800.ttf','Mono.ttf']: subprocess.run(['cp',f'fonts/{f}',f'{v}/hf/assets/'])
# --- legendas ---
KEY=set(C['key']); groups=[];cur=[]
for w in W:
    cur.append(w)
    if len(cur)==3 or re.search(r'[,.?!:]$',w['w']): groups.append(cur);cur=[]
if cur: groups.append(cur)
caps=[];js=[]
for gi,g in enumerate(groups):
    a=g[0]['s']; b=groups[gi+1][0]['s'] if gi+1<len(groups) else T-0.05
    b=max(b,a+0.2)
    sp=''.join(f'<span class="{"k" if w["w"] in KEY else ""}" id="c{gi}_{j}">{html.escape(w["w"])}</span> ' for j,w in enumerate(g))
    caps.append(f'<div class="clip cap" data-start="{a:.2f}" data-duration="{b-a:.2f}">{sp}</div>')
    for j,w in enumerate(g): js.append(f'tl.fromTo("#c{gi}_{j}",{{opacity:0.3,scale:0.9}},{{opacity:1,scale:1,duration:0.12}},{w["s"]:.2f});')
el=[]
for i,(a,b,s,m) in enumerate(C['heads']):
    el.append(f'<div id="h{i}" class="clip hd" data-start="{a}" data-duration="{round(b-a,2)}">'+(f'<div class="s">{s}</div>' if s else '')+f'<div class="m">{m}</div></div>')
    js.append(f'tl.fromTo("#h{i} .m",{{scale:1.5,opacity:0}},{{scale:1,opacity:1,duration:0.3,ease:"power4.out"}},{a});')
for i,(a,d,t,k) in enumerate(C['pills']):
    el.append(f'<div id="p{i}" class="clip ov" data-start="{a}" data-duration="{d}"><span class="pill {k}">{t}</span></div>')
    js.append(f'tl.fromTo("#p{i} .pill",{{opacity:0,x:220}},{{opacity:1,x:0,duration:0.32,ease:"back.out(1.8)"}},{a});')
a,d,t1,t2=C['stamp']
el.append(f'<div id="st" class="clip" data-start="{a}" data-duration="{d}"><span class="sb">{t1}</span><div class="ss">{t2}</div></div>')
js+= [f'tl.fromTo("#st .sb",{{scale:3,opacity:0}},{{scale:1,opacity:1,duration:0.25,ease:"power3.in"}},{a});',
      f'tl.fromTo("#bg",{{filter:"grayscale(0) brightness(1)"}},{{filter:"grayscale(1) brightness(0.55)",duration:0.12}},{a});',
      f'tl.to("#bg",{{filter:"grayscale(0) brightness(1)",duration:0.2}},{a+d-0.1});',
      f'tl.fromTo("#bg",{{x:0}},{{x:-26,duration:0.05,yoyo:true,repeat:5}},{a});',
      f'tl.fromTo("#flash",{{opacity:0.8}},{{opacity:0,duration:0.3}},{a});']
for n,key in enumerate(['counter','counter2']):
    a,d,val,unit,lab=C[key]
    el.append(f'<div id="k{n}" class="clip ov cnt" data-start="{a}" data-duration="{d}"><div class="big"><span id="n{n}">0</span>{unit}</div><span class="pill">{lab}</span></div>')
    js+= [f'tl.fromTo("#k{n} .big",{{scale:2.2,opacity:0}},{{scale:1,opacity:1,duration:0.3,ease:"power4.out"}},{a});',
          f'tl.fromTo("#n{n}",{{textContent:{0 if val<1000 else val-40}}},{{textContent:{val},duration:1.1,ease:"power2.out",snap:{{textContent:1}}}},{a+0.15});']
a,d,rows=C['status']
el.append(f'<div id="sts" class="clip" data-start="{a}" data-duration="{d}">'+''.join(f'<div class="row" id="r{i}"><div class="fl">{f}</div><div><div class="lb">{l}</div><div class="tx">{t}</div></div></div>' for i,(f,l,t) in enumerate(rows))+'</div>')
for i in range(len(rows)): js.append(f'tl.fromTo("#r{i}",{{opacity:0,x:-200}},{{opacity:1,x:0,duration:0.35,ease:"back.out(1.6)"}},{a+0.2+i*1.6});')
for s_ in C['scenes'][1:]:
    js.append(f'tl.fromTo("#bg",{{scale:1.18}},{{scale:1,duration:0.45,ease:"power3.out"}},{s_[0]});')
    js.append(f'tl.fromTo("#flash",{{opacity:0.18}},{{opacity:0,duration:0.16}},{s_[0]});')
end=C['heads'][-1][0]
el.append(f'<div id="end" class="clip" data-start="{end}" data-duration="{round(T-end,2)}"><div class="warn">Conteúdo educativo. Não é recomendação médica nem sugestão de uso.</div><span class="handle">@obolari_academy</span></div>')
js.append(f'tl.fromTo("#end",{{opacity:0,y:40}},{{opacity:1,y:0,duration:0.4}},{end+0.3});')
H=f'''<!doctype html><html lang="pt-BR"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script><style>
@font-face{{font-family:"Bric";src:url("assets/Bric-800.ttf");font-weight:800}}@font-face{{font-family:"Bric";src:url("assets/Bric-700.ttf");font-weight:700}}@font-face{{font-family:"Mono";src:url("assets/Mono.ttf")}}
*{{margin:0;padding:0;box-sizing:border-box}}html,body{{width:1080px;height:1920px;overflow:hidden;background:#0E0E0E}}
#root{{position:relative;width:1080px;height:1920px;font-family:"Bric",sans-serif;color:#fff;overflow:hidden}}
#bg{{position:absolute;inset:0;width:1080px;height:1920px;object-fit:cover;z-index:1}}
#tsh{{position:absolute;left:0;top:0;width:1080px;height:430px;z-index:3;background:linear-gradient(rgba(0,0,0,.7),rgba(0,0,0,.35))}} #bsh{{position:absolute;left:0;top:1500px;width:1080px;height:420px;z-index:3;background:linear-gradient(rgba(0,0,0,.2),rgba(0,0,0,.75))}}
#frame{{position:absolute;inset:26px;z-index:9;border:4px solid #CBEF4B;border-radius:34px;box-shadow:0 0 0 40px #0E0E0E}}
#tag{{position:absolute;z-index:9;top:78px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:14px;font-family:"Mono";font-size:24px;letter-spacing:5px}}
#tag .d{{width:16px;height:16px;border-radius:50%;background:#CBEF4B;box-shadow:0 0 14px #CBEF4B}}#tag .c{{color:#CBEF4B}}
.hd{{position:absolute;z-index:6;left:50px;right:50px;top:140px;height:270px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:6px}}
.hd .s{{font-family:"Mono";font-size:28px;letter-spacing:2px;color:#141414;background:#CBEF4B;border:3px solid #141414;padding:4px 14px;border-radius:8px;text-transform:uppercase}}
.hd .m{{font-weight:800;font-size:82px;line-height:1.02;letter-spacing:-2px;text-shadow:0 6px 24px rgba(0,0,0,.6)}} .hd .m span{{color:#CBEF4B}}
.cap{{position:absolute;z-index:7;left:60px;right:60px;top:1560px;text-align:center;font-weight:800;font-size:62px;line-height:1.1;letter-spacing:-1px;text-shadow:0 4px 18px rgba(0,0,0,.85)}} .cap .k{{color:#CBEF4B}}
.ov{{position:absolute;z-index:5;left:60px;right:60px;top:1240px;text-align:center}}
.pill{{display:inline-block;background:rgba(14,14,14,.88);border:3px solid #CBEF4B;font-weight:800;font-size:44px;padding:12px 28px;border-radius:18px;box-shadow:8px 8px 0 rgba(203,239,75,.35)}}
.pill b{{color:#CBEF4B}} .pill.v{{border-color:#FF8A3D}} .pill.v b{{color:#FF8A3D}}
.cnt{{top:1000px}} .big{{font-weight:800;font-size:200px;line-height:1;color:#CBEF4B;text-shadow:0 10px 40px rgba(0,0,0,.7);margin-bottom:16px}}
#st{{position:absolute;z-index:8;left:0;right:0;top:760px;text-align:center}} #st .sb{{display:inline-block;background:#CBEF4B;color:#141414;font-weight:800;font-size:130px;padding:6px 40px;border-radius:24px;border:6px solid #141414;transform:rotate(-4deg);box-shadow:14px 14px 0 #141414}}
#st .ss{{margin-top:40px;display:inline-block;background:rgba(14,14,14,.9);border:3px solid #fff;font-weight:800;font-size:48px;padding:10px 26px;border-radius:16px}} #st .ss b{{color:#CBEF4B}}
#sts{{position:absolute;z-index:6;left:70px;right:70px;top:880px;display:flex;flex-direction:column;gap:22px}}
.row{{display:flex;gap:22px;align-items:center;background:#FBFAF6;color:#141414;border:4px solid #141414;border-radius:20px;padding:20px 24px;box-shadow:10px 10px 0 #CBEF4B}}
.fl{{font-size:76px}} .lb{{font-family:"Mono";font-size:26px;letter-spacing:3px;color:#555}} .tx{{font-weight:800;font-size:40px;line-height:1.1}}
#flash{{position:absolute;inset:0;z-index:8;background:#fff;opacity:0}}
#end{{position:absolute;z-index:6;left:70px;right:70px;top:1080px;text-align:center}} .warn{{background:rgba(14,14,14,.88);border-left:10px solid #D9503F;font-weight:700;font-size:38px;padding:16px 22px;border-radius:12px;margin-bottom:24px;text-align:left}}
.handle{{display:inline-block;background:#141414;color:#CBEF4B;font-family:"Mono";font-size:34px;padding:10px 26px;border-radius:40px;border:2px solid #CBEF4B}}
#foot{{position:absolute;z-index:9;top:1806px;left:0;right:0;text-align:center;font-family:"Mono";font-size:18px;letter-spacing:2px;color:rgba(255,255,255,.7)}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{T}" data-width="1080" data-height="1920">
<video id="bg" class="clip" data-start="0" data-duration="{T}" src="assets/bg.mp4" muted></video>
<div id="tsh" class="clip" data-start="0" data-duration="{T}"></div><div id="bsh" class="clip" data-start="0" data-duration="{T}"></div>
{chr(10).join(el)}
{chr(10).join(caps)}
<div id="flash" class="clip" data-start="0" data-duration="{T}"></div>
<div id="frame" class="clip" data-start="0" data-duration="{T}"></div>
<div id="tag" class="clip" data-start="0" data-duration="{T}"><span class="d"></span>OBOLARI ACADEMY<span class="c">· {C['tag']}</span></div>
<div id="foot" class="clip" data-start="0" data-duration="{T}">CONTEÚDO EDUCATIVO · NÃO É RECOMENDAÇÃO MÉDICA</div>
</div><script>
const tl=gsap.timeline({{paused:true}});
tl.fromTo("#flash",{{opacity:0.6}},{{opacity:0,duration:0.25}},0);
{chr(10).join(js)}
window.__timelines=window.__timelines||{{}};window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
open(f'{v}/hf/index.html','w').write(H); print('ok',v,len(groups))
