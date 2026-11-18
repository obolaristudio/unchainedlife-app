import json,re,html
W=json.load(open('vwords.json')); T=85.4
rep={'anticristo':'Anticristo','Salve':'Salva','IA':'IA','2':'2','lhe':'-lhe'}
words=[]
for w in W:
    t=rep.get(w['w'],w['w'])
    if t=='-lhe' and words: words[-1]['w']+='-lhe'; continue
    words.append({'w':t,'s':w['s']})
groups=[];cur=[]
for w in words:
    cur.append(w)
    if len(cur)==3 or re.search(r'[,.?!:]$',w['w']): groups.append(cur);cur=[]
if cur: groups.append(cur)
KEY={'Anticristo','artificial?','Bíblia','assustadora.','imagem','fôlego,','fôlego','obedece.','IA','voz','milhões','Apocalipse','13,','15','17,','besta','falasse.','comprar','vender','marca.','Calma,','profecia.','multidões.','tela.','compra,','assiste','acredita.','Algoritmos','perceba.','teste.','40','minutos','desapareceram.','tempo','horas','máquina','controlar.','atenção','agora?','atenção,','vida?','Salva'}
caps=[];js=[]
for gi,g in enumerate(groups):
    a=g[0]['s']; b=groups[gi+1][0]['s'] if gi+1<len(groups) else T-0.1
    spans=''.join(f'<span class="{"k" if w["w"] in KEY else ""}" id="c{gi}_{j}">{html.escape(w["w"])}</span> ' for j,w in enumerate(g))
    caps.append(f'<div id="cg{gi}" class="clip cap" data-start="{a:.2f}" data-duration="{b-a:.2f}">{spans}</div>')
    for j,w in enumerate(g): js.append(f'tl.fromTo("#c{gi}_{j}",{{opacity:0.25,y:8}},{{opacity:1,y:0,duration:0.12}},{w["s"]:.2f});')
