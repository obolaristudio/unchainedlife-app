import json,os,shutil,subprocess
tl=json.load(open('tl.json')); C=tl['cues']; S={s['key']:s for s in tl['segs']}
idx={s['key']:i for i,s in enumerate(tl['segs'])}
HEAD='''<!doctype html><html lang="pt-BR"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script><style>
@font-face{font-family:"Bric";src:url("assets/fonts/Bricolage-800.ttf");font-weight:800}
@font-face{font-family:"Bric";src:url("assets/fonts/Bricolage-700.ttf");font-weight:700}
:root{--lime:#CBEF4B;--ink:#141414;--cream:#F2EFE6;--card:#FBFAF6;--red:#D9503F;--grid:#E6E3DA}
*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1920px;overflow:hidden;background:#141414}
#root{position:relative;width:1080px;height:1920px;font-family:"Bric",sans-serif;overflow:hidden;color:var(--ink)}
#foot{position:absolute;left:0;top:0;width:1080px;height:1920px;object-fit:cover}
.lay{position:absolute;inset:0}
%s</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="%.3f" data-width="1080" data-height="1920">
<video id="foot" class="clip" data-start="0" data-duration="%.3f" src="assets/seg.mp4" muted></video>
%s</div><script>const tl=gsap.timeline({paused:true});
%s
window.__timelines["main"]=tl;tl.seek(0);</script></body></html>'''
def proj(key,css,html,js):
    s=S[key]; d=round(s['end']-s['start'],3); p=f'hf/{key}'
    os.makedirs(p+'/assets/fonts',exist_ok=True)
    shutil.copy(f"seg/{idx[key]:02d}.mp4",p+'/assets/seg.mp4')
    for f in ('Bricolage-800.ttf','Bricolage-700.ttf'): shutil.copy(os.path.expanduser('~/.fonts/'+f),p+'/assets/fonts/'+f)
    shutil.copy('../hftest/hyperframes.json',p+'/hyperframes.json')
    open(p+'/index.html','w').write(HEAD%(css,d,d,html,js))
