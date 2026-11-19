import json,re,html,random
random.seed(7)
W=json.load(open('vwords.json')); T=72.0
rep={'bichiga.':'bexiga.','Salve':'Salva','60,':'60,'}
words=[{'w':rep.get(w['w'],w['w']),'s':w['s']} for w in W]
groups=[];cur=[]
for w in words:
    cur.append(w)
    if len(cur)==3 or re.search(r'[,.?!:]$',w['w']): groups.append(cur);cur=[]
if cur: groups.append(cur)
KEY={'sabia?','pele','minuto.','DMSO.','DMSO','papel,','madeira.','60,','estranho.','alho','boca.','moléculas','barquinho','passageiros','passageiros.','três','magnésio.','pouco','atalho,','poucos.','MSM.','MSM,','curioso.','enxofre','articulações.','antioxidantes.','bloqueia','antioxidante.','cavalos,','veterinários.','FDA','único','bexiga.','tudo','própria.','Salva','lista','segue.'}
caps=[];js=[]
for gi,g in enumerate(groups):
    a=g[0]['s']; b=groups[gi+1][0]['s'] if gi+1<len(groups) else T-0.1
    spans=''.join(f'<span class="{"k" if w["w"] in KEY else ""}" id="c{gi}_{j}">{html.escape(w["w"])}</span> ' for j,w in enumerate(g))
    caps.append(f'<div id="cg{gi}" class="clip cap" data-start="{a:.2f}" data-duration="{b-a:.2f}">{spans}</div>')
    for j,w in enumerate(g): js.append(f'tl.fromTo("#c{gi}_{j}",{{opacity:0.25,y:8}},{{opacity:1,y:0,duration:0.12}},{w["s"]:.2f});')
