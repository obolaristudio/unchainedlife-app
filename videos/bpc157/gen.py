import json,re,html,random
random.seed(7)
W=json.load(open('vwords.json')); T=81.5
rep={'vazinhos':'vasinhos','Querem':'Quer','guia':'GUIA','Obolária':'Obolari','Proibidos':'proibidos','Atletas.':'atletas.','Agência':'agência','Mundial':'mundial'}
words=[];skip=set()
for i,w in enumerate(W):
    if i in skip: continue
    t=rep.get(w['w'],w['w'])
    if t=='BPC' and i+1<len(W) and W[i+1]['w'].startswith('-157'): t='BPC'+W[i+1]['w']; skip.add(i+1)
    if t=='Anti' and i+1<len(W) and W[i+1]['w']=='-Doping': t='antidoping'; skip.add(i+1)
    if t=='a' and i+1<len(W) and W[i+1]['w']=='livre': t='alívio'; skip.add(i+1)
    if t=='o' and i+1<len(W) and W[i+1]['w']=='nador': t='na dor'; skip.add(i+1)
    words.append({'w':t,'s':w['s']})
words[-6]['w']=words[-6]['w']  # noop
groups=[];cur=[]
for w in words:
    cur.append(w)
    if len(cur)==3 or re.search(r'[,.?!:]$',w['w']): groups.append(cur);cur=[]
if cur: groups.append(cur)
KEY={'BPC-157?','BPC-157','recuperação.','proteção','corpo.','estômago.','15','contas.','90,','Croácia.','ratos,','tendões,','ligamentos,','músculos','intestino','vasinhos','estradas','pessoas,','11','12','joelho.','surpresa.','antidoping','proibidos','2026,','receita','Anvisa.','GUIA'}
caps=[];js=[]
for gi,g in enumerate(groups):
    a=g[0]['s']; b=groups[gi+1][0]['s'] if gi+1<len(groups) else T-0.1
    spans=''.join(f'<span class="{"k" if w["w"] in KEY else ""}" id="c{gi}_{j}">{html.escape(w["w"])}</span> ' for j,w in enumerate(g))
    caps.append(f'<div id="cg{gi}" class="clip cap" data-start="{a:.2f}" data-duration="{b-a:.2f}">{spans}</div>')
    for j,w in enumerate(g): js.append(f'tl.fromTo("#c{gi}_{j}",{{opacity:0.25,y:8}},{{opacity:1,y:0,duration:0.12}},{w["s"]:.2f});')