L=lambda k,key: round(C[k]-S[key]['start'],3) if isinstance(k,str) else round(k-S[key]['start'],3)
# A — 04 Snap Zoom
a=L('a1','A')
proj('A','#foot{transform-origin:50% 42%}','',f'''tl.fromTo("#foot",{{scale:1}},{{scale:1.38,duration:0.1,ease:"expo.out"}},{a});
tl.to("#foot",{{scale:1,duration:0.12,ease:"power2.in"}},{a+1.35});''')
# B — 13 Magazine Cover
b=L('b1','B')-0.1
proj('B','''#foot{transform-origin:50% 50%}
#flash{position:absolute;inset:0;background:#fff;opacity:0}
#mast{position:absolute;left:0;right:0;top:118px;text-align:center;font-weight:800;font-size:150px;letter-spacing:-6px;line-height:1;opacity:0}
#bg{position:absolute;inset:0;background:var(--cream);opacity:0}
#kick{position:absolute;left:96px;top:300px;background:var(--red);color:#fff;font-weight:800;font-size:34px;letter-spacing:4px;padding:8px 20px;border-radius:8px;opacity:0}
#issue{position:absolute;right:96px;top:310px;font-weight:700;font-size:26px;letter-spacing:3px;opacity:0}
#head{position:absolute;left:110px;right:110px;top:1000px;color:#fff;font-weight:800;font-size:92px;line-height:.98;letter-spacing:-2px;text-shadow:0 6px 24px rgba(0,0,0,.6);opacity:0}
#badge{position:absolute;right:70px;top:420px;width:250px;height:250px;border-radius:50%;background:var(--lime);border:6px solid var(--ink);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;font-weight:800;font-size:40px;line-height:1;box-shadow:10px 10px 0 var(--ink);opacity:0}
#badge b{font-size:64px}
#bar{position:absolute;left:96px;top:430px;width:150px;height:90px;background:repeating-linear-gradient(90deg,#141414 0 4px,#fff 4px 7px,#141414 7px 9px,#fff 9px 14px);border:6px solid #fff;opacity:0}''',
'''<div id="bg" class="clip lay" data-start="0" data-duration="99"></div>''','')
h=open('hf/B/index.html').read()
h=h.replace('<video id="foot"','<div id="bg" class="clip" data-start="0" data-duration="%s"></div><video id="foot"'%S['B']['end']).replace('<div id="bg" class="clip lay" data-start="0" data-duration="99"></div>','''<div id="cov" class="clip lay" data-start="0" data-duration="DUR">
<div id="mast">LONGEVIDADE</div><div id="kick">ESTUDO PURE</div><div id="issue">Nº 01 · OBOLARI ACADEMY</div>
<div id="bar"></div><div id="badge">THE<br>LANCET<b>2015</b></div>
<div id="head">140 mil pessoas.<br>17 países.</div></div><div id="flash" class="clip" data-start="0" data-duration="DUR"></div>''')
d=round(S['B']['end']-S['B']['start'],3); h=h.replace('DUR',str(d)).replace('data-duration="%s"></div><video'%S['B']['end'],'data-duration="%s"></div><video'%d)
h=h.replace('const tl=gsap.timeline({paused:true});\n',f'''const tl=gsap.timeline({{paused:true}});
tl.fromTo("#flash",{{opacity:0}},{{opacity:1,duration:0.05}},{b});tl.to("#flash",{{opacity:0,duration:0.35,ease:"power2.out"}},{b+0.07});
tl.set("#bg",{{opacity:1}},{b+0.05});tl.set("#foot",{{scale:0.78,y:120,outline:"8px solid #fff"}},{b+0.05});
tl.fromTo("#mast",{{opacity:0,y:-40}},{{opacity:1,y:0,duration:0.3,ease:"power3.out"}},{b+0.1});
tl.fromTo("#kick,#issue,#bar",{{opacity:0}},{{opacity:1,duration:0.2,stagger:0.08}},{b+0.35});
tl.fromTo("#badge",{{opacity:0,scale:0,rotation:-30}},{{opacity:1,scale:1,rotation:-12,duration:0.4,ease:"back.out(2.5)"}},{b+0.6});
tl.fromTo("#head",{{opacity:0,y:40}},{{opacity:1,y:0,duration:0.35,ease:"power3.out"}},{b+0.45});
tl.fromTo("#flash",{{opacity:0}},{{opacity:0.7,duration:0.04}},{b+1.9});tl.to("#flash",{{opacity:0,duration:0.25}},{b+1.95});
''')
open('hf/B/index.html','w').write(h)
# C — 08 Growth Curve
c0=1.25; cs=L('c1','C'); ce=L(22.44,'C')
proj('C','''#chart{position:absolute;inset:0;background-color:var(--cream);background-image:linear-gradient(var(--grid) 2px,transparent 2px),linear-gradient(90deg,var(--grid) 2px,transparent 2px);background-size:60px 60px}
#chart svg{position:absolute;left:0;top:0}
#pill{position:absolute;right:70px;top:250px;background:var(--red);color:#fff;border:5px solid var(--ink);box-shadow:12px 12px 0 var(--ink);border-radius:24px;padding:20px 40px;text-align:center}
#pill .n{font-size:170px;font-weight:800;line-height:1}#pill .l{font-size:40px;font-weight:700}
#label{position:absolute;left:70px;top:250px;background:var(--lime);border:5px solid var(--ink);box-shadow:10px 10px 0 var(--ink);border-radius:14px;padding:12px 24px;font-size:50px;font-weight:800;max-width:430px}
#ax{position:absolute;left:80px;top:1250px;font-size:30px;font-weight:700;color:#777}''',
f'''<div id="chart" class="clip" data-start="{c0}" data-duration="{round(S['C']['end']-S['C']['start']-c0,3)}">
<svg width="1080" height="1920" viewBox="0 0 1080 1920"><path id="line" d="M80 1210 C 300 1170, 450 1060, 600 900 S 880 640, 990 600" fill="none" stroke="#D9503F" stroke-width="16" stroke-linecap="round"/><circle id="dot" cx="990" cy="600" r="26" fill="#D9503F" stroke="#141414" stroke-width="6"/></svg>
<div id="label">−5 kg de força na mão</div><div id="pill"><div class="n"><span id="num">+0</span>%</div><div class="l">risco de morte</div></div>
<div id="ax">menos força →</div></div>''',
f'''const L=document.getElementById("line").getTotalLength();
tl.fromTo("#chart",{{clipPath:"circle(0% at 50% 45%)"}},{{clipPath:"circle(80% at 50% 45%)",duration:0.35,ease:"power3.out"}},{c0});
tl.fromTo("#label",{{opacity:0,x:-60}},{{opacity:1,x:0,duration:0.3,ease:"power3.out"}},{c0+0.15});
tl.fromTo("#pill",{{opacity:0,scale:0.6,rotation:-6}},{{opacity:1,scale:1,rotation:0,duration:0.35,ease:"back.out(2.5)"}},{cs});
tl.fromTo("#line",{{strokeDasharray:L,strokeDashoffset:L}},{{strokeDashoffset:0,duration:{ce-cs:.2f},ease:"power2.inOut"}},{cs});
tl.fromTo("#dot",{{scale:0,transformOrigin:"50% 50%"}},{{scale:1,duration:0.25,ease:"back.out(3)"}},{ce});
const c={{v:0}};tl.to(c,{{v:16,duration:{ce-cs:.2f},ease:"power2.inOut",onUpdate:()=>{{document.getElementById("num").textContent="+"+Math.round(c.v)}}}},{cs});
tl.fromTo("#pill",{{scale:1}},{{scale:1.12,duration:0.08,yoyo:true,repeat:1}},{ce});''')
# I — 20 Checklist
rows=[('Treino de força','2x+ por semana'),('Proteína','em todas as refeições'),('Sono','de qualidade')]
ti=[L(k,'I') for k in ('i1','i2','i3')]
rh=''.join(f'<div class="row" id="r{i}"><div class="bx"><span id="k{i}">✓</span></div><div><div class="t">{a}</div><div class="s">{b}</div></div></div>' for i,(a,b) in enumerate(rows))
proj('I','''#wipe{position:absolute;inset:0;background:var(--ink)}
#board{position:absolute;left:70px;right:70px;top:190px}
#cnt{font-weight:800;font-size:190px;line-height:1;color:var(--lime)}#cnt small{font-size:90px;color:#fff;opacity:.5}
#ttl{color:#fff;font-weight:800;font-size:60px;margin:10px 0 40px}
.row{display:flex;gap:30px;align-items:center;background:var(--card);border:5px solid var(--lime);border-radius:20px;padding:22px 30px;margin-bottom:26px}
.bx{width:84px;height:84px;flex:none;border:5px solid var(--ink);border-radius:14px;display:flex;align-items:center;justify-content:center;font-size:58px;font-weight:800}
.t{font-weight:800;font-size:54px}.s{font-weight:700;font-size:34px;color:#555}''',
f'''<div id="wipe" class="clip" data-start="0.05" data-duration="{round(S['I']['end']-S['I']['start']-0.05,3)}"><div id="board">
<div id="cnt"><span id="n">0</span><small>/3</small></div><div id="ttl">O que a ciência mostra</div>{rh}</div></div>''',
f'''tl.fromTo("#wipe",{{clipPath:"circle(0% at 50% 50%)"}},{{clipPath:"circle(85% at 50% 50%)",duration:0.5,ease:"power3.inOut"}},0.05);
tl.fromTo(".row",{{opacity:0.35,x:40}},{{x:0,duration:0.3,stagger:0.08,ease:"power3.out"}},0.4);
tl.set("[id^=k]",{{opacity:0}},0);
'''+''.join(f'''tl.to("#r{i}",{{opacity:1,duration:0.1}},{t});tl.to("#r{i} .bx",{{backgroundColor:"#CBEF4B",duration:0.1}},{t});tl.fromTo("#k{i}",{{opacity:0,scale:2.2}},{{opacity:1,scale:1,duration:0.25,ease:"back.out(3)"}},{t});tl.set("#n",{{textContent:"{i+1}"}},{t});tl.fromTo("#cnt",{{scale:1.15}},{{scale:1,duration:0.25,transformOrigin:"0% 50%"}},{t});
''' for i,t in enumerate(ti)))
print('ok',a,b,cs,ce,ti)
