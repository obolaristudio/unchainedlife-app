import json,re,html,random
random.seed(7)
W=json.load(open('vwords.json')); T=84.4
rep={'homezartana':'olmesartana','essa':'esse','estamina.':'histamina.','frouxa,':'afrouxa,','testime':'Intestino','Salve':'Salva','enxada':'inchada','Albolária':'Obolari','guia':'GUIA','Guia':'guia','Gratuito':'gratuito','manda':'manda'}
words=[]
for i,w in enumerate(W):
    if w['w']=='3.' and i+1<len(W) and W[i+1]['w']=='Resumo.': continue
    t=rep.get(w['w'],w['w'])
    if w['w']=='Em' and i+1<len(W) and W[i+1]['w']=='testime': continue
    if w['w']=='te' and i+1<len(W) and W[i+1]['w']=='manda' and W[i+2]['w']=='o': t='eu te'
    if w['w']=='manda' and i>0 and W[i-1]['w']=='te': t='mando'
    words.append({'w':t,'s':w['s']})
groups=[];cur=[]
for w in words:
    cur.append(w)
    if len(cur)==3 or re.search(r'[,.?!:]$',w['w']): groups.append(cur);cur=[]
if cur: groups.append(cur)
KEY={'sabia?','pressão','celíaca','intestino.','médicos','estufada,','gases,','fibra.','5','investiga.','1.','remédio.','olmesartana','raros,','diarreia','celíaca.','FDA','sozinho.','médico.','2.','inflamada.','2019,','vivo','minutos,','leite','soja','buracos','3.','Bactérias','histamina.','alergia.','nervos','frouxa.','4.','vazamento.','camada','sangue','inflamação','cansaço,','pele,','cabeça','estresse.','cérebro,','defesa','ciclo.','Estufamento','Salva','GUIA'}
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
{hd('h0',0,7.3,'<div class="s"><span style="background:#CBEF4B;color:#141414;padding:2px 14px;border-radius:10px">Você sabia?</span> 🤔</div><div class="m">Um remédio de <span>pressão</span><br>pode imitar a <span>celíaca</span></div>')}
<div id="o0" class="clip ov" data-start="5.1" data-duration="2.2"><span class="pill v">e a maioria dos médicos <b>não pensa nisso</b> 😮</span></div>
{hd('h1',7.3,16.0,'<div class="m">Barriga <span>estufada</span>? 🎈</div>')}
<div id="o1" class="clip ov" data-start="7.6" data-duration="4.0"><div class="chips" style="flex-direction:row;flex-wrap:wrap;justify-content:center;gap:12px"><span class="chip" id="o1a">🎈 estufamento</span><span class="chip" id="o1b">💨 gases</span><span class="chip" id="o1c">😣 intestino irritado</span></div></div>
<div id="o1d" class="clip ov" data-start="11.6" data-duration="1.0"><span class="pill">“come mais <b>fibra</b>” 🥣</span></div>
<div id="o1e" class="clip ov" data-start="12.6" data-duration="3.4" style="top:1120px"><div class="big"><span style="color:#CBEF4B">5</span> causas</div><span class="pill v">que <b>quase ninguém investiga</b> 🔎</span></div>
{hd('h2',16.0,31.1,'<div class="m"><span>1</span> · O remédio 💊</div>')}
<div id="o2" class="clip ov" data-start="17.3" data-duration="13.8" style="top:990px"><div class="chips"><span class="pill" id="o2a">💊 <b>olmesartana</b> (pressão alta)</span><span class="pill" id="o2b">casos raros: <b>diarreia forte</b></span><span class="pill" id="o2c">🔬 no microscópio: <b>parece celíaca</b></span><span class="pill" id="o2d">🇺🇸 <b>alerta da FDA</b> (2013)</span><span class="pill v" id="o2e">⚠️ nunca pare sozinho: <b>fale com seu médico</b></span></div></div>
{hd('h3',31.1,44.4,'<div class="m"><span>2</span> · A porta inflamada 🚪</div>')}
<div id="o3" class="clip ov" data-start="34.0" data-duration="10.4"><div class="chips"><span class="pill" id="o3a">🎥 2019: intestino <b>filmado ao vivo</b></span><span class="pill" id="o3b">🥛 leite e soja → <b>buracos em minutos</b></span><span class="pill v" id="o3c">em <b>parte</b> dos pacientes com intestino irritável</span></div></div>
{hd('h4',44.4,52.1,'<div class="m"><span>3</span> · Fábrica de histamina 🦠</div>')}
<div id="o4" class="clip ov" data-start="46.9" data-duration="5.2"><div class="chips"><span class="pill" id="o4a">🤧 a mesma <b>da alergia</b></span><span class="pill" id="o4b">⚡ irrita os <b>nervos da barriga</b></span></div></div>
{hd('h5',52.1,65.3,'<div class="m"><span>4</span> · O vazamento 💧</div>')}
<div id="o5" class="clip ov" data-start="53.7" data-duration="5.8"><div class="chips"><span class="pill" id="o5a">🧱 parede = <b>1 camada de células</b></span><span class="pill v" id="o5b">🦠 pedaços de bactéria <b>caem no sangue</b></span></div></div>
<div id="o5c" class="clip ov" data-start="59.5" data-duration="5.8"><div class="chips" style="flex-direction:row;flex-wrap:wrap;justify-content:center;gap:12px"><span class="chip" id="o5d">😴 cansaço</span><span class="chip" id="o5e">🧴 pele</span><span class="chip" id="o5f">🤕 cabeça</span></div></div>
<div id="stamp" class="clip" data-start="63.7" data-duration="1.6"><span style="font-size:96px">LIGA AO INTESTINO!</span></div>
{hd('h6',65.3,75.2,'<div class="m"><span>5</span> · O estresse 🧠</div>')}
<div id="o6" class="clip ov" data-start="66.8" data-duration="8.4"><div class="chips"><span class="pill" id="o6a">🧠 ⇄ 🫃 conversam <b>o tempo todo</b></span><span class="pill" id="o6b">estresse → <b>barriga inflama</b></span><span class="pill v" id="o6c">barriga inflamada → <b>mais estresse</b> 🔁</span></div></div>
{hd('h7',75.2,T,'<div class="m">Não é só<br>falta de <span>fibra</span></div>')}
<div id="cta" class="clip" data-start="78.2" data-duration="{round(T-78.2,2)}"><span>Salva e manda 📤</span></div>
<div id="cta2" class="clip" data-start="81.2" data-duration="{round(T-81.2,2)}" style="position:absolute;z-index:6;left:0;right:0;top:1360px;text-align:center"><span class="pill">📩 comenta <b>GUIA</b></span></div>
{chr(10).join(caps)}
<div id="flash" class="clip" data-start="0" data-duration="{T}"></div>
<div id="frame" class="clip" data-start="0" data-duration="{T}"></div>
<div id="tag" class="clip" data-start="0" data-duration="{T}"><span class="d"></span>OBOLARI ACADEMY<span class="c">· INTESTINO</span></div>
<div id="foot" class="clip" data-start="0" data-duration="{T}">@OBOLARI_ACADEMY · CONTEÚDO EDUCATIVO · NÃO É RECOMENDAÇÃO MÉDICA</div>
</div><script>
const tl=gsap.timeline({{paused:true}});
tl.set("#flash",{{opacity:0}},0);
tl.fromTo("#h0 .m",{{scale:1.6,opacity:0}},{{scale:1,opacity:1,duration:0.3,ease:"power4.out"}},0.0);
tl.fromTo("#flash",{{opacity:0.5}},{{opacity:0,duration:0.25}},0.0);
'''
HS=[('#h1',7.3),('#h2',16.0),('#h3',31.1),('#h4',44.4),('#h5',52.1),('#h6',65.3),('#h7',75.2)]
for h,t in HS:
    H+=f'tl.fromTo("{h}",{{y:30,opacity:0}},{{y:0,opacity:1,duration:0.3,ease:"power3.out"}},{t});\n'
S=json.load(open('scenes.json'))
for s_ in S[1:]:
    if s_[0]!=62.8: H+=f'tl.fromTo("#flash",{{opacity:0.22}},{{opacity:0,duration:0.16}},{s_[0]});\n'
SL=[('#o0',5.1),('#o1d',11.6),('#o2a',17.3),('#o2b',21.6),('#o2c',22.9),('#o2d',25.2),('#o2e',28.4),('#o3a',34.0),('#o3b',40.1),('#o3c',43.0),('#o4a',46.9),('#o4b',48.6),('#o5a',53.7),('#o5b',57.4),('#o6a',66.8),('#o6b',69.2),('#o6c',71.8)]
for i,t in SL: H+=f'tl.fromTo("{i}",{{opacity:0,x:200}},{{opacity:1,x:0,duration:0.32,ease:"back.out(1.8)"}},{t});\n'
for i,t in [('#o1a',7.6),('#o1b',8.4),('#o1c',9.0),('#o5d',61.5),('#o5e',62.3),('#o5f',62.8)]:
    H+=f'tl.fromTo("{i}",{{opacity:0,y:-260}},{{opacity:1,y:0,duration:0.45,ease:"bounce.out"}},{t});\n'
for h in ['#h2','#h3','#h4','#h5','#h6']:
    t=dict(HS)[h]; H+=f'tl.fromTo("{h} .m span",{{scale:2.4}},{{scale:1,duration:0.35,ease:"back.out(2)"}},{t});\n'
H+='''tl.fromTo("#flash",{opacity:0.6},{opacity:0,duration:0.25},0);
tl.fromTo("#h0 .m",{scale:1.5,opacity:0},{scale:1,opacity:1,duration:0.3,ease:"power4.out"},0.0);
tl.fromTo("#h0 .s",{scale:2,opacity:0},{scale:1,opacity:1,duration:0.25,ease:"back.out(2)"},0.0);
tl.fromTo("#o1e .big",{scale:2.2,opacity:0},{scale:1,opacity:1,duration:0.3,ease:"power4.out"},12.6);
tl.fromTo("#flash",{opacity:0.6},{opacity:0,duration:0.3},12.6);
tl.fromTo("#bg",{x:0},{x:-30,duration:0.05,yoyo:true,repeat:5},63.7);
tl.fromTo("#bg",{filter:"grayscale(0) brightness(1)"},{filter:"grayscale(1) brightness(0.6)",duration:0.15},63.7);
tl.to("#bg",{filter:"grayscale(0) brightness(1)",duration:0.2},65.2);
tl.fromTo("#flash",{opacity:0.8},{opacity:0,duration:0.3},63.7);
tl.fromTo("#stamp span",{scale:3,opacity:0},{scale:1,opacity:1,duration:0.25,ease:"power3.in"},63.75);
tl.fromTo("#cta span",{scale:0.6,opacity:0},{scale:1,opacity:1,duration:0.4,ease:"back.out(2.2)"},78.2);
tl.fromTo("#cta2",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},81.2);
'''+'\n'.join(js)+'''
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
open('hf/index.html','w').write(H);print('ok',len(groups))