beads=''.join(f'<i id="bd{i}" style="background:{c}"></i>' for i,c in enumerate(['#E53935','#F4C430','#CBEF4B','#4FC3F7','#B388FF']*3))
for i in range(15): js.append(f'tl.fromTo("#bd{i}",{{scale:0}},{{scale:1,duration:0.18,ease:"back.out(3)"}},{15.4+i*0.16:.2f});')
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
.beads{{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;background:rgba(14,14,14,.82);padding:18px;border-radius:22px;max-width:760px;margin:0 auto}} .beads i{{display:block;width:62px;height:62px;border-radius:50%;box-shadow:inset -6px -6px 0 rgba(0,0,0,.2)}}
#stamp,#stamp2{{position:absolute;z-index:7;left:0;right:0;top:820px;text-align:center}} #stamp2 span{{display:inline-block;border:8px solid #E53935;color:#fff;background:rgba(14,14,14,.88);font-weight:800;font-size:70px;padding:10px 30px;border-radius:20px;transform:rotate(-5deg)}} #stamp2 b{{color:#E53935}}
#stamp span{{display:inline-block;background:#CBEF4B;color:#141414;font-weight:800;font-size:150px;padding:6px 40px;border-radius:24px;transform:rotate(-4deg);box-shadow:0 20px 60px rgba(0,0,0,.6)}}
#flash{{position:absolute;inset:0;z-index:8;background:#fff;opacity:0}}
#cta{{position:absolute;z-index:6;left:0;right:0;top:1230px;text-align:center}}
#cta span{{display:inline-block;background:#CBEF4B;color:#141414;font-weight:800;font-size:70px;padding:18px 46px;border-radius:60px;box-shadow:0 0 50px rgba(203,239,75,.6)}}
#foot{{position:absolute;z-index:9;top:1800px;left:0;right:0;text-align:center;font-weight:700;font-size:20px;letter-spacing:2px;color:rgba(255,255,255,.75)}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{T}" data-width="1080" data-height="1920">
<video id="bg" class="clip" data-start="0" data-duration="{T}" src="assets/bg.mp4" muted></video>
<div id="shade" class="clip" data-start="0" data-duration="{T}"></div>
{hd('h0',0,3.0,'<div class="s">Você já ouviu falar do</div><div class="m" style="font-size:120px"><span>BPC-157?</span></div>')}
{hd('h1',3.0,6.7,'<div class="m">o peptídeo da<br><span>recuperação</span> 💪</div>')}
{hd('h2',6.7,15.1,'<div class="m">BPC = <span>Body Protection<br>Compound</span></div><div class="s">"composto de proteção do corpo"</div>')}
<div id="o1" class="clip ov" data-start="10.4" data-duration="4.7"><span class="pill">vem de uma proteína do nosso <b>suco do estômago</b> 🧪</span></div>
{hd('h3',15.1,19.0,'<div class="m"><span>15</span> aminoácidos</div><div class="s">um colar de 15 contas 📿</div>')}
<div id="o2" class="clip ov" data-start="15.3" data-duration="3.7"><div class="beads">{beads}</div></div>
{hd('h4',19.0,26.5,'<div class="m">Começou nos anos <span>90</span></div><div class="s">na Croácia 🇭🇷</div>')}
<div id="o3" class="clip ov" data-start="22.4" data-duration="4.1"><span class="pill"><b>centenas</b> de estudos em laboratório e animais 🔬</span></div>
{hd('h5',26.5,37.5,'<div class="m">O que os estudos<br><span>mostraram</span></div>')}
<div id="o4" class="clip ov" data-start="28.8" data-duration="8.7" style="top:1080px"><div class="big" id="mouse" style="font-size:120px">🐭</div><div class="chips" style="margin-top:6px;flex-direction:row;flex-wrap:wrap;justify-content:center;gap:12px"><span class="chip" id="k1">🦵 tendões</span><span class="chip" id="k2">🔗 ligamentos</span><span class="chip" id="k3">💪 músculos</span><span class="chip" id="k4">🌀 intestino</span><span class="chip" id="k5" style="border-color:#B388FF">cicatrizaram <b style="color:#B388FF">mais rápido</b> (em ratos)</span></div></div>
{hd('h6',37.5,46.2,'<div class="m">Como ele <span>age</span>?</div><div class="s">ideia dos cientistas</div>')}
<div id="o5" class="clip ov" data-start="39.6" data-duration="6.6"><span class="pill">novos <b>vasinhos de sangue</b> 🩸</span><div style="margin-top:16px"><span class="pill">= novas <b>estradas</b> de nutrientes 🛣️</span></div></div>
{hd('h7',46.2,54.0,'<div class="m">E em <span>pessoas</span>?</div><div class="s">estudos ainda poucos e pequenos</div>')}
<div id="o6" class="clip ov" data-start="50.2" data-duration="3.8"><div class="big"><span id="n11">0</span> de 12</div><span class="pill">relataram <b>alívio na dor do joelho</b> 🦵</span></div>
<div id="stamp" class="clip" data-start="54.0" data-duration="2.6"><span>ESPERA…</span></div>
{hd('h8',56.6,62.0,'<div class="m">Tão famoso que…</div>')}
<div id="stamp2" class="clip" data-start="56.9" data-duration="5.1"><span>🏅 <b>PROIBIDO</b><br>no esporte</span><div style="margin-top:20px"><span class="pill">agência mundial <b>antidoping</b> (WADA)</span></div></div>
{hd('h9',62.0,71.4,'<div class="m">Novidade 🇺🇸</div><div class="s">outubro de 2026</div>')}
<div id="o7" class="clip ov" data-start="65.3" data-duration="6.1"><span class="pill">EUA: farmácias de manipulação<br>podem preparar <b>com receita</b></span></div>
{hd('h10',71.4,T,'<div class="m">E no <span>Brasil</span>? 🇧🇷</div>')}
<div id="o8" class="clip ov" data-start="71.6" data-duration="2.7"><span class="pill">ainda <b>sem registro</b> na Anvisa</span></div>
<div id="cta" class="clip" data-start="76.5" data-duration="{round(T-76.5,2)}"><span>Comenta GUIA 📩</span></div>
{chr(10).join(caps)}
<div id="flash" class="clip" data-start="0" data-duration="{T}"></div>
<div id="frame" class="clip" data-start="0" data-duration="{T}"></div>
<div id="tag" class="clip" data-start="0" data-duration="{T}"><span class="d"></span>OBOLARI ACADEMY<span class="c">· PEPTÍDEOS</span></div>
<div id="foot" class="clip" data-start="0" data-duration="{T}">@OBOLARI_ACADEMY · CONTEÚDO EDUCATIVO · NÃO É RECOMENDAÇÃO MÉDICA</div>
</div><script>
const tl=gsap.timeline({{paused:true}});
tl.set("#flash",{{opacity:0}},0);
tl.fromTo("#h0 .m",{{scale:1.6,opacity:0}},{{scale:1,opacity:1,duration:0.3,ease:"power4.out"}},0.0);
tl.fromTo("#flash",{{opacity:0.5}},{{opacity:0,duration:0.25}},0.0);
'''
for h,t in [('#h1',3.0),('#h2',6.7),('#h3',15.1),('#h4',19.0),('#h5',26.5),('#h6',37.5),('#h7',46.2),('#h8',56.6),('#h9',62.0),('#h10',71.4)]:
    H+=f'tl.fromTo("{h}",{{y:30,opacity:0}},{{y:0,opacity:1,duration:0.3,ease:"power3.out"}},{t});\n'
S=json.load(open('scenes.json'))
for s_ in S[1:]:
    if s_[0]!=54.0: H+=f'tl.fromTo("#flash",{{opacity:0.3}},{{opacity:0,duration:0.18}},{s_[0]});\n'
for o,t in [('#o1',10.4),('#o2',15.3),('#o3',22.4),('#o7',65.3),('#o8',71.6)]:
    H+=f'tl.fromTo("{o}",{{opacity:0,x:200}},{{opacity:1,x:0,duration:0.35,ease:"back.out(1.8)"}},{t});\n'
H+='''tl.fromTo("#o4",{opacity:0},{opacity:1,duration:0.2},28.8);
tl.fromTo("#mouse",{y:-900,scale:0.5},{y:0,scale:1,duration:0.6,ease:"bounce.out"},28.8);
tl.fromTo("#k1",{opacity:0,scale:0.5},{opacity:1,scale:1,duration:0.25,ease:"back.out(2.5)"},32.1);
tl.fromTo("#k2",{opacity:0,scale:0.5},{opacity:1,scale:1,duration:0.25,ease:"back.out(2.5)"},32.9);
tl.fromTo("#k3",{opacity:0,scale:0.5},{opacity:1,scale:1,duration:0.25,ease:"back.out(2.5)"},33.8);
tl.fromTo("#k4",{opacity:0,scale:0.5},{opacity:1,scale:1,duration:0.25,ease:"back.out(2.5)"},35.0);
tl.fromTo("#k5",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},36.0);
tl.fromTo("#o5",{opacity:0},{opacity:1,duration:0.3},39.6);
tl.fromTo("#o5 > div",{opacity:0,x:200},{opacity:1,x:0,duration:0.35,ease:"back.out(1.8)"},41.6);
tl.fromTo("#o6",{opacity:0},{opacity:1,duration:0.2},50.2);
tl.fromTo("#n11",{textContent:0},{textContent:11,duration:1.2,ease:"power2.out",snap:{textContent:1}},50.3);
tl.fromTo("#bg",{x:0},{x:-30,duration:0.05,yoyo:true,repeat:5},54.0);
tl.fromTo("#bg",{filter:"grayscale(0) brightness(1)"},{filter:"grayscale(1) brightness(0.6)",duration:0.15},54.0);
tl.to("#bg",{filter:"grayscale(0) brightness(1)",duration:0.2},56.5);
tl.fromTo("#flash",{opacity:0.8},{opacity:0,duration:0.3},54.0);
tl.fromTo("#stamp span",{scale:3,opacity:0},{scale:1,opacity:1,duration:0.25,ease:"power3.in"},54.05);
tl.fromTo("#stamp2 span",{scale:2.6,opacity:0,rotation:-25},{scale:1,opacity:1,rotation:-5,duration:0.3,ease:"power3.in"},56.9);
tl.fromTo("#stamp2 .pill",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},57.8);
tl.fromTo("#cta span",{scale:0.6,opacity:0},{scale:1,opacity:1,duration:0.4,ease:"back.out(2.2)"},76.6);
tl.to("#cta span",{scale:1.06,duration:0.45,yoyo:true,repeat:5,ease:"sine.inOut"},77.1);
'''+'\n'.join(js)+'''
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
open('hf/index.html','w').write(H);print('ok',len(groups))
