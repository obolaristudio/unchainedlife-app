import json,re,html,random
random.seed(7)
W=json.load(open('vwords.json')); T=80.5
rep={'encontra.':'conta.','COA':'CoA','malonil':'malonil-','guia,':'GUIA,','Albolari':'Obolari','Química':'química','Vida':'vida','Real':'real'}
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
KEY={'gordura?','2','partes,','química','possível.','glicose','fábrica.','gordura.','vida','real','queimar','combustível.','muito','vários','dias','engorda?','Espera,','sobrando.','insulina,','chave','depósito','guardada','queimado','guardar','junto.','manteiga,','pizza,','frita,','GUIA,'}
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
{hd('h0',0,3.5,'<div class="m">Carboidrato vira<br><span>gordura?</span> 🍞➡️🧈</div>')}
{hd('h1',3.5,7.5,'<div class="m">A resposta tem<br><span>2 partes</span></div><div class="s">e a segunda quase ninguém conta</div>')}
{hd('h2',7.5,15.0,'<div class="m">PARTE 1:<br><span>a química</span> 🧪</div>')}
<div id="sim" class="clip ov" data-start="8.8" data-duration="1.9"><div class="big" style="color:#CBEF4B">SIM ✅</div></div>
<div id="o1" class="clip ov" data-start="10.6" data-duration="4.4"><span class="pill">glicose do <b>pão</b> e do <b>arroz</b> → pode virar gordura</span></div>
{hd('h3',15.0,21.6,'<div class="m">Como uma<br><span>fábrica</span> 🏭</div>')}
<div id="o2" class="clip ov" data-start="15.0" data-duration="6.6"><div class="chips" style="flex-direction:row;flex-wrap:wrap;justify-content:center;gap:10px;align-items:center"><span class="chip" id="f1">🍞 glicose</span><span class="arr" id="a1">➜</span><span class="chip" id="f2">⚙️ malonil-CoA</span><span class="arr" id="a2">➜</span><span class="chip" id="f3" style="border-color:#F4C430">🧈 gordura</span></div></div>
{hd('h4',21.6,30.7,'<div class="m">PARTE 2:<br><span>a vida real</span> 🧍</div>')}
<div id="o3" class="clip ov" data-start="23.4" data-duration="4.8"><span class="pill">o corpo <b>quase não usa</b> essa fábrica 🏭💤</span></div>
<div id="o4" class="clip ov" data-start="28.2" data-duration="2.5"><div class="big">🔥</div><span class="pill">prefere <b>QUEIMAR</b> o carboidrato</span></div>
{hd('h5',30.7,39.3,'<div class="m">Só fabrica muita<br>gordura <span>quando…</span></div>')}
<div id="o5" class="clip ov" data-start="35.0" data-duration="4.3"><span class="pill">você come <b>muito além</b> do que gasta</span><div style="margin-top:14px"><span class="pill">por <b>vários dias seguidos</b> 📅</span></div></div>
{hd('h6',39.3,44.0,'<div class="m">Então carboidrato<br><span>não engorda?</span> 🤔</div>')}
<div id="stamp" class="clip" data-start="41.5" data-duration="2.5"><span>ESPERA…</span></div>
{hd('h7',44.0,54.7,'<div class="m">Efeito <span>poupador</span><br>de gordura</div>')}
<div id="o6" class="clip ov" data-start="44.1" data-duration="4.8"><div class="big">🔋</div><span class="pill">carboidrato = <b>energia do momento</b></span><div style="margin-top:14px" id="o6b"><span class="pill">a gordura do prato <b>fica sobrando</b> 🧈</span></div></div>
<div id="o7" class="clip ov" data-start="50.3" data-duration="4.4"><div class="big" id="keyi">🔑</div><span class="pill"><b>insulina</b> = chave que abre o depósito de gordura</span></div>
{hd('h8',54.7,58.8,'<div class="m"><span>Resultado:</span></div>')}
<div id="o8" class="clip ov" data-start="54.8" data-duration="4.0"><span class="pill">a gordura da comida é <b>guardada</b> com mais facilidade 📦</span></div>
{hd('h9',58.8,66.4,'<div class="m"><span>Resumindo</span> 📝</div>')}
<div id="o9" class="clip ov" data-start="59.6" data-duration="6.8"><div class="chips"><span class="chip" id="v1">🔥 carboidrato extra: mais <b style="color:#CBEF4B">QUEIMADO</b></span><span class="chip" id="v2" style="border-color:#F4C430">📦 ajuda a <b style="color:#F4C430">GUARDAR</b> a gordura que vem junto</span></div></div>
{hd('h10',66.4,71.3,'<div class="m">A dupla do <span>prato</span> 🍽️</div><div class="s">carboidrato + gordura juntos</div>')}
<div id="o10" class="clip ov" data-start="66.4" data-duration="4.9"><div class="chips" style="flex-direction:row;flex-wrap:wrap;justify-content:center;gap:12px"><span class="chip" id="p1">🍞🧈 pão com manteiga</span><span class="chip" id="p2">🍕 pizza</span><span class="chip" id="p3">🍟 batata frita</span></div></div>
{hd('h11',71.3,T,'<div class="m">Salva e <span>manda</span> 📤</div><div class="s">pra quem acha que "carboidrato vira gordura e ponto"</div>')}
<div id="cta" class="clip" data-start="75.4" data-duration="{round(T-75.4,2)}"><span>Comenta GUIA 📩</span></div>
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
for h,t in [('#h1',3.5),('#h2',7.5),('#h3',15.0),('#h4',21.6),('#h5',30.7),('#h6',39.3),('#h7',44.0),('#h8',54.7),('#h9',58.8),('#h10',66.4),('#h11',71.3)]:
    H+=f'tl.fromTo("{h}",{{y:30,opacity:0}},{{y:0,opacity:1,duration:0.3,ease:"power3.out"}},{t});\n'
