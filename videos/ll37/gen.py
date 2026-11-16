import json,re,html
# Reel LL-37 (estrutura do viral @thecellbrief, roteiro e imagens originais). Template: videos/bpc157/gen.py
W=json.load(open('vwords.json')); T=82.9
rep={'LL37.':'LL-37.','LL37':'LL-37','Obolary':'Obolari'}
words=[{'w':rep.get(w['w'],w['w']),'s':w['s']} for w in W]
groups=[];cur=[]
for w in words:
    cur.append(w)
    if len(cur)==3 or re.search(r'[,.?!:]$',w['w']): groups.append(cur);cur=[]
if cur: groups.append(cur)
KEY={'pele','antibiótico,','germes','mãos','cortes','LL-37.','LL-37','37','colar','contas.','L,','pele,','intestino','respiratórias.','negativa.','positiva.','ímã,','atraem.','furos','2020,','microscópio.','falhas.','morreu.','2003','dois','dias','normal.','surpresa.','vitamina','D.','gene','creme,','feridas','estudo.','fura.','sabia','Comenta'}
caps=[];js=[]
for gi,g in enumerate(groups):
    a=g[0]['s']; b=groups[gi+1][0]['s'] if gi+1<len(groups) else T-0.1
    spans=''.join(f'<span class="{"k" if w["w"] in KEY else ""}" id="c{gi}_{j}">{html.escape(w["w"])}</span> ' for j,w in enumerate(g))
    caps.append(f'<div id="cg{gi}" class="clip cap" data-start="{a:.2f}" data-duration="{b-a:.2f}">{spans}</div>')
    for j,w in enumerate(g): js.append(f'tl.fromTo("#c{gi}_{j}",{{opacity:0.25,y:8}},{{opacity:1,y:0,duration:0.12}},{w["s"]:.2f});')
