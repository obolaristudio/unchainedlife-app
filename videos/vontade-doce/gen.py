import json,re,html,random
random.seed(7)
W=json.load(open('vwords.json')); T=73.4
rep={'sobe,':'some,','rin':'rim','pix.':'Pix.','doce.':'doce?','Camundongos':'camundongos','Salve':'Salva','guia,':'GUIA,','Albolari':'Obolari','do':'do'}
words=[]
for i,w in enumerate(W):
    t=rep.get(w['w'],w['w'])
    if w['w']=='mando' : t='mando o'
    if w['w']=='do' and i+1<len(W) and W[i+1]['w']=='sódio': t='o'
    words.append({'w':t,'s':w['s']})
groups=[];cur=[]
for w in words:
    cur.append(w)
    if len(cur)==3 or re.search(r'[,.?!:]$',w['w']): groups.append(cur);cur=[]
if cur: groups.append(cur)
KEY={'sabia?','doce','sua,','elétrico','barriga.','emoção','elétrica.','sódio,','sal,','potássio','bombinha','susto.','metade','cérebro.','moeda','Pix.','conta.','insulina.','alta,','rim','sal.','seis','metade','urina.','doce?','2020,','Nature','camundongos','vago,','calaram','formou.','2014,','bactérias','hipótese','estudo.','notificação.','hora.','Salva','GUIA,'}
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
{hd('h0',0,6.9,'<div class="s"><span style="background:#CBEF4B;color:#141414;padding:2px 14px;border-radius:10px">Você sabia?</span> 🤔</div><div class="m">Sua vontade de doce<br><span>pode não ser sua</span> 🍫</div>')}
<div id="o0" class="clip ov" data-start="3.6" data-duration="3.3"><span class="pill">⚡ pode ser um <b>sinal elétrico</b> vindo da <b>barriga</b></span></div>
{hd('h1',6.9,18.3,'<div class="m">Cada emoção é<br>uma <span>descarga</span> ⚡</div>')}
<div id="o1" class="clip ov" data-start="11.4" data-duration="6.9"><div class="chips"><span class="pill" id="o1a">🧂 <b>sódio (sal)</b> entra no neurônio</span><span class="pill" id="o1b">🍌 <b>potássio</b> sai</span><span class="pill" id="o1c">🔄 uma <b>bombinha</b> põe tudo de volta</span></div></div>
<div id="stamp" class="clip" data-start="18.3" data-duration="1.1"><span>SUSTO:</span></div>
{hd('h2',19.4,28.4,'<div class="m">O sal é a <span>moeda</span><br>do seu cérebro 🪙</div>')}
<div id="o2" class="clip ov" data-start="19.4" data-duration="3.3" style="top:1100px"><div class="big">~<span id="n50">0</span>%</div><span class="pill">da energia do cérebro vai para <b>essa bomba</b></span></div>
<div id="o2b" class="clip ov" data-start="25.1" data-duration="3.3"><span class="pill">💸 como um <b>Pix</b>: o dinheiro não some, <b>muda de conta</b></span></div>
{hd('h3',28.4,38.0,'<div class="m">Insulina alta<br><span>segura sal</span> 🧂</div>')}
<div id="o3" class="clip ov" data-start="29.7" data-duration="8.3" style="top:1080px"><div class="chips"><span class="pill" id="o3a">🫘 o <b>rim</b> retém mais sódio</span><span class="pill" id="o3b">👥 estudo clássico com <b>6 pessoas</b></span><span class="pill v" id="o3c">📉 sódio na urina: <b>quase metade</b></span></div></div>
{hd('h4',38.0,51.0,'<div class="m">E o <span>doce</span>? 🍬</div><div class="s">Nature, 2020 · em camundongos</div>')}
<div id="o4" class="clip ov" data-start="42.5" data-duration="8.5" style="top:1010px"><div class="chips"><span class="pill" id="o4a">🍬 açúcar no intestino <b>acende o nervo vago</b></span><span class="pill" id="o4b">🧵 o fio <b>barriga ⇄ cérebro</b></span><span class="pill v" id="o4c">🔇 fio calado → <b>preferência pelo doce não se formou</b></span></div></div>
{hd('h5',51.0,60.3,'<div class="m">Bactérias com<br><span>fome de doce</span>? 🦠</div>')}
<div id="o5" class="clip ov" data-start="54.2" data-duration="6.1"><div class="chips"><span class="pill" id="o5a">💭 hipótese desde <b>2014</b></span><span class="pill v" id="o5b">🔬 ainda <b>em estudo</b></span></div></div>
{hd('h6',60.3,67.2,'<div class="m">É só uma<br><span>notificação</span> 🔔</div>')}
<div id="o6" class="clip ov" data-start="65.6" data-duration="1.6"><span class="pill">você <b>não precisa responder na hora</b> ✋</span></div>
{hd('h7',67.2,T,'<div class="m">Salva e <span>manda</span> 📤</div><div class="s">pra quem ataca o doce à noite</div>')}
<div id="cta" class="clip" data-start="70.1" data-duration="{round(T-70.1,2)}"><span>Comenta GUIA 📩</span></div>
{chr(10).join(caps)}
<div id="flash" class="clip" data-start="0" data-duration="{T}"></div>
<div id="frame" class="clip" data-start="0" data-duration="{T}"></div>
<div id="tag" class="clip" data-start="0" data-duration="{T}"><span class="d"></span>OBOLARI ACADEMY<span class="c">· CÉREBRO & INTESTINO</span></div>
<div id="foot" class="clip" data-start="0" data-duration="{T}">@OBOLARI_ACADEMY · CONTEÚDO EDUCATIVO · NÃO É RECOMENDAÇÃO MÉDICA</div>
</div><script>
const tl=gsap.timeline({{paused:true}});
tl.set("#flash",{{opacity:0}},0);
tl.fromTo("#h0 .m",{{scale:1.6,opacity:0}},{{scale:1,opacity:1,duration:0.3,ease:"power4.out"}},0.0);
tl.fromTo("#flash",{{opacity:0.5}},{{opacity:0,duration:0.25}},0.0);
'''
HS=[('#h1',6.9),('#h2',19.4),('#h3',28.4),('#h4',38.0),('#h5',51.0),('#h6',60.3),('#h7',67.2)]
for h,t in HS:
    H+=f'tl.fromTo("{h}",{{y:30,opacity:0}},{{y:0,opacity:1,duration:0.3,ease:"power3.out"}},{t});\n'
S=json.load(open('scenes.json'))
for s_ in S[1:]:
    if s_[0]!=18.3: H+=f'tl.fromTo("#flash",{{opacity:0.22}},{{opacity:0,duration:0.16}},{s_[0]});\n'
SL=[('#o0',3.6),('#o1a',11.4),('#o1b',13.9),('#o1c',15.5),('#o2b',25.1),('#o3a',29.7),('#o3b',32.1),('#o3c',35.2),('#o4a',42.5),('#o4b',45.1),('#o4c',47.3),('#o5a',54.2),('#o5b',58.8),('#o6',65.6)]
for i,t in SL: H+=f'tl.fromTo("{i}",{{opacity:0,x:200}},{{opacity:1,x:0,duration:0.32,ease:"back.out(1.8)"}},{t});\n'
H+='''tl.fromTo("#flash",{opacity:0.6},{opacity:0,duration:0.25},0);
tl.fromTo("#h0 .m",{scale:1.5,opacity:0},{scale:1,opacity:1,duration:0.3,ease:"power4.out"},0.0);
tl.fromTo("#h0 .s",{scale:2,opacity:0},{scale:1,opacity:1,duration:0.25,ease:"back.out(2)"},0.0);
tl.fromTo("#bg",{x:0},{x:-30,duration:0.05,yoyo:true,repeat:5},18.3);
tl.fromTo("#bg",{filter:"grayscale(0) brightness(1)"},{filter:"grayscale(1) brightness(0.6)",duration:0.15},18.3);
tl.to("#bg",{filter:"grayscale(0) brightness(1)",duration:0.2},19.3);
tl.fromTo("#flash",{opacity:0.8},{opacity:0,duration:0.3},18.3);
tl.fromTo("#stamp span",{scale:3,opacity:0},{scale:1,opacity:1,duration:0.25,ease:"power3.in"},18.35);
tl.fromTo("#o2 .big",{scale:2.2,opacity:0},{scale:1,opacity:1,duration:0.3,ease:"power4.out"},19.4);
tl.fromTo("#n50",{textContent:0},{textContent:50,duration:1.2,ease:"power2.out",snap:{textContent:1}},19.6);
tl.fromTo("#h6 .m span",{scale:2.4},{scale:1,duration:0.35,ease:"back.out(2)"},60.3);
tl.fromTo("#bg",{x:0},{x:-14,duration:0.05,yoyo:true,repeat:7},64.6);
tl.fromTo("#cta span",{scale:0.6,opacity:0},{scale:1,opacity:1,duration:0.4,ease:"back.out(2.2)"},70.1);
tl.to("#cta span",{scale:1.06,duration:0.45,yoyo:true,repeat:2,ease:"sine.inOut"},70.6);
'''+'\n'.join(js)+'''
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
open('hf/index.html','w').write(H);print('ok',len(groups))
