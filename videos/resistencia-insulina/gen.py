import json,re,html,random
random.seed(7)
W=json.load(open('vwords.json')); T=136.3
rep={'Roma.':'HOMA.','Albolária':'Obolari','Salve':'Salva','guia,':'GUIA,'}
words=[]
for i,w in enumerate(W):
    t=rep.get(w['w'],w['w'])
    if w['w'] in ('insulina.','insulina,','insulina') and i>0 and W[i-1]['w']=='resistência': t='à '+t
    words.append({'w':t,'s':w['s']})
groups=[];cur=[]
for w in words:
    cur.append(w)
    if len(cur)==3 or re.search(r'[,.?!:]$',w['w']): groups.append(cur);cur=[]
if cur: groups.append(cur)
KEY={'10','escondido','normal.','fígado,','pressão','policístico','cérebro.','à insulina.','à insulina,','à insulina','chave.','porta','energia.','fechadura','emperrar.','pâncreas','forçar','traiçoeira.','normal,','dobrado.','todo.','gordura.','esteatose.','sal','sobe.','masculinos.','policístico.','Alzheimer.','3.','hipótese,','barriga.','comer.','doce','axilas.','jejum','HOMA.','notícia.','açúcar','proteína,','verduras','fibras.','picos','força.','músculo','segunda','bem.','noite','pausas','beliscar','baixar.','mágico.','Salva','manda','GUIA,'}
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
#stamp span{{display:inline-block;background:#CBEF4B;color:#141414;font-weight:800;font-size:150px;padding:6px 40px;border-radius:24px;transform:rotate(-4deg);box-shadow:0 20px 60px rgba(0,0,0,.6)}}
#flash{{position:absolute;inset:0;z-index:8;background:#fff;opacity:0}}
#cta{{position:absolute;z-index:6;left:0;right:0;top:1230px;text-align:center}}
#cta span{{display:inline-block;background:#CBEF4B;color:#141414;font-weight:800;font-size:70px;padding:18px 46px;border-radius:60px;box-shadow:0 0 50px rgba(203,239,75,.6)}}
#foot{{position:absolute;z-index:9;top:1800px;left:0;right:0;text-align:center;font-weight:700;font-size:20px;letter-spacing:2px;color:rgba(255,255,255,.75)}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{T}" data-width="1080" data-height="1920">
<video id="bg" class="clip" data-start="0" data-duration="{T}" src="assets/bg.mp4" muted></video>
<div id="shade" class="clip" data-start="0" data-duration="{T}"></div>
<div id="tsh" class="clip" data-start="0" data-duration="{T}"></div><div id="bsh" class="clip" data-start="0" data-duration="{T}"></div>
{hd('h0',0,12.2,'<div class="s">pode ficar 10+ anos escondido 🕵️</div><div class="m">O problema que o<br><span>exame não mostra</span></div>')}
<div id="o0" class="clip ov" data-start="6.9" data-duration="5.3"><div class="chips" style="flex-direction:row;flex-wrap:wrap;justify-content:center;gap:12px"><span class="chip" id="o0a">🫀 fígado</span><span class="chip" id="o0b">🩺 pressão</span><span class="chip" id="o0c">🌸 ovários</span><span class="chip" id="o0d">🧠 cérebro</span></div></div>
{hd('h1',12.2,14.6,'<div class="m" style="font-size:96px">Resistência<br>à <span>insulina</span></div>')}
{hd('h2',14.6,24.9,'<div class="m">A insulina é<br>uma <span>chave</span> 🔑</div>')}
<div id="o2" class="clip ov" data-start="19.1" data-duration="5.8"><div class="chips"><span class="pill" id="o2a">🍞 comida → <b>glicose no sangue</b></span><span class="pill" id="o2b">🔑 insulina <b>abre a porta</b> da célula</span><span class="pill" id="o2c">⚡ glicose vira <b>energia</b></span></div></div>
{hd('h3',24.9,34.1,'<div class="m">A fechadura<br><span>emperra</span> 🔒</div>')}
<div id="o3" class="clip ov" data-start="27.8" data-duration="6.3"><div class="chips"><span class="pill v" id="o3a">🙅 as células <b>respondem mal</b></span><span class="pill" id="o3b">🏭 pâncreas fabrica <b>cada vez mais insulina</b></span></div></div>
{hd('h4',34.1,44.4,'<div class="m">Por que ela é<br><span>traiçoeira</span> 🕵️</div>')}
<div id="o4" class="clip ov" data-start="39.6" data-duration="4.8"><div class="chips"><span class="chip" id="o4a" style="font-size:54px">Glicose: <b style="color:#CBEF4B">normal ✅</b></span><span class="chip" id="o4b" style="font-size:54px;border-color:#E53935">Insulina: <b style="color:#FF6B5E">lá em cima ⚠️</b></span></div></div>
{hd('h5',44.4,73.1,'<div class="m">Aparece no<br><span>corpo todo</span></div>')}
<div id="o5a" class="clip ov" data-start="46.8" data-duration="3.5"><span class="pill">🫀 <b>Fígado</b>: acumula gordura (esteatose)</span></div>
<div id="o5b" class="clip ov" data-start="50.3" data-duration="5.4"><div class="chips"><span class="pill">🩺 <b>Vasos</b>: + sal retido, − relaxamento</span><span class="pill v" id="o5b2">→ a <b>pressão sobe</b> 📈</span></div></div>
<div id="o5c" class="clip ov" data-start="55.7" data-duration="6.5"><div class="chips"><span class="pill">🌸 <b>Ovários</b>: + hormônios masculinos</span><span class="pill v" id="o5c2">→ ligado à <b>SOP</b></span></div></div>
<div id="o5d" class="clip ov" data-start="62.2" data-duration="10.9"><div class="chips"><span class="pill">🧠 <b>Cérebro</b>: ligação estudada com Alzheimer</span><span class="pill v" id="o5d2">“diabetes tipo 3” = <b>ainda hipótese</b> 🔬</span></div></div>
<div id="stamp" class="clip" data-start="73.1" data-duration="1.5"><span>ESPERA…</span></div>
{hd('h6',74.6,89.9,'<div class="m">Como saber se<br><span>você tem</span>? 🔎</div>')}
<div id="o6" class="clip ov" data-start="76.8" data-duration="7.5" style="top:1110px"><div class="chips" style="align-items:flex-start;max-width:900px;margin:0 auto"><span class="pill" id="o6a">☑️ gordura na <b>barriga</b></span><span class="pill" id="o6b">☑️ <b>sono pesado</b> depois de comer</span><span class="pill" id="o6c">☑️ vontade de <b>doce</b> o tempo todo</span><span class="pill" id="o6d">☑️ <b>manchas escuras</b> no pescoço/axilas</span></div></div>
<div id="o6e" class="clip ov" data-start="84.3" data-duration="5.6"><span class="pill">🧪 no exame: <b>insulina em jejum + HOMA-IR</b></span></div>
{hd('h7',89.9,94.4,'<div class="m">A boa<br><span>notícia</span> ✅</div><div class="s">na maioria das pessoas, melhora muito</div>')}
{hd('h8',94.4,102.1,'<div class="m"><span>1</span> · O prato 🥗</div>')}
<div id="o8" class="clip ov" data-start="95.0" data-duration="7.1"><div class="chips"><span class="pill v" id="o8a">− açúcar e <b>farinha branca</b></span><span class="pill" id="o8b">+ <b>proteína, verduras e fibras</b></span><span class="pill" id="o8c">📉 menos <b>picos</b> de glicose e insulina</span></div></div>
{hd('h9',102.1,112.0,'<div class="m"><span>2</span> · Treino de força 💪</div>')}
<div id="o9" class="clip ov" data-start="103.9" data-duration="8.1"><div class="chips"><span class="pill" id="o9a">💪 músculo = <b>maior consumidor de glicose</b></span><span class="pill" id="o9b">🚪 abre uma <b>2ª porta</b>, com menos insulina</span></div></div>
{hd('h10',112.0,117.8,'<div class="m"><span>3</span> · Dormir bem 😴</div>')}
<div id="o10" class="clip ov" data-start="113.3" data-duration="4.5"><span class="pill">1 noite ruim → <b>pior resposta à insulina</b> no dia seguinte</span></div>
{hd('h11',117.8,123.7,'<div class="m"><span>4</span> · Pausas ⏳</div>')}
<div id="o11" class="clip ov" data-start="118.4" data-duration="5.3"><span class="pill">sem beliscar o dia todo → <b>insulina tem tempo de baixar</b></span></div>
{hd('h12',123.7,130.6,'<div class="m">Não existe<br><span>remédio mágico</span></div>')}
<div id="o12" class="clip ov" data-start="126.1" data-duration="4.5"><div class="chips" style="flex-direction:row;flex-wrap:wrap;justify-content:center;gap:12px"><span class="chip" id="o12a">💪 músculo</span><span class="chip" id="o12b">🥗 prato</span><span class="chip" id="o12c">😴 sono</span><span class="chip" id="o12d">⏳ pausas</span></div></div>
{hd('h13',130.6,T,'<div class="m">Salva e <span>manda</span> 📤</div><div class="s">pra quem você ama</div>')}
<div id="cta" class="clip" data-start="132.8" data-duration="{round(T-132.8,2)}"><span>Comenta GUIA 📩</span></div>
{chr(10).join(caps)}
<div id="flash" class="clip" data-start="0" data-duration="{T}"></div>
<div id="frame" class="clip" data-start="0" data-duration="{T}"></div>
<div id="tag" class="clip" data-start="0" data-duration="{T}"><span class="d"></span>OBOLARI ACADEMY<span class="c">· METABOLISMO</span></div>
<div id="foot" class="clip" data-start="0" data-duration="{T}">@OBOLARI_ACADEMY · CONTEÚDO EDUCATIVO · NÃO É RECOMENDAÇÃO MÉDICA</div>
</div><script>
const tl=gsap.timeline({{paused:true}});
tl.set("#flash",{{opacity:0}},0);
tl.fromTo("#h0 .m",{{scale:1.6,opacity:0}},{{scale:1,opacity:1,duration:0.3,ease:"power4.out"}},0.0);
tl.fromTo("#flash",{{opacity:0.5}},{{opacity:0,duration:0.25}},0.0);
'''
HS=[('#h1',12.2),('#h2',14.6),('#h3',24.9),('#h4',34.1),('#h5',44.4),('#h6',74.6),('#h7',89.9),('#h8',94.4),('#h9',102.1),('#h10',112.0),('#h11',117.8),('#h12',123.7),('#h13',130.6)]
for h,t in HS:
    H+=f'tl.fromTo("{h}",{{y:30,opacity:0}},{{y:0,opacity:1,duration:0.3,ease:"power3.out"}},{t});\n'
S=json.load(open('scenes.json'))
for s_ in S[1:]:
    if s_[0] not in (73.1,): H+=f'tl.fromTo("#flash",{{opacity:0.25}},{{opacity:0,duration:0.18}},{s_[0]});\n'
SL=[('#o2a',19.1),('#o2b',20.7),('#o2c',23.6),('#o3a',27.8),('#o3b',29.9),('#o4a',39.7),('#o4b',41.7),('#o5a',46.8),('#o5b',50.3),('#o5b2',54.9),('#o5c',55.7),('#o5c2',59.4),('#o5d',62.2),('#o5d2',69.9),('#o6a',76.8),('#o6b',78.3),('#o6c',80.0),('#o6d',82.1),('#o6e',84.3),('#o8a',95.0),('#o8b',97.2),('#o8c',99.4),('#o9a',103.9),('#o9b',107.6),('#o10',113.3),('#o11',118.4)]
for i,t in SL: H+=f'tl.fromTo("{i}",{{opacity:0,x:200}},{{opacity:1,x:0,duration:0.35,ease:"back.out(1.8)"}},{t});\n'
for i,t in [('#o0a',6.9),('#o0b',8.2),('#o0c',9.3),('#o0d',10.6),('#o12a',126.1),('#o12b',126.8),('#o12c',127.6),('#o12d',128.3)]:
    H+=f'tl.fromTo("{i}",{{opacity:0,y:-260}},{{opacity:1,y:0,duration:0.45,ease:"bounce.out"}},{t});\n'
for h in ['#h8','#h9','#h10','#h11']:
    t=dict(HS)[h]; H+=f'tl.fromTo("{h} .m span",{{scale:2.4}},{{scale:1,duration:0.35,ease:"back.out(2)"}},{t});\n'
H+='''tl.fromTo("#h1 .m",{scale:1.5,opacity:0},{scale:1,opacity:1,duration:0.3,ease:"power4.out"},12.2);
tl.fromTo("#flash",{opacity:0.6},{opacity:0,duration:0.3},12.2);
tl.to("#o4b",{scale:1.08,duration:0.3,yoyo:true,repeat:3,ease:"sine.inOut"},42.2);
tl.fromTo("#bg",{x:0},{x:-30,duration:0.05,yoyo:true,repeat:5},73.1);
tl.fromTo("#bg",{filter:"grayscale(0) brightness(1)"},{filter:"grayscale(1) brightness(0.6)",duration:0.15},73.1);
tl.to("#bg",{filter:"grayscale(0) brightness(1)",duration:0.2},74.5);
tl.fromTo("#flash",{opacity:0.8},{opacity:0,duration:0.3},73.1);
tl.fromTo("#stamp span",{scale:3,opacity:0},{scale:1,opacity:1,duration:0.25,ease:"power3.in"},73.15);
tl.fromTo("#cta span",{scale:0.6,opacity:0},{scale:1,opacity:1,duration:0.4,ease:"back.out(2.2)"},132.8);
tl.to("#cta span",{scale:1.06,duration:0.45,yoyo:true,repeat:3,ease:"sine.inOut"},133.3);
'''+'\n'.join(js)+'''
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
open('hf/index.html','w').write(H);print('ok',len(groups))
