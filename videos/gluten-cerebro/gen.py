import json,re,html,random
random.seed(7)
W=json.load(open('vwords.json')); T=72.0
rep={'afrocha':'afrouxa','nevoa':'névoa','guia,':'GUIA,','Obolary':'Obolari','o':'o'}
words=[]
for i,w in enumerate(W):
    t=rep.get(w['w'],w['w'])
    if w['w']=='o' and i+1<len(W) and W[i+1]['w']=='trigo' and W[i-1]['w']=='faltou': continue
    if w['w']=='mando': t='mando o'
    words.append({'w':t,'s':w['s']})
groups=[];cur=[]
for w in words:
    cur.append(w)
    if len(cur)==3 or re.search(r'[,.?!:]$',w['w']): groups.append(cur);cur=[]
if cur: groups.append(cur)
KEY={'sabia?','pão','porta','intestino.','cérebro.','zonulina.','Fasano','glúten,','trigo,','junções','zíper.','rápido.','celíaco,','aberta,','ataca','Guerra,','trigo','Dohan','esquizofrenia','caíram.','novo.','Espera,','mental?','Não.','hipótese','100','tem.','névoa','cansaço,','ansiedade','formigamento.','sensibilidade','atenção,','tratamento.','parar','própria.','exame','resultado.','Salva','GUIA,'}
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
{hd('h0',0,6.8,'<div class="s"><span style="background:#CBEF4B;color:#141414;padding:2px 14px;border-radius:10px">Você sabia?</span> 🤔</div><div class="m">Um pão pode abrir<br>uma <span>porta</span> no intestino 🍞</div>')}
<div id="o0" class="clip ov" data-start="3.9" data-duration="2.9"><span class="pill">🧠 e tem cientista estudando se <b>chega ao cérebro</b></span></div>
{hd('h1',6.8,17.7,'<div class="m">A porta se chama<br><span>zonulina</span> 🚪</div>')}
<div id="o1" class="clip ov" data-start="9.0" data-duration="8.7"><div class="chips"><span class="pill" id="o1a">🔬 descoberta de <b>Alessio Fasano</b></span><span class="pill" id="o1b">🌾 o <b>glúten</b> ativa a zonulina</span><span class="pill" id="o1c">🤐 as células se afastam, como <b>abrir um zíper</b></span></div></div>
{hd('h2',17.7,24.9,'<div class="m">Abre e <span>fecha</span>…<br>na maioria</div>')}
<div id="o2" class="clip ov" data-start="20.6" data-duration="4.3"><span class="pill v">no <b>celíaco</b>, ela fica aberta e o corpo <b>ataca o intestino</b></span></div>
{hd('h3',24.9,35.2,'<div class="m">O mistério<br>da <span>guerra</span> 📜</div>')}
<div id="o3" class="clip ov" data-start="26.6" data-duration="8.6" style="top:1060px"><div class="chips"><span class="pill" id="o3a">🌾 faltou <b>trigo</b> na 2ª Guerra</span><span class="pill" id="o3b">🏥 internações por esquizofrenia <b>caíram</b> 📉</span><span class="pill" id="o3c">🍞 o pão voltou → <b>subiram de novo</b> 📈</span><div style="margin-top:6px;font-weight:700;font-size:28px;color:#F2EFE6" id="o3d">observação do Dr. Curtis Dohan</div></div></div>
<div id="stamp" class="clip" data-start="35.2" data-duration="1.4"><span>ESPERA…</span></div>
{hd('h4',36.6,41.1,'<div class="m">Isso <span>prova</span><br>alguma coisa?</div>')}
<div id="o4" class="clip ov" data-start="38.1" data-duration="3.0" style="top:1100px"><div class="big" style="color:#FF6B5E">NÃO.</div><span class="pill">é uma <b>hipótese</b> estudada até hoje 🔬</span></div>
{hd('h5',41.1,54.7,'<div class="m">O que já<br>se <span>sabe</span> ✅</div>')}
<div id="o5" class="clip ov" data-start="42.2" data-duration="5.2" style="top:1100px"><div class="big"><span style="color:#CBEF4B">1</span> em 100</div><span class="pill">tem doença celíaca, e <b>muita gente nem sabe</b></span></div>
<div id="o5b" class="clip ov" data-start="47.4" data-duration="4.5"><div class="chips" style="flex-direction:row;flex-wrap:wrap;justify-content:center;gap:12px"><span class="chip" id="o5c">🌫️ névoa mental</span><span class="chip" id="o5d">😴 cansaço</span><span class="chip" id="o5e">😰 ansiedade</span><span class="chip" id="o5f">✋ formigamento</span></div></div>
<div id="o5g" class="clip ov" data-start="51.9" data-duration="2.8"><span class="pill">e há quem tenha <b>sensibilidade ao glúten</b> sem ser celíaco</span></div>
<div id="stamp2" class="clip" data-start="54.7" data-duration="1.4"><span>⚠️ MAS <b>ATENÇÃO</b></span></div>
{hd('h6',56.1,65.4,'<div class="m">Nada disso<br><span>substitui tratamento</span></div>')}
<div id="o6" class="clip ov" data-start="57.7" data-duration="7.7"><div class="chips"><span class="pill v" id="o6a">💊 ninguém deve <b>parar remédio</b> por conta própria</span><span class="pill" id="o6b">🧪 antes de tirar o glúten: <b>exame de celíaca</b></span><span class="pill" id="o6c">a dieta pode <b>esconder o resultado</b></span></div></div>
{hd('h7',65.4,T,'<div class="m">Salva e <span>manda</span> 📤</div><div class="s">pra quem vive com a barriga e a cabeça pesadas</div>')}
<div id="cta" class="clip" data-start="68.7" data-duration="{round(T-68.7,2)}"><span>Comenta GUIA 📩</span></div>
{chr(10).join(caps)}
<div id="flash" class="clip" data-start="0" data-duration="{T}"></div>
<div id="frame" class="clip" data-start="0" data-duration="{T}"></div>
<div id="tag" class="clip" data-start="0" data-duration="{T}"><span class="d"></span>OBOLARI ACADEMY<span class="c">· INTESTINO & CÉREBRO</span></div>
<div id="foot" class="clip" data-start="0" data-duration="{T}">@OBOLARI_ACADEMY · CONTEÚDO EDUCATIVO · NÃO É RECOMENDAÇÃO MÉDICA</div>
</div><script>
const tl=gsap.timeline({{paused:true}});
tl.set("#flash",{{opacity:0}},0);
tl.fromTo("#h0 .m",{{scale:1.6,opacity:0}},{{scale:1,opacity:1,duration:0.3,ease:"power4.out"}},0.0);
tl.fromTo("#flash",{{opacity:0.5}},{{opacity:0,duration:0.25}},0.0);
'''
HS=[('#h1',6.8),('#h2',17.7),('#h3',24.9),('#h4',36.6),('#h5',41.1),('#h6',56.1),('#h7',65.4)]
for h,t in HS:
    H+=f'tl.fromTo("{h}",{{y:30,opacity:0}},{{y:0,opacity:1,duration:0.3,ease:"power3.out"}},{t});\n'
S=json.load(open('scenes.json'))
for s_ in S[1:]:
    if s_[0] not in (35.2,54.7): H+=f'tl.fromTo("#flash",{{opacity:0.22}},{{opacity:0,duration:0.16}},{s_[0]});\n'
SL=[('#o0',3.9),('#o1a',9.0),('#o1b',10.9),('#o1c',14.1),('#o2',20.6),('#o3a',26.6),('#o3b',29.1),('#o3c',33.2),('#o3d',29.6),('#o5g',51.9),('#o6a',57.7),('#o6b',59.9),('#o6c',63.3)]
for i,t in SL: H+=f'tl.fromTo("{i}",{{opacity:0,x:200}},{{opacity:1,x:0,duration:0.32,ease:"back.out(1.8)"}},{t});\n'
for i,t in [('#o5c',48.1),('#o5d',49.1),('#o5e',49.7),('#o5f',50.8)]:
    H+=f'tl.fromTo("{i}",{{opacity:0,y:-260}},{{opacity:1,y:0,duration:0.45,ease:"bounce.out"}},{t});\n'
H+='''tl.fromTo("#flash",{opacity:0.6},{opacity:0,duration:0.25},0);
tl.fromTo("#h0 .m",{scale:1.5,opacity:0},{scale:1,opacity:1,duration:0.3,ease:"power4.out"},0.0);
tl.fromTo("#h0 .s",{scale:2,opacity:0},{scale:1,opacity:1,duration:0.25,ease:"back.out(2)"},0.0);
tl.fromTo("#h1 .m span",{scale:2.2},{scale:1,duration:0.35,ease:"back.out(2)"},7.9);
tl.fromTo("#bg",{x:0},{x:-30,duration:0.05,yoyo:true,repeat:5},35.2);
tl.fromTo("#bg",{filter:"grayscale(0) brightness(1)"},{filter:"grayscale(1) brightness(0.6)",duration:0.15},35.2);
tl.to("#bg",{filter:"grayscale(0) brightness(1)",duration:0.2},36.5);
tl.fromTo("#flash",{opacity:0.8},{opacity:0,duration:0.3},35.2);
tl.fromTo("#stamp span",{scale:3,opacity:0},{scale:1,opacity:1,duration:0.25,ease:"power3.in"},35.25);
tl.fromTo("#o4 .big",{scale:2.6,opacity:0},{scale:1,opacity:1,duration:0.3,ease:"power4.out"},38.1);
tl.fromTo("#o5 .big",{scale:2.2,opacity:0},{scale:1,opacity:1,duration:0.3,ease:"power4.out"},42.2);
tl.fromTo("#stamp2 span",{scale:2.6,opacity:0,rotation:-15},{scale:1,opacity:1,rotation:-5,duration:0.3,ease:"power3.in"},54.75);
tl.fromTo("#bg",{x:0},{x:-20,duration:0.05,yoyo:true,repeat:3},55.0);
tl.fromTo("#flash",{opacity:0.6},{opacity:0,duration:0.3},54.7);
tl.fromTo("#cta span",{scale:0.6,opacity:0},{scale:1,opacity:1,duration:0.4,ease:"back.out(2.2)"},68.7);
tl.to("#cta span",{scale:1.06,duration:0.45,yoyo:true,repeat:2,ease:"sine.inOut"},69.2);
'''+'\n'.join(js)+'''
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
open('hf/index.html','w').write(H);print('ok',len(groups))
