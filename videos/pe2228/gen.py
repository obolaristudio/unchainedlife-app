import json,re,html
# Reel PE-22-28 (roteiro do Maxwell ajustado à Regra nº 1). Template: videos/ll37/gen.py
W=json.load(open('vwords.json')); T=69.0
rep={'-2228.':'PE-22-28.','-2228':'PE-22-28','spagin,':'spadin,','spagin':'spadin','TREC':'TREK-1.','Obolary':'Obolari','aqui!':'aqui.'}
words=[]
for i,w in enumerate(W):
    t=w['w']
    if t=='PE' and i+1<len(W) and W[i+1]['w'].startswith('-2228'): continue
    if t=='-1.' and i>0 and W[i-1]['w']=='TREC': continue
    words.append({'w':rep.get(t,t),'s':w['s'] if t not in('-2228.','-2228') else W[i-1]['s']})
groups=[];cur=[]
for w in words:
    cur.append(w)
    if len(cur)==3 or re.search(r'[,.?!:]$',w['w']): groups.append(cur);cur=[]
if cur: groups.append(cur)
KEY={'semanas','camundongos,','quatro','dias.','PE-22-28.','PE-22-28','sete','contas.','spadin,','spadin','TREK-1.','freio,','freio.','quieto.','serotonina','ativos.','2017,','dias,','nado.','hipocampo,','novos.','conexões','23','horas.','sete.','pessoas,','testado.','estudo.','neurônio.','cérebro','Comenta'}
caps=[];js=[]
for gi,g in enumerate(groups):
    a=g[0]['s']; b=groups[gi+1][0]['s'] if gi+1<len(groups) else T-0.1
    spans=''.join(f'<span class="{"k" if w["w"] in KEY else ""}" id="c{gi}_{j}">{html.escape(w["w"])}</span> ' for j,w in enumerate(g))
    caps.append(f'<div id="cg{gi}" class="clip cap" data-start="{a:.2f}" data-duration="{b-a:.2f}">{spans}</div>')
    for j,w in enumerate(g): js.append(f'tl.fromTo("#c{gi}_{j}",{{opacity:0.25,y:8}},{{opacity:1,y:0,duration:0.12}},{w["s"]:.2f});')