def hd(id,a,b,inner): return f'<div id="{id}" class="clip hd" data-start="{a}" data-duration="{round(b-a,2)}">{inner}</div>'
def ov(id,a,b,inner,top=1180): return f'<div id="{id}" class="clip ov" data-start="{a}" data-duration="{round(b-a,2)}" style="top:{top}px">{inner}</div>'
G='#E8B84A'
H=f'''<!doctype html><html lang="pt-BR"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script><style>
@font-face{{font-family:"Bric";src:url("assets/fonts/Bricolage-800.ttf");font-weight:800}}
@font-face{{font-family:"Bric";src:url("assets/fonts/Bricolage-700.ttf");font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}html,body{{width:1080px;height:1920px;overflow:hidden;background:#0A0A0A}}
#root{{position:relative;width:1080px;height:1920px;font-family:"Bric",sans-serif;color:#fff;overflow:hidden}}
#bg{{position:absolute;inset:0;width:1080px;height:1920px;object-fit:cover;z-index:1;filter:contrast(1.12) saturate(.7) brightness(.85)}}
#vig{{position:absolute;inset:0;z-index:2;background:radial-gradient(ellipse at 50% 50%,rgba(0,0,0,0) 45%,rgba(0,0,0,.75) 100%)}}
#frame{{position:absolute;inset:26px;z-index:9;border:4px solid {G};border-radius:34px;box-shadow:0 0 0 40px #0A0A0A,0 0 30px rgba(232,184,74,.35) inset}}
#tag{{position:absolute;z-index:9;top:80px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:16px;font-weight:700;font-size:26px;letter-spacing:8px}}
#tag .d{{width:18px;height:18px;border-radius:50%;background:#E53935;box-shadow:0 0 14px #E53935}}#tag .c{{color:{G}}}
.hd{{position:absolute;z-index:6;left:40px;right:40px;top:150px;height:260px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}}
.hd .s{{font-weight:700;font-size:40px;color:#E9E4D8;margin-top:8px}}
.hd .m{{font-weight:800;font-size:78px;line-height:1.02;letter-spacing:-2px}}
.hd .m span,.hd .s span{{color:{G}}} .hd .m em{{font-style:normal;color:#E53935}}
.cap{{position:absolute;z-index:6;left:60px;right:60px;top:1555px;text-align:center;font-weight:800;font-size:60px;line-height:1.1;letter-spacing:-1px;text-shadow:0 4px 18px rgba(0,0,0,.9)}}
.cap .k{{color:{G}}}
.ov{{position:absolute;z-index:5;left:60px;right:60px;text-align:center}}
.pill{{display:inline-block;background:rgba(10,10,10,.88);border:3px solid {G};font-weight:800;font-size:44px;padding:12px 28px;border-radius:18px}}
.pill b{{color:{G}}} .pill.r{{border-color:#E53935}} .pill.r b{{color:#E53935}}
.row{{display:flex;flex-direction:column;gap:14px;align-items:center}}
.verse{{display:inline-block;max-width:900px;background:linear-gradient(#efe3c4,#d9c79b);color:#2a1d0c;font-family:Georgia,"Times New Roman",serif;font-style:italic;font-size:48px;line-height:1.25;padding:30px 40px;border-radius:10px;box-shadow:0 20px 60px rgba(0,0,0,.7),0 0 0 3px #6b4b1a inset}}
.verse small{{display:block;font-style:normal;font-family:"Bric";font-weight:800;font-size:32px;color:#7a1c12;margin-top:14px;letter-spacing:2px}}
.big{{font-weight:800;font-size:170px;line-height:1;color:#fff;text-shadow:0 0 40px rgba(229,57,53,.7)}}
#stamp{{position:absolute;z-index:7;left:0;right:0;top:830px;text-align:center}}
#stamp span{{display:inline-block;background:{G};color:#141414;font-weight:800;font-size:150px;padding:6px 44px;border-radius:24px;transform:rotate(-4deg);box-shadow:0 20px 60px rgba(0,0,0,.7)}}
#flash{{position:absolute;inset:0;z-index:8;background:#fff;opacity:0}}
#red{{position:absolute;inset:0;z-index:8;background:#E53935;mix-blend-mode:multiply;opacity:0}}
#cta{{position:absolute;z-index:6;left:0;right:0;top:1230px;text-align:center}}
#cta span{{display:inline-block;background:{G};color:#141414;font-weight:800;font-size:70px;padding:18px 46px;border-radius:60px;box-shadow:0 0 50px rgba(232,184,74,.6)}}
#foot{{position:absolute;z-index:9;top:1800px;left:0;right:0;text-align:center;font-weight:700;font-size:20px;letter-spacing:2px;color:rgba(255,255,255,.7)}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{T}" data-width="1080" data-height="1920">
<video id="bg" class="clip" data-start="0" data-duration="{T}" src="assets/bg.mp4" muted></video>
<div id="vig" class="clip" data-start="0" data-duration="{T}"></div>
{hd('h0',0,8.7,'<div class="m">E se o <em>Anticristo</em><br>fosse uma <span>IA</span>?</div><div class="s">uma passagem que muita gente está relendo</div>')}
{ov('o0',6.9,8.7,'<span class="pill r">e ela é <b>assustadora</b> 😨</span>')}
{hd('h1',8.7,16.5,'<div class="m">Um texto de<br><span>2 mil anos</span> 📜</div><div class="s">descreve uma imagem feita pelo homem</div>')}
{ov('o1',12.5,16.5,'<div class="row"><span class="pill" id="a1">💨 ganha <b>fôlego</b></span><span class="pill" id="a2">🗣️ passa a <b>falar</b></span><span class="pill r" id="a3">🙇 e muita gente <b>obedece</b></span></div>',1080)}
{hd('h2',16.5,24.9,'<div class="m">O que uma <span>IA</span><br>faz hoje 🤖</div>')}
{ov('o2',18.4,24.9,'<div class="row"><span class="pill" id="b1">💬 <b>fala</b> com você</span><span class="pill" id="b2">🎙️ <b>imita a voz</b> com segundos de áudio</span><span class="pill" id="b3">👥 conversa com <b>milhões</b> ao mesmo tempo</span></div>',1080)}
{hd('h3',24.9,39.5,'<div class="m">Abre em<br><span>Apocalipse 13</span> 📖</div>')}
{ov('v1',29.4,34.3,'<span class="verse">“Foi-lhe dado comunicar fôlego à imagem da besta, para que a imagem falasse.”<small>APOCALIPSE 13:15</small></span>',1010)}
{ov('v2',35.9,39.5,'<span class="verse">“…ninguém podia comprar ou vender, a não ser quem tivesse a marca.”<small>APOCALIPSE 13:17</small></span>',1040)}
<div id="stamp" class="clip" data-start="39.5" data-duration="1.7"><span>CALMA.</span></div>
{hd('h4',41.2,50.9,'<div class="m">A Bíblia <span>não fala</span><br>de IA</div><div class="s">ninguém pode afirmar que essa é a profecia</div>')}
{ov('o4',45.0,50.9,'<div class="row"><span class="pill" id="d1">mas descreve uma <b>imagem criada pelo homem</b></span><span class="pill r" id="d2">que fala e tem <b>poder sobre multidões</b></span></div>',1180)}
{hd('h5',50.9,60.7,'<div class="m">Quase tudo passa<br>por uma <span>tela</span> 📱</div>')}
{ov('o5',53.6,57.0,'<div class="row"><span class="pill" id="e1">🛒 o que você <b>compra</b></span><span class="pill" id="e2">📺 o que você <b>assiste</b></span><span class="pill" id="e3">🙏 até o que você <b>acredita</b></span></div>',1080)}
{ov('o5b',57.0,60.7,'<span class="pill r">⚙️ <b>algoritmos</b> escolhem por você<br>sem que você perceba</span>',1200)}
{hd('h6',60.7,71.5,'<div class="m">Faz o <span>teste</span> ⏳</div><div class="s">você pega o celular só pra ver a hora…</div>')}
{ov('o6',64.4,66.4,'<div class="big"><span id="n40">0</span> min</div><span class="pill r"><b>desapareceram</b></span>',1050)}
{ov('o6b',66.4,71.5,'<div class="row"><span class="pill" id="g1">“não tenho tempo” 🤔</span><span class="pill r" id="g2">mas passa <b>horas na tela</b></span></div>',1180)}
{hd('h7',71.5,74.2,'<div class="m">A pergunta não é<br>a <span>máquina</span>…</div>')}
{hd('h8',74.2,78.0,'<div class="m">Quem controla<br>a sua <span>atenção</span>?</div><div class="s">agora</div>')}
{hd('h9',78.0,T,'<div class="m">E a sua <span>vida</span>?</div><div class="s">quem está no controle</div>')}
<div id="cta" class="clip" data-start="82.2" data-duration="{round(T-82.2,2)}"><span>Salva e manda 📤</span></div>
{chr(10).join(caps)}
<div id="flash" class="clip" data-start="0" data-duration="{T}"></div>
<div id="red" class="clip" data-start="0" data-duration="{T}"></div>
<div id="frame" class="clip" data-start="0" data-duration="{T}"></div>
<div id="tag" class="clip" data-start="0" data-duration="{T}"><span class="d"></span>APOCALIPSE 13<span class="c">· REFLEXÃO</span></div>
<div id="foot" class="clip" data-start="0" data-duration="{T}">REFLEXÃO · TEXTOS BÍBLICOS: APOCALIPSE 13:15–17</div>
</div><script>
const tl=gsap.timeline({{paused:true}});
tl.set("#flash",{{opacity:0}},0);tl.set("#red",{{opacity:0}},0);
tl.fromTo("#h0 .m",{{scale:1.6,opacity:0}},{{scale:1,opacity:1,duration:0.35,ease:"power4.out"}},0.0);
tl.fromTo("#red",{{opacity:0.6}},{{opacity:0,duration:0.5}},0.3);
tl.fromTo("#h0 em",{{x:-8}},{{x:8,duration:0.05,yoyo:true,repeat:7}},0.3);
tl.fromTo("#h0 .s",{{opacity:0}},{{opacity:1,duration:0.3}},3.6);
tl.fromTo("#o0",{{scale:0.5,opacity:0}},{{scale:1,opacity:1,duration:0.3,ease:"back.out(2)"}},6.9);
'''
for h,t in [('#h1',8.7),('#h2',16.5),('#h3',24.9),('#h4',41.2),('#h5',50.9),('#h6',60.7),('#h7',71.5),('#h8',74.2),('#h9',78.0)]:
    H+=f'tl.fromTo("{h}",{{y:30,opacity:0}},{{y:0,opacity:1,duration:0.35,ease:"power3.out"}},{t});\n'