beads=''.join(f'<i id="bd{i}" style="background:{c}"></i>' for i,c in enumerate(['#E53935','#F4C430','#CBEF4B','#4FC3F7','#B388FF']*3))
for i in range(0): js.append(f'tl.fromTo("#bd{i}",{{scale:0}},{{scale:1,duration:0.18,ease:"back.out(3)"}},{15.4+i*0.16:.2f});')
def hd(id,a,b,inner): return f'<div id="{id}" class="clip hd" data-start="{a}" data-duration="{round(b-a,2)}">{inner}</div>'
rain=""
H=f'''<!doctype html><html lang="pt-BR"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script><style>
@font-face{{font-family:"Bric";src:url("assets/fonts/Bricolage-800.ttf");font-weight:800}}
@font-face{{font-family:"Bric";src:url("assets/fonts/Bricolage-700.ttf");font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}html,body{{width:1080px;height:1920px;overflow:hidden;background:#0E0E0E}}
#root{{position:relative;width:1080px;height:1920px;font-family:"Bric",sans-serif;color:#fff;overflow:hidden}}
#stage{{position:absolute;inset:0;z-index:1}}
#bg{{position:absolute;inset:0;width:1080px;height:1920px;object-fit:cover;z-index:1}}
#shade{{position:absolute;left:0;top:420px;width:1080px;height:1100px;z-index:2;background:linear-gradient(rgba(0,0,0,0) 55%,rgba(0,0,0,.6) 100%)}}
#tsh{{position:absolute;left:0;top:0;width:1080px;height:430px;z-index:3;background:rgba(0,0,0,.55)}} #bsh{{position:absolute;left:0;top:1520px;width:1080px;height:400px;z-index:3;background:rgba(0,0,0,.6)}}
#frame{{position:absolute;inset:26px;z-index:9;border:4px solid #CBEF4B;border-radius:34px;box-shadow:0 0 0 40px #0E0E0E}}
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
.pill b{{color:#CBEF4B}} .pill.v{{border-color:#B388FF}} .pill.v b{{color:#B388FF}}
.big{{font-weight:800;font-size:150px;line-height:1;text-shadow:0 10px 40px rgba(0,0,0,.6)}}
.chips{{display:flex;flex-direction:column;gap:16px;align-items:center}}
.chip{{display:inline-block;background:rgba(14,14,14,.88);border:3px solid #CBEF4B;font-weight:800;font-size:46px;padding:10px 26px;border-radius:16px}}
.arr{{font-weight:800;font-size:60px;color:#CBEF4B}} .beads{{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;background:rgba(14,14,14,.82);padding:18px;border-radius:22px;max-width:760px;margin:0 auto}} .beads i{{display:block;width:62px;height:62px;border-radius:50%;box-shadow:inset -6px -6px 0 rgba(0,0,0,.2)}}
#stamp,#stamp2{{position:absolute;z-index:7;left:0;right:0;top:820px;text-align:center}} #stamp2 span{{display:inline-block;border:8px solid #E53935;color:#fff;background:rgba(14,14,14,.88);font-weight:800;font-size:70px;padding:10px 30px;border-radius:20px;transform:rotate(-5deg)}} #stamp2 b{{color:#E53935}}
#stamp span{{display:inline-block;background:#CBEF4B;color:#141414;font-weight:800;font-size:130px;padding:6px 40px;border-radius:24px;transform:rotate(-4deg);box-shadow:0 20px 60px rgba(0,0,0,.6)}}
#flash{{position:absolute;inset:0;z-index:8;background:#fff;opacity:0}}
#cta{{position:absolute;z-index:6;left:0;right:0;top:1230px;text-align:center}}
#cta span{{display:inline-block;background:#CBEF4B;color:#141414;font-weight:800;font-size:70px;padding:18px 46px;border-radius:60px;box-shadow:0 0 50px rgba(203,239,75,.6)}}
#foot{{position:absolute;z-index:9;top:1800px;left:0;right:0;text-align:center;font-weight:700;font-size:20px;letter-spacing:2px;color:rgba(255,255,255,.75)}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{T}" data-width="1080" data-height="1920">
<video id="bg" class="clip" data-start="0" data-duration="{T}" src="assets/bg.mp4" muted></video>
<div id="shade" class="clip" data-start="0" data-duration="{T}"></div>
<div id="tsh" class="clip" data-start="0" data-duration="{T}"></div><div id="bsh" class="clip" data-start="0" data-duration="{T}"></div>
<div id="vs" class="clip" data-start="0" data-duration="1.0" style="position:absolute;z-index:7;left:0;right:0;top:820px;text-align:center"><span style="display:inline-block;background:#CBEF4B;color:#141414;font-weight:800;font-size:118px;white-space:nowrap;padding:10px 40px;border-radius:28px;transform:rotate(-3deg);box-shadow:0 20px 60px rgba(0,0,0,.6)">Você sabia? 🤔</span></div>
{hd('h0',1.0,6.8,'<div class="m">Atravessa a pele em<br><span>menos de 1 minuto</span> ⏱️</div>')}
<div id="o0" class="clip ov" data-start="2.9" data-duration="2.5" style="top:1120px"><div class="big"><span id="n30">0</span> s</div></div>
<div id="o0b" class="clip ov" data-start="5.4" data-duration="1.4" style="top:1120px"><div class="big" style="font-size:190px;color:#CBEF4B">DMSO</div></div>
{hd('h1',6.8,17.8,'<div class="m">De onde ele<br><span>veio</span>? 🏭</div>')}
<div id="o1" class="clip ov" data-start="7.3" data-duration="8.7"><div class="chips"><span class="pill" id="o1a">🏭 nasceu na <b>fábrica de papel</b></span><span class="pill" id="o1b">🌲 solvente tirado da <b>madeira</b></span><span class="pill" id="o1c">📅 anos 60: um médico <b>começa a estudar</b></span></div></div>
<div id="o1d" class="clip ov" data-start="16.0" data-duration="1.8" style="top:1150px"><span class="chip" style="font-size:64px">🧄 gosto de <b style="color:#CBEF4B">alho</b> na boca!</span></div>
{hd('h2',17.8,24.9,'<div class="m">Ele leva<br><span>passageiros</span> 🚣</div>')}
<div id="o2" class="clip ov" data-start="18.7" data-duration="6.2"><div class="chips"><span class="pill" id="o2a">⛵ DMSO = um <b>barquinho</b></span><span class="pill" id="o2b">carrega <b>outras moléculas</b> pela pele</span></div></div>
{hd('h3',24.9,29.1,'<div class="m"><span>3 passageiros</span><br>famosos</div><div class="s">o que a ciência diz de cada um</div>')}
<div id="o3" class="clip ov" data-start="25.9" data-duration="3.2"><div class="chips" style="flex-direction:row;flex-wrap:wrap;justify-content:center;gap:12px"><span class="chip" id="o3a">🧲 magnésio</span><span class="chip" id="o3b">🦴 MSM</span><span class="chip" id="o3c">🍅 antioxidantes</span></div></div>
{hd('h4',29.1,37.1,'<div class="m"><span>1</span> · Magnésio 🧲</div>')}
<div id="o4" class="clip ov" data-start="30.9" data-duration="6.2"><div class="chips"><span class="pill" id="o4a">sozinho: <b>atravessa pouco</b> a pele</span><span class="pill" id="o4b">DMSO: testado como <b>atalho</b></span><span class="pill v" id="o4c">🔬 estudos <b>ainda são poucos</b></span></div></div>
{hd('h5',37.1,46.7,'<div class="m"><span>2</span> · MSM 🦴</div>')}
<div id="stamp" class="clip" data-start="38.9" data-duration="1.0"><span>CURIOSO…</span></div>
<div id="o5" class="clip ov" data-start="39.9" data-duration="6.8"><div class="chips"><span class="pill" id="o5a">o corpo transforma <b>DMSO → MSM</b></span><span class="pill" id="o5b">composto de <b>enxofre</b> estudado para as articulações</span></div></div>
{hd('h6',46.7,54.1,'<div class="m"><span>3</span> · Antioxidantes 🍅</div>')}
<div id="o6" class="clip ov" data-start="48.8" data-duration="5.3"><div class="chips"><span class="pill v" id="o6a">🧱 a pele <b>bloqueia a maioria</b></span><span class="pill" id="o6b">mas o DMSO <b>já é um antioxidante</b></span></div></div>
{hd('h7',54.1,68.3,'<div class="m">Status pelo <span>mundo</span> 🌎</div>')}
<div id="o7" class="clip ov" data-start="54.1" data-duration="14.2" style="top:1120px"><div class="chips"><span class="pill" id="o7a">🐴 cavalos: <b>uso veterinário</b> há décadas</span><span class="pill" id="o7b">🇺🇸 FDA: <b>1 único uso</b> em pessoas (bexiga)</span><span class="pill v" id="o7c">carrega tudo da pele → <b>não usar por conta própria</b></span></div></div>
{hd('h8',68.3,T,'<div class="m">Salva essa <span>lista</span> 📌</div><div class="s">uma molécula curiosa por dia</div>')}
<div id="cta" class="clip" data-start="69.2" data-duration="{round(T-69.2,2)}"><span>Segue pra mais 🔔</span></div>
{chr(10).join(caps)}
<div id="flash" class="clip" data-start="0" data-duration="{T}"></div>
<div id="frame" class="clip" data-start="0" data-duration="{T}"></div>
<div id="tag" class="clip" data-start="0" data-duration="{T}"><span class="d"></span>OBOLARI ACADEMY<span class="c">· MOLÉCULAS</span></div>
<div id="foot" class="clip" data-start="0" data-duration="{T}">@OBOLARI_ACADEMY · CONTEÚDO EDUCATIVO · NÃO É RECOMENDAÇÃO MÉDICA</div>
</div><script>
const tl=gsap.timeline({{paused:true}});
tl.set("#flash",{{opacity:0}},0);
tl.fromTo("#h0 .m",{{scale:1.6,opacity:0}},{{scale:1,opacity:1,duration:0.3,ease:"power4.out"}},0.0);
tl.fromTo("#flash",{{opacity:0.5}},{{opacity:0,duration:0.25}},0.0);
'''
HS=[('#h0',1.0),('#h1',6.8),('#h2',17.8),('#h3',24.9),('#h4',29.1),('#h5',37.1),('#h6',46.7),('#h7',54.1),('#h8',68.3)]
for h,t in HS:
    H+=f'tl.fromTo("{h}",{{y:30,opacity:0}},{{y:0,opacity:1,duration:0.3,ease:"power3.out"}},{t});\n'