beads=''.join(f'<i id="bd{i}"></i>' for i in range(7))
for i in range(7): js.append(f'tl.fromTo("#bd{i}",{{scale:0}},{{scale:1,duration:0.16,ease:"back.out(3)"}},{12.9+i*0.09:.2f});')
sp=''.join(f'<i class="{"g" if i>=10 else ""}"></i>' for i in range(17))
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
.beads.sm i{{width:44px;height:44px;background:#555}} .beads.sm i.g{{background:#3D7BFF}}
.brake{{display:inline-flex;align-items:center;gap:18px;background:#FBFAF6;color:#141414;border:5px solid #141414;box-shadow:10px 10px 0 #141414;border-radius:20px;padding:16px 30px;font-weight:800;font-size:62px;position:relative}}
#bline{{position:absolute;left:-10px;right:-10px;top:50%;height:12px;background:#E53935;transform-origin:left center;transform:scaleX(0) rotate(-8deg)}}
.bars{{display:flex;flex-direction:column;gap:22px;background:rgba(14,14,14,.86);border:3px solid #CBEF4B;border-radius:22px;padding:26px 30px;max-width:900px;margin:0 auto;text-align:left}}
.bar .l{{font-weight:800;font-size:40px;margin-bottom:8px}} .bar .tr{{height:58px;background:rgba(255,255,255,.12);border-radius:12px;overflow:hidden}}
.bar .f{{height:100%;border-radius:12px;transform-origin:left center;display:flex;align-items:center;justify-content:flex-end;padding-right:16px;font-weight:800;font-size:40px;color:#141414}}
#d4{{position:absolute;z-index:7;left:0;right:0;top:880px;text-align:center}}
#d4 span{{display:inline-block;color:#E53935;-webkit-text-stroke:5px #fff;font-weight:800;font-size:210px}}
#clock{{position:absolute;z-index:7;left:0;right:0;top:560px;text-align:center;font-size:200px}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{T}" data-width="1080" data-height="1920">
<video id="bg" class="clip" data-start="0" data-duration="{T}" src="assets/bg.mp4" muted></video>
<div id="shade" class="clip" data-start="0" data-duration="{T}"></div>
{hd('h0',0,3.5,'<div class="s">Antidepressivos costumam levar</div><div class="m" style="font-size:130px"><span>SEMANAS</span> ⏳</div>')}
{hd('h1',3.5,8.4,'<div class="m">Mas em <span>camundongos</span>…</div><div class="s">um peptídeo agiu em</div>')}
<div id="d4" class="clip" data-start="7.45" data-duration="0.95"><span>4 DIAS</span></div>
{hd('h2',8.4,10.6,'<div class="s">o nome dele:</div><div class="m" style="font-size:140px"><span>PE-22-28</span></div>')}
{hd('h3',10.6,14.4,'<div class="m">só <span>7</span> aminoácidos</div><div class="s">um colar de 7 contas 📿</div>')}
<div id="o1" class="clip ov" data-start="12.8" data-duration="1.6"><div class="beads">{beads}</div></div>
{hd('h4',14.4,18.7,'<div class="m">um pedaço do <span>spadin</span></div><div class="s">peptídeo que o próprio corpo produz</div>')}
<div id="o2" class="clip ov" data-start="15.5" data-duration="3.2" style="top:1080px"><div class="beads sm">{sp}</div><div style="margin-top:18px"><span class="pill">spadin: 17 contas → <b>PE-22-28: as 7 do fim</b></span></div></div>
{hd('h5',18.7,29.0,'<div class="m">Como ele <span>age</span>?</div>')}
<div id="o3" class="clip ov" data-start="21.9" data-duration="7.1" style="top:1050px"><div class="brake" id="brk">🛑 TREK-1<span id="bline"></span></div><div style="margin-top:28px"><span class="pill" id="p1">um <b>freio</b> que deixa o neurônio quieto 😴</span></div><div style="margin-top:16px"><span class="pill" id="p2">PE-22-28 <b>solta o freio</b> 🟢</span></div></div>
{hd('h6',29.0,33.9,'<div class="m"><span>Serotonina</span> mais ativa</div><div class="s">com o spadin, em camundongos</div>')}
<div id="o4" class="clip ov" data-start="31.3" data-duration="2.6"><span class="pill">neurônios de <b>serotonina</b> ficaram mais ativos ⚡</span></div>
{hd('h7',33.9,47.4,'<div class="m">Estudo de <span>2017</span> 🐭</div><div class="s">em camundongos</div>')}
<div id="o5" class="clip ov" data-start="34.5" data-duration="3.0" style="top:1080px"><div class="study"><div class="j">FRONTIERS IN PHARMACOLOGY · 2017</div><div class="t">PE 22-28: efeito <mark>antidepressivo</mark> em camundongos</div></div></div>
<div id="o6" class="clip ov" data-start="38.0" data-duration="9.4" style="top:1030px"><div class="chips" style="flex-direction:column;align-items:center"><span class="chip" id="q1">🏊 desistiram menos no teste de nado</span><span class="chip" id="q2">🧠 neurônios novos no hipocampo</span><span class="chip" id="q3" style="border-color:#3D7BFF">🔗 mais conexões <span style="color:#3D7BFF">(em laboratório)</span></span></div></div>
<div id="clock" class="clip" data-start="47.45" data-duration="1.0">⏰</div>
{hd('h8',47.4,52.5,'<div class="m">E tem <span>mais</span>…</div><div class="s">quanto tempo o efeito durou</div>')}
<div id="o7" class="clip ov" data-start="48.3" data-duration="4.2" style="top:1060px"><div class="bars"><div class="bar"><div class="l">spadin</div><div class="tr"><div class="f" id="b1" style="width:30%;background:#888">7 h</div></div></div><div class="bar"><div class="l" style="color:#CBEF4B">PE-22-28</div><div class="tr"><div class="f" id="b2" style="width:100%;background:#CBEF4B"><span id="n23">0</span>&nbsp;h</div></div></div></div></div>
{hd('h9',52.5,55.5,'<div class="m">E em <span>pessoas</span>?</div>')}
<div id="o8" class="clip ov" data-start="53.6" data-duration="1.9"><span class="pill o">ainda <b>não testado</b> · em estudo</span></div>
<div id="sum" class="clip" data-start="55.5" data-duration="4.5"><div id="sa">PE-22-28</div><div id="sb"><span>solta o freio</span></div><div id="sc">do neurônio 🧠</div></div>
{hd('h10',60.0,T,'<div class="m">Qual peptídeo do <span>cérebro</span>?</div><div class="s">conteúdo educativo</div>')}
<div id="cta" class="clip" data-start="65.2" data-duration="{round(T-65.2,2)}"><span>Comenta aqui 💬</span></div>
<div id="handle" class="clip" data-start="65.4" data-duration="{round(T-65.4,2)}"><span>@obolari_academy</span></div>
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
for h,t in [('#h1',3.5),('#h3',10.6),('#h4',14.4),('#h5',18.7),('#h6',29.0),('#h7',33.9),('#h8',47.4),('#h9',52.5),('#h10',60.0)]:
    H+=f'tl.fromTo("{h}",{{y:30,opacity:0}},{{y:0,opacity:1,duration:0.3,ease:"power3.out"}},{t});\n'
S=json.load(open('scenes.json'))
for s_ in S[1:]: H+=f'tl.fromTo("#flash",{{opacity:0.3}},{{opacity:0,duration:0.18}},{s_[0]});\n'
for o,t in [('#o4',31.3),('#o8',53.6)]:
    H+=f'tl.fromTo("{o}",{{opacity:0,x:200}},{{opacity:1,x:0,duration:0.35,ease:"back.out(1.8)"}},{t});\n'
H+='''tl.fromTo("#d4 span",{scale:2.8,opacity:0},{scale:1,opacity:1,duration:0.25,ease:"power4.out"},7.45);
tl.fromTo("#flash",{opacity:0.55},{opacity:0,duration:0.2},7.45);
tl.fromTo("#h2 .m",{scale:2.4,opacity:0},{scale:1,opacity:1,duration:0.28,ease:"power4.out"},8.9);
tl.fromTo("#h2 .s",{opacity:0},{opacity:1,duration:0.2},8.4);
tl.fromTo("#flash",{opacity:0.45},{opacity:0,duration:0.2},8.9);
tl.fromTo("#o2 .beads",{opacity:0},{opacity:1,duration:0.25},15.5);
tl.to("#o2 .beads i:not(.g)",{opacity:0.25,duration:0.3},16.6);
tl.fromTo("#o2 .pill",{opacity:0,y:20},{opacity:1,y:0,duration:0.3,ease:"back.out(2)"},16.6);
tl.fromTo("#brk",{opacity:0,scale:0.4},{opacity:1,scale:1,duration:0.35,ease:"back.out(2.5)"},22.0);
tl.fromTo("#p1",{opacity:0,x:200},{opacity:1,x:0,duration:0.35,ease:"back.out(1.8)"},24.0);
tl.fromTo("#bline",{scaleX:0},{scaleX:1,duration:0.3,ease:"power3.out"},27.75);
tl.to("#brk",{x:-14,duration:0.05,yoyo:true,repeat:5},27.75);
tl.fromTo("#p2",{opacity:0,x:200},{opacity:1,x:0,duration:0.35,ease:"back.out(1.8)"},27.9);
tl.fromTo("#flash",{opacity:0.45},{opacity:0,duration:0.2},27.75);
tl.fromTo("#o5 .study",{opacity:0,y:120,rotation:-6},{opacity:1,y:0,rotation:-2,duration:0.4,ease:"back.out(1.8)"},34.5);
tl.fromTo("#q1",{opacity:0,scale:0.5},{opacity:1,scale:1,duration:0.25,ease:"back.out(2.5)"},38.1);
tl.fromTo("#q2",{opacity:0,scale:0.5},{opacity:1,scale:1,duration:0.25,ease:"back.out(2.5)"},42.4);
tl.fromTo("#q3",{opacity:0,scale:0.5},{opacity:1,scale:1,duration:0.25,ease:"back.out(2.5)"},45.3);
tl.fromTo("#clock",{y:-900,rotation:-30},{y:0,rotation:0,duration:0.55,ease:"bounce.out"},47.45);
tl.fromTo("#bg",{x:0},{x:-24,duration:0.05,yoyo:true,repeat:5},47.95);
tl.fromTo("#flash",{opacity:0.6},{opacity:0,duration:0.25},47.95);
tl.fromTo("#o7",{opacity:0},{opacity:1,duration:0.2},48.3);
tl.fromTo("#b1",{scaleX:0},{scaleX:1,duration:0.6,ease:"power2.out"},48.4);
tl.fromTo("#b2",{scaleX:0},{scaleX:1,duration:1.0,ease:"power2.out"},49.3);
tl.fromTo("#n23",{textContent:0},{textContent:23,duration:1.0,ease:"power2.out",snap:{textContent:1}},49.3);
tl.fromTo("#sa",{opacity:0,x:-300},{opacity:1,x:0,duration:0.3,ease:"back.out(2)"},56.7);
tl.fromTo("#sb",{opacity:0,scale:2.2},{opacity:1,scale:1,duration:0.25,ease:"power4.out"},58.1);
tl.fromTo("#sc",{opacity:0,y:30},{opacity:1,y:0,duration:0.3},59.2);
tl.fromTo("#flash",{opacity:0.5},{opacity:0,duration:0.2},58.1);
tl.fromTo("#cta span",{scale:0.6,opacity:0},{scale:1,opacity:1,duration:0.4,ease:"back.out(2.2)"},65.2);
tl.to("#cta span",{scale:1.06,duration:0.45,yoyo:true,repeat:3,ease:"sine.inOut"},65.7);
tl.fromTo("#handle span",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},65.4);
tl.fromTo("#bg",{scale:1.0},{scale:1.06,duration:'''+str(T)+''',ease:"none"},0);
'''+'\n'.join(js)+'''
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
open('hf/index.html','w').write(H);print('ok',len(groups))