S=json.load(open('scenes.json'))
for s_ in S[1:]:
    if s_[0] not in (39.5,41.2): H+=f'tl.fromTo("#flash",{{opacity:0.22}},{{opacity:0,duration:0.18}},{s_[0]});\n'
for ids,ts in [(['#a1','#a2','#a3'],[12.6,13.6,14.8]),(['#b1','#b2','#b3'],[18.4,19.7,22.2]),(['#d1','#d2'],[45.0,47.6]),(['#e1','#e2','#e3'],[53.6,54.5,56.0]),(['#g1','#g2'],[66.4,69.8])]:
    for i,t in zip(ids,ts): H+=f'tl.fromTo("{i}",{{opacity:0,x:220}},{{opacity:1,x:0,duration:0.35,ease:"back.out(1.8)"}},{t});\n'
H+='''tl.fromTo("#v1 .verse",{opacity:0,rotation:-3,y:60},{opacity:1,rotation:0,y:0,duration:0.5,ease:"power3.out"},29.4);
tl.fromTo("#v2 .verse",{opacity:0,rotation:3,y:60},{opacity:1,rotation:0,y:0,duration:0.5,ease:"power3.out"},35.9);
tl.fromTo("#red",{opacity:0.45},{opacity:0,duration:0.6},38.9);
tl.fromTo("#bg",{x:0},{x:-30,duration:0.05,yoyo:true,repeat:5},39.5);
tl.fromTo("#bg",{filter:"contrast(1.12) saturate(.7) brightness(.85)"},{filter:"grayscale(1) brightness(0.5)",duration:0.15},39.5);
tl.to("#bg",{filter:"contrast(1.12) saturate(.7) brightness(.85)",duration:0.25},41.0);
tl.fromTo("#flash",{opacity:0.8},{opacity:0,duration:0.3},39.5);
tl.fromTo("#stamp span",{scale:3,opacity:0},{scale:1,opacity:1,duration:0.25,ease:"power3.in"},39.55);
tl.fromTo("#o5b",{opacity:0,scale:0.6},{opacity:1,scale:1,duration:0.3,ease:"back.out(2)"},57.0);
tl.fromTo("#o6",{opacity:0},{opacity:1,duration:0.15},64.4);
tl.fromTo("#n40",{textContent:0},{textContent:40,duration:0.9,ease:"power2.out",snap:{textContent:1}},64.4);
tl.fromTo("#red",{opacity:0.5},{opacity:0,duration:0.5},65.2);
tl.fromTo("#h8 .m",{scale:1.15},{scale:1,duration:3.5,ease:"none"},74.2);
tl.fromTo("#cta span",{scale:0.6,opacity:0},{scale:1,opacity:1,duration:0.4,ease:"back.out(2.2)"},82.2);
tl.to("#cta span",{scale:1.06,duration:0.45,yoyo:true,repeat:3,ease:"sine.inOut"},82.7);
'''+'\n'.join(js)+'''
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
open('hf/index.html','w').write(H);print('ok',len(groups))