S=json.load(open('scenes.json'))
for s_ in S[1:]:
    if s_[0] not in (41.5,): H+=f'tl.fromTo("#flash",{{opacity:0.3}},{{opacity:0,duration:0.18}},{s_[0]});\n'
for o,t in [('#o1',10.6),('#o3',23.4),('#o8',54.8)]:
    H+=f'tl.fromTo("{o}",{{opacity:0,x:200}},{{opacity:1,x:0,duration:0.35,ease:"back.out(1.8)"}},{t});\n'
H+='''tl.fromTo("#sim .big",{scale:2.5,opacity:0},{scale:1,opacity:1,duration:0.3,ease:"back.out(2)"},8.8);
tl.fromTo("#f1",{opacity:0,scale:0.4},{opacity:1,scale:1,duration:0.3,ease:"back.out(2.5)"},16.2);
tl.fromTo("#a1",{opacity:0,x:-40},{opacity:1,x:0,duration:0.3},17.2);
tl.fromTo("#f2",{opacity:0,scale:0.4},{opacity:1,scale:1,duration:0.3,ease:"back.out(2.5)"},18.4);
tl.fromTo("#a2",{opacity:0,x:-40},{opacity:1,x:0,duration:0.3},20.2);
tl.fromTo("#f3",{opacity:0,scale:0.4},{opacity:1,scale:1,duration:0.3,ease:"back.out(2.5)"},20.9);
tl.fromTo("#o4 .big",{y:300,scale:0.3,opacity:0},{y:0,scale:1.2,opacity:1,duration:0.4,ease:"back.out(2)"},28.2);
tl.fromTo("#o4 .pill",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},28.5);
tl.fromTo("#o5",{opacity:0,x:200},{opacity:1,x:0,duration:0.35,ease:"back.out(1.8)"},35.0);
tl.fromTo("#o5 > div",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},37.5);
tl.fromTo("#bg",{x:0},{x:-30,duration:0.05,yoyo:true,repeat:5},41.5);
tl.fromTo("#bg",{filter:"grayscale(0) brightness(1)"},{filter:"grayscale(1) brightness(0.6)",duration:0.15},41.5);
tl.to("#bg",{filter:"grayscale(0) brightness(1)",duration:0.2},43.9);
tl.fromTo("#flash",{opacity:0.8},{opacity:0,duration:0.3},41.5);
tl.fromTo("#stamp span",{scale:3,opacity:0},{scale:1,opacity:1,duration:0.25,ease:"power3.in"},41.55);
tl.fromTo("#o6 .big",{scale:0,opacity:0},{scale:1,opacity:1,duration:0.35,ease:"back.out(2.5)"},44.1);
tl.fromTo("#o6 > .pill",{opacity:0},{opacity:1,duration:0.3},44.4);
tl.fromTo("#o6b",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},46.4);
tl.fromTo("#keyi",{x:-700,rotation:-90,opacity:0},{x:0,rotation:0,opacity:1,duration:0.5,ease:"power3.out"},50.3);
tl.to("#keyi",{rotation:90,duration:0.35,ease:"power2.inOut"},53.3);
tl.fromTo("#o7 .pill",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},51.2);
tl.fromTo("#v1",{opacity:0,scale:0.5},{opacity:1,scale:1,duration:0.3,ease:"back.out(2.5)"},59.6);
tl.fromTo("#v2",{opacity:0,scale:0.5},{opacity:1,scale:1,duration:0.3,ease:"back.out(2.5)"},63.3);
tl.fromTo("#p1",{opacity:0,y:-300},{opacity:1,y:0,duration:0.4,ease:"bounce.out"},66.4);
tl.fromTo("#p2",{opacity:0,y:-300},{opacity:1,y:0,duration:0.4,ease:"bounce.out"},67.4);
tl.fromTo("#p3",{opacity:0,y:-300},{opacity:1,y:0,duration:0.4,ease:"bounce.out"},68.0);
tl.fromTo("#cta span",{scale:0.6,opacity:0},{scale:1,opacity:1,duration:0.4,ease:"back.out(2.2)"},75.5);
tl.to("#cta span",{scale:1.06,duration:0.45,yoyo:true,repeat:5,ease:"sine.inOut"},76.0);
'''+'\n'.join(js)+'''
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
open('hf/index.html','w').write(H);print('ok',len(groups))