# colar de 37 contas: as 2 primeiras sao "L"
beads=''.join(f'<i id="bd{i}" class="{"L" if i<2 else ""}">{"L" if i<2 else ""}</i>' for i in range(37))
for i in range(37): js.append(f'tl.fromTo("#bd{i}",{{scale:0}},{{scale:1,duration:0.14,ease:"back.out(3)"}},{16.5+i*0.035:.3f});')
def hd(id,a,b,inner): return f'<div id="{id}" class="clip hd" data-start="{a}" data-duration="{round(b-a,2)}">{inner}</div>'
H=f'''<!doctype html><html lang="pt-BR"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script><style>
@font-face{{font-family:"Bric";src:url("assets/fonts/Bricolage-800.ttf");font-weight:800}}
@font-face{{font-family:"Bric";src:url("assets/fonts/Bricolage-700.ttf");font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}html,body{{width:1080px;height:1920px;overflow:hidden;background:#0E0E0E}}
#root{{position:relative;width:1080px;height:1920px;font-family:"Bric",sans-serif;color:#fff;overflow:hidden}}
#bg{{position:absolute;inset:0;width:1080px;height:1920px;object-fit:cover;z-index:1}}
#shade{{position:absolute;left:0;top:420px;width:1080px;height:1100px;z-index:2;background:linear-gradient(rgba(0,0,0,0) 55%,rgba(0,0,0,.6) 100%)}}
#tag{{position:absolute;z-index:9;top:80px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:16px;font-weight:700;font-size:26px;letter-spacing:8px}}
#tag .d{{width:18px;height:18px;border-radius:50%;background:#CBEF4B;box-shadow:0 0 14px #CBEF4B}}#tag .c{{color:#CBEF4B}}
.hd{{position:absolute;z-index:6;left:40px;right:40px;top:150px;height:260px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}}
.hd .s{{font-weight:700;font-size:42px;color:#F2EFE6}}
.hd .m{{font-weight:800;font-size:80px;line-height:1;letter-spacing:-2px}}
.hd .m span,.hd .s span{{color:#CBEF4B}}
.cap{{position:absolute;z-index:6;left:60px;right:60px;top:1555px;text-align:center;font-weight:800;font-size:60px;line-height:1.1;letter-spacing:-1px;text-shadow:0 4px 18px rgba(0,0,0,.8)}}
.cap .k{{color:#CBEF4B}}
.ov{{position:absolute;z-index:5;left:60px;right:60px;top:1200px;text-align:center}}
.pill{{display:inline-block;background:rgba(14,14,14,.86);border:3px solid #CBEF4B;font-weight:800;font-size:44px;padding:12px 28px;border-radius:18px}}
.pill b{{color:#CBEF4B}} .pill.o{{border-color:#FF8A3D}} .pill.o b{{color:#FF8A3D}} .pill.r{{border-color:#E53935}} .pill.r b{{color:#E53935}}
.big{{font-weight:800;font-size:150px;line-height:1;text-shadow:0 10px 40px rgba(0,0,0,.6)}}
.chips{{display:flex;flex-direction:row;flex-wrap:wrap;gap:14px;justify-content:center}}
.chip{{display:inline-block;background:rgba(14,14,14,.88);border:3px solid #CBEF4B;font-weight:800;font-size:46px;padding:10px 26px;border-radius:16px}}
.beads{{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;background:rgba(14,14,14,.82);padding:18px;border-radius:22px;max-width:820px;margin:0 auto}}
.beads i{{display:flex;align-items:center;justify-content:center;width:62px;height:62px;border-radius:50%;background:#3D7BFF;box-shadow:inset -6px -6px 0 rgba(0,0,0,.25);font-style:normal;font-weight:800;font-size:40px;color:#141414}}
.beads i.L{{background:#CBEF4B;border:3px solid #fff}}
.charge{{display:flex;justify-content:center;align-items:center;gap:40px}}
.ball{{width:250px;height:250px;border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;font-weight:800;border:6px solid #141414;box-shadow:8px 8px 0 #141414}}
.ball b{{font-size:130px;line-height:.9}} .ball small{{font-size:32px}}
.ball.neg{{background:#E53935}} .ball.pos{{background:#CBEF4B;color:#141414}}
.study{{display:inline-block;max-width:900px;background:#FBFAF6;color:#141414;border:4px solid #141414;box-shadow:10px 10px 0 #141414;border-radius:16px;padding:24px 30px;text-align:left}}
.study .j{{font-family:monospace;font-size:26px;letter-spacing:3px;color:#555}} .study .t{{font-weight:800;font-size:44px;line-height:1.1;margin-top:8px}} .study .t mark{{background:#CBEF4B;padding:0 6px}}
.steps{{display:flex;flex-direction:column;gap:14px;align-items:center}}
#days span{{display:inline-block;color:#E53935;-webkit-text-stroke:4px #fff;font-size:190px}}
#crack{{position:absolute;inset:0;z-index:8;opacity:0}}
#stampS{{position:absolute;z-index:8;left:0;right:0;top:760px;text-align:center}}
#stampS span{{display:inline-block;background:#E53935;color:#fff;font-weight:800;font-size:120px;padding:6px 40px;border-radius:24px;border:6px solid #141414;transform:rotate(-4deg);box-shadow:14px 14px 0 #141414}}
#vitd{{position:absolute;z-index:6;left:0;right:0;top:820px;text-align:center}}
#vitd span{{display:inline-block;background:#CBEF4B;color:#141414;font-weight:800;font-size:130px;padding:6px 40px;border-radius:24px;border:6px solid #141414;box-shadow:14px 14px 0 #141414}}
#sum{{position:absolute;z-index:6;left:0;right:0;top:700px;text-align:center;font-weight:800;font-size:130px;line-height:1.05;letter-spacing:-3px;text-shadow:0 10px 40px rgba(0,0,0,.7)}}
#sum span{{color:#CBEF4B}}
#flash{{position:absolute;inset:0;z-index:8;background:#fff;opacity:0}}
#cta{{position:absolute;z-index:6;left:0;right:0;top:1230px;text-align:center}}
#cta span{{display:inline-block;background:#CBEF4B;color:#141414;font-weight:800;font-size:70px;padding:18px 46px;border-radius:60px;box-shadow:0 0 50px rgba(203,239,75,.6)}}
#handle{{position:absolute;z-index:6;left:0;right:0;top:1400px;text-align:center}}
#handle span{{display:inline-block;background:#141414;color:#CBEF4B;font-family:monospace;font-weight:700;font-size:34px;letter-spacing:4px;padding:10px 26px;border-radius:40px}}
#foot{{position:absolute;z-index:9;top:1800px;left:0;right:0;text-align:center;font-weight:700;font-size:20px;letter-spacing:2px;color:rgba(255,255,255,.75)}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{T}" data-width="1080" data-height="1920">
<video id="bg" class="clip" data-start="0" data-duration="{T}" src="assets/bg.mp4" muted></video>
<div id="shade" class="clip" data-start="0" data-duration="{T}"></div>
{hd('h0',0,4.3,'<div class="s">Sua pele fabrica o próprio</div><div class="m" style="font-size:118px"><span>ANTIBIÓTICO</span> 🛡️</div>')}
{hd('h1',4.3,10.2,'<div class="m">Germes nas suas<br><span>mãos</span>, todo dia 🖐️</div>')}
<div id="o1" class="clip ov" data-start="8.7" data-duration="1.5"><span class="pill">e a maioria <b>não vai longe</b></span></div>
{hd('h2',10.2,14.1,'<div class="s">um dos motivos:</div><div class="m" style="font-size:150px"><span>LL-37</span></div>')}
{hd('h3',14.1,22.1,'<div class="m"><span id="n37">0</span> aminoácidos</div><div class="s">um colar de 37 contas 📿</div>')}
<div id="o2" class="clip ov" data-start="16.4" data-duration="5.7" style="top:1000px"><div class="beads">{beads}</div><div style="margin-top:22px"><span class="pill" id="pL">começa com <b>L</b> + <b>L</b> → LL-37</span></div></div>
{hd('h4',22.1,26.7,'<div class="m">Quem <span>fabrica</span>?</div>')}
<div id="o3" class="clip ov" data-start="23.2" data-duration="3.5"><div class="chips" style="flex-direction:column;align-items:center"><span class="chip" id="q1">🧴 pele</span><span class="chip" id="q2">🌀 intestino</span><span class="chip" id="q3">🫁 vias respiratórias</span></div></div>
{hd('h5',26.7,38.0,'<div class="m">Como ele <span>age</span>?</div>')}
<div id="o4" class="clip ov" data-start="29.3" data-duration="6.2" style="top:1050px"><div class="charge"><div class="ball neg" id="bn"><b>−</b><small>bactéria</small></div><div class="big" id="mag" style="font-size:110px">🧲</div><div class="ball pos" id="bp"><b>+</b><small>LL-37</small></div></div></div>
<div id="o5" class="clip ov" data-start="35.5" data-duration="2.5"><span class="pill r">gruda e abre <b>furos</b> na parede</span></div>
{hd('h6',38.0,45.6,'<div class="m"><span>2020</span> 🔬</div><div class="s">filmado no microscópio</div>')}
<div id="o6" class="clip ov" data-start="38.6" data-duration="2.7" style="top:1080px"><div class="study"><div class="j">SCIENTIFIC REPORTS · 2020</div><div class="t">LL-37 forma <mark>canais</mark> na membrana da bactéria</div></div></div>
<div id="o7" class="clip ov" data-start="41.4" data-duration="4.2" style="top:1080px"><div class="steps"><span class="pill" id="s1">1 · <b>falhas</b> na parede</span><span class="pill r" id="s2">2 · a bactéria <b>morre</b></span></div></div>
{hd('h7',45.6,55.3,'<div class="m">Depois de um <span>corte</span></div><div class="s">a pele aumenta a produção</div>')}
<div id="o8" class="clip ov" data-start="48.5" data-duration="2.1" style="top:1080px"><div class="study"><div class="j">J INVEST DERMATOL · 2003</div><div class="t">pico de LL-37 na <mark>pele ferida</mark></div></div></div>
<div id="days" class="clip ov" data-start="50.6" data-duration="2.0" style="top:900px"><span>2 DIAS</span></div>
<div id="o9" class="clip ov" data-start="52.6" data-duration="2.7"><span class="pill">ferida fechou → <b>volta ao normal</b></span></div>
<svg id="crack" class="clip" data-start="55.3" data-duration="1.4" viewBox="0 0 1080 1920"><g stroke="#fff" stroke-width="7" fill="none" stroke-linecap="round"><path d="M540 960 L300 640 L180 420"/><path d="M540 960 L820 700 L1000 520"/><path d="M540 960 L700 1260 L760 1560"/><path d="M540 960 L260 1180 L80 1300"/><path d="M540 960 L480 600 L520 300"/><path d="M300 640 L120 700"/><path d="M700 1260 L940 1320"/></g></svg>
<div id="stampS" class="clip" data-start="55.35" data-duration="1.35"><span>SURPRESA!</span></div>
{hd('h8',56.7,64.6,'<div class="m">Quem <span>liga</span> a fábrica?</div><div class="s">em células humanas</div>')}
<div id="vitd" class="clip" data-start="61.0" data-duration="3.6"><span>☀️ VITAMINA D</span></div>
<div id="o10" class="clip ov" data-start="62.0" data-duration="2.6"><span class="pill">aciona o <b>gene</b> do LL-37 🧬</span></div>
{hd('h9',64.6,70.4,'<div class="m">E em <span>pessoas</span>?</div>')}
<div id="o11" class="clip ov" data-start="66.4" data-duration="2.8"><span class="pill">testado em <b>creme</b>, em feridas na perna</span></div>
<div id="o12" class="clip ov" data-start="69.2" data-duration="1.2"><span class="pill o">ainda <b>em estudo</b></span></div>
<div id="sum" class="clip" data-start="70.4" data-duration="3.8"><div id="sa">germe entra.</div><div id="sb"><span>LL-37 fura.</span></div></div>
{hd('h10',74.2,T,'<div class="m">Você já <span>sabia</span>?</div><div class="s">conteúdo educativo</div>')}
<div id="cta" class="clip" data-start="79.4" data-duration="{round(T-79.4,2)}"><span>Comenta aqui 💬</span></div>
<div id="handle" class="clip" data-start="79.6" data-duration="{round(T-79.6,2)}"><span>@obolari_academy</span></div>
{chr(10).join(caps)}
<div id="flash" class="clip" data-start="0" data-duration="{T}"></div>
<div id="tag" class="clip" data-start="0" data-duration="{T}"><span class="d"></span>OBOLARI ACADEMY<span class="c">· PEPTÍDEOS</span></div>
<div id="foot" class="clip" data-start="0" data-duration="{T}">@OBOLARI_ACADEMY · CONTEÚDO EDUCATIVO · NÃO É RECOMENDAÇÃO MÉDICA</div>
</div><script>
const tl=gsap.timeline({{paused:true}});
tl.set("#flash",{{opacity:0}},0);
tl.fromTo("#h0 .m",{{scale:1.6,opacity:0}},{{scale:1,opacity:1,duration:0.3,ease:"power4.out"}},0.0);
tl.fromTo("#flash",{{opacity:0.5}},{{opacity:0,duration:0.25}},0.0);
'''
for h,t in [('#h1',4.3),('#h3',14.1),('#h4',22.1),('#h5',26.7),('#h6',38.0),('#h7',45.6),('#h8',56.7),('#h9',64.6),('#h10',74.2)]:
    H+=f'tl.fromTo("{h}",{{y:30,opacity:0}},{{y:0,opacity:1,duration:0.3,ease:"power3.out"}},{t});\n'