S=json.load(open('scenes.json'))
for s_ in S[1:]:
    if s_[0]!=38.9: H+=f'tl.fromTo("#flash",{{opacity:0.25}},{{opacity:0,duration:0.18}},{s_[0]});\n'
SL=[('#o1a',7.3),('#o1b',8.5),('#o1c',10.4),('#o2a',18.7),('#o2b',19.8),('#o4a',30.9),('#o4b',33.0),('#o4c',35.1),('#o5a',39.9),('#o5b',43.8),('#o6a',48.8),('#o6b',50.7),('#o7a',54.1),('#o7b',57.9),('#o7c',63.7)]
for i,t in SL: H+=f'tl.fromTo("{i}",{{opacity:0,x:200}},{{opacity:1,x:0,duration:0.35,ease:"back.out(1.8)"}},{t});\n'
for i,t in [('#o3a',26.4),('#o3b',26.9),('#o3c',27.4)]:
    H+=f'tl.fromTo("{i}",{{opacity:0,y:-260}},{{opacity:1,y:0,duration:0.45,ease:"bounce.out"}},{t});\n'
for h in ['#h4','#h5','#h6']:
    t=dict(HS)[h]; H+=f'tl.fromTo("{h} .m span",{{scale:2.4}},{{scale:1,duration:0.35,ease:"back.out(2)"}},{t});\n'