S=json.load(open('scenes.json'))
for s_ in S[1:]:
    if s_[0]!=55.3: H+=f'tl.fromTo("#flash",{{opacity:0.3}},{{opacity:0,duration:0.18}},{s_[0]});\n'
for o,t in [('#o1',8.7),('#o5',35.5),('#o9',52.6),('#o10',62.0),('#o11',66.4),('#o12',69.2)]:
    H+=f'tl.fromTo("{o}",{{opacity:0,x:200}},{{opacity:1,x:0,duration:0.35,ease:"back.out(1.8)"}},{t});\n'
H+='''// 04 Snap Zoom no nome
tl.fromTo("#h2 .m",{scale:2.4,opacity:0},{scale:1,opacity:1,duration:0.28,ease:"power4.out"},12.4);
tl.fromTo("#h2 .s",{opacity:0},{opacity:1,duration:0.2},10.2);
tl.fromTo("#flash",{opacity:0.45},{opacity:0,duration:0.2},12.4);
// 08 contador 0 -> 37
tl.fromTo("#n37",{textContent:0},{textContent:37,duration:1.0,ease:"power2.out",snap:{textContent:1}},14.5);
tl.fromTo("#o2",{opacity:0},{opacity:1,duration:0.2},16.4);
tl.fromTo("#pL",{opacity:0,y:20},{opacity:1,y:0,duration:0.3,ease:"back.out(2)"},20.3);
tl.to(".beads i.L",{scale:1.25,duration:0.25,yoyo:true,repeat:3},20.3);
// 05 Checklist Pop
tl.fromTo("#q1",{opacity:0,scale:0.5},{opacity:1,scale:1,duration:0.25,ease:"back.out(2.5)"},23.3);
tl.fromTo("#q2",{opacity:0,scale:0.5},{opacity:1,scale:1,duration:0.25,ease:"back.out(2.5)"},24.2);
tl.fromTo("#q3",{opacity:0,scale:0.5},{opacity:1,scale:1,duration:0.25,ease:"back.out(2.5)"},25.4);
// cargas opostas se atraem
tl.fromTo("#bn",{opacity:0,x:-300},{opacity:1,x:0,duration:0.35,ease:"back.out(2)"},29.4);
tl.fromTo("#bp",{opacity:0,x:300},{opacity:1,x:0,duration:0.35,ease:"back.out(2)"},32.2);
tl.fromTo("#mag",{opacity:0,scale:0},{opacity:1,scale:1,duration:0.3,ease:"back.out(3)"},33.6);
tl.to("#bn",{x:110,duration:0.6,ease:"power3.in"},34.4);
tl.to("#bp",{x:-110,duration:0.6,ease:"power3.in"},34.4);
tl.to("#mag",{opacity:0,scale:0.3,duration:0.3},34.4);
tl.fromTo("#flash",{opacity:0.5},{opacity:0,duration:0.2},35.0);
// 13 Magazine Cover (estudos)
tl.fromTo("#o6 .study",{opacity:0,y:120,rotation:-6},{opacity:1,y:0,rotation:-2,duration:0.4,ease:"back.out(1.8)"},38.6);
tl.fromTo("#s1",{opacity:0,x:200},{opacity:1,x:0,duration:0.3,ease:"back.out(2)"},41.4);
tl.fromTo("#s2",{opacity:0,x:200},{opacity:1,x:0,duration:0.3,ease:"back.out(2)"},44.2);
tl.fromTo("#o8 .study",{opacity:0,y:120,rotation:6},{opacity:1,y:0,rotation:2,duration:0.4,ease:"back.out(1.8)"},48.5);
tl.fromTo("#days span",{scale:2.6,opacity:0},{scale:1,opacity:1,duration:0.25,ease:"power4.out"},50.62);
tl.fromTo("#flash",{opacity:0.5},{opacity:0,duration:0.2},50.62);
// 17 Frame Break (a surpresa)
tl.fromTo("#bg",{x:0},{x:-30,duration:0.05,yoyo:true,repeat:5},55.3);
tl.fromTo("#crack",{opacity:0,scale:0.6},{opacity:1,scale:1,duration:0.12},55.3);
tl.fromTo("#flash",{opacity:0.85},{opacity:0,duration:0.3},55.3);
tl.fromTo("#stampS span",{scale:3,opacity:0,rotation:-20},{scale:1,opacity:1,rotation:-4,duration:0.25,ease:"power3.in"},55.4);
tl.fromTo("#vitd span",{y:-1200,rotation:-10},{y:0,rotation:-3,duration:0.6,ease:"bounce.out"},61.0);
tl.fromTo("#sa",{opacity:0,x:-300},{opacity:1,x:0,duration:0.3,ease:"back.out(2)"},71.1);
tl.fromTo("#sb",{opacity:0,scale:2.2},{opacity:1,scale:1,duration:0.25,ease:"power4.out"},72.3);
tl.fromTo("#flash",{opacity:0.5},{opacity:0,duration:0.2},73.38);
tl.fromTo("#cta span",{scale:0.6,opacity:0},{scale:1,opacity:1,duration:0.4,ease:"back.out(2.2)"},79.5);
tl.to("#cta span",{scale:1.06,duration:0.45,yoyo:true,repeat:3,ease:"sine.inOut"},80.0);
tl.fromTo("#handle span",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},79.7);
// deriva lenta de zoom no fundo
tl.fromTo("#bg",{scale:1.0},{scale:1.06,duration:'''+str(T)+''',ease:"none"},0);
'''+'\n'.join(js)+'''
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
open('hf/index.html','w').write(H);print('ok',len(groups))