H+='''tl.fromTo("#flash",{opacity:0.6},{opacity:0,duration:0.25},0);
tl.fromTo("#vs span",{scale:2.6,opacity:0},{scale:1,opacity:1,duration:0.3,ease:"power4.out"},0.02);
tl.to("#vs",{opacity:0,y:-40,duration:0.15},0.85);
tl.fromTo("#n30",{textContent:0},{textContent:30,duration:1.4,ease:"power2.out",snap:{textContent:1}},3.0);
tl.fromTo("#o0b .big",{scale:2.2,opacity:0},{scale:1,opacity:1,duration:0.3,ease:"power4.out"},5.4);
tl.fromTo("#flash",{opacity:0.6},{opacity:0,duration:0.3},5.4);
tl.fromTo("#o1d span",{scale:0,rotation:-20},{scale:1,rotation:-4,duration:0.4,ease:"back.out(3)"},16.0);
tl.fromTo("#bg",{x:0},{x:-30,duration:0.05,yoyo:true,repeat:5},38.9);
tl.fromTo("#bg",{filter:"grayscale(0) brightness(1)"},{filter:"grayscale(1) brightness(0.6)",duration:0.15},38.9);
tl.to("#bg",{filter:"grayscale(0) brightness(1)",duration:0.2},39.8);
tl.fromTo("#flash",{opacity:0.8},{opacity:0,duration:0.3},38.9);
tl.fromTo("#stamp span",{scale:3,opacity:0},{scale:1,opacity:1,duration:0.25,ease:"power3.in"},38.95);
tl.fromTo("#cta span",{scale:0.6,opacity:0},{scale:1,opacity:1,duration:0.4,ease:"back.out(2.2)"},69.2);
tl.to("#cta span",{scale:1.06,duration:0.45,yoyo:true,repeat:2,ease:"sine.inOut"},69.7);
'''+'\n'.join(js)+'''
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
open('hf/index.html','w').write(H);print('ok',len(groups))
