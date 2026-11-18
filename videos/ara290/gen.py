import json,re,html,random
random.seed(7)
W=json.load(open('vwords.json')); T=81.0
rep={'peptídio':'peptídeo','Obolary':'Obolari','guia,':'GUIA,','2,':'2,'}
words=[];skip=set()
for i,w in enumerate(W):
    if i in skip: continue
    t=rep.get(w['w'],w['w'])
    n=W[i+1]['w'] if i+1<len(W) else ''
    if t=='DOP' and n=='em': t='doping no'; skip.add(i+1)
    if t=='AR' and n.startswith('-290'): t='ARA'+n; skip.add(i+1)
    if t=='quebra' and n.startswith('-cabe'): t='quebra'+n; skip.add(i+1)
    words.append({'w':t,'s':w['s']})
groups=[];cur=[]
for w in words:
    cur.append(w)
    if len(cur)==3 or re.search(r'[,.?!:]$',w['w']): groups.append(cur);cur=[]
if cur: groups.append(cur)
KEY={'doping no','nervos.','EPO.','EPO','vermelhos,','oxigênio.','escândalos','duas','funções.','sangue,','reparar','tecidos.','pedacinho','11','quebra-cabeça.','ARA-290,','cibinetida.','surpresa.','sangue.','interruptor','reparo.','manutenção','nervos?','sarcoidose,','finos,','28','córnea','ARA-290.','órfão','Unidos.','fase','2,','nenhum','país.','Antidoping','ARA-290','proibidas','atletas.','Salva','manda','ciência.','GUIA,'} or {'cobre.','cobre,','esquecidos','defesa.','neutrófilos,','soldados','vírus','bactérias','encostar.','58%','infecções.','ferro.','anemia','surpreendente.','Zinco','zinco','roubar','porta','intestino.','espelho.','GHK-Cu,','colágeno.','cérebro,','equilíbrio,','excesso.','fígado,','ostras,','castanhas,','cacau','feijão.','GUIA,'}
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
{hd('h0',0,6.8,'<div class="s">Do doping no ciclismo 🚴</div><div class="m">a um peptídeo que<br><span>protege nervos</span>?</div>')}
{hd('h1',6.8,15.8,'<div class="m">A <span>EPO</span> 🩸</div><div class="s">o motor do doping</div>')}
<div id="o1" class="clip ov" data-start="9.5" data-duration="6.3"><div class="chips"><span class="pill" id="o1a">🔴 mais glóbulos vermelhos = <b>mais oxigênio</b></span><span class="pill" id="o1b">🚴 centro dos <b>maiores escândalos</b> do ciclismo</span></div></div>
{hd('h2',15.8,24.6,'<div class="m">Uma molécula,<br><span>duas funções</span></div>')}
<div id="o2" class="clip ov" data-start="20.2" data-duration="4.4"><div class="chips"><span class="chip" id="o2a" style="border-color:#E53935">🩸 fabricar sangue</span><span class="chip" id="o2b">🛠️ proteger e reparar</span></div></div>
{hd('h3',24.6,35.5,'<div class="m">Só um <span>pedacinho</span> ✂️</div><div class="s">recortado da EPO</div>')}
<div id="o3" class="clip ov" data-start="27.3" data-duration="4.9"><span class="pill"><b>11</b> aminoácidos 🧩 = uma peça do quebra-cabeça</span></div>
<div id="o3b" class="clip ov" data-start="32.2" data-duration="3.3" style="top:1150px"><div class="big" style="font-size:170px">ARA-<span style="color:#CBEF4B">290</span></div><span class="pill" id="o3c">ou <b>cibinetida</b></span></div>
<div id="stamp" class="clip" data-start="35.5" data-duration="1.4"><span>ESPERA…</span></div>
{hd('h4',36.9,45.6,'<div class="m">Não aumenta<br>o <span>sangue</span> 🙅</div>')}
<div id="o4" class="clip ov" data-start="38.6" data-duration="7.0"><div class="chips"><span class="pill" id="o4a">🔌 liga o <b>receptor de reparo</b></span><span class="pill" id="o4b">🛠️ equipe de manutenção ✅</span><span class="pill v" id="o4c">🏭 fábrica de sangue <b>desligada</b></span></div></div>
{hd('h5',45.6,57.3,'<div class="m">E os <span>nervos</span>? 🧠</div>')}
<div id="o5" class="clip ov" data-start="46.6" data-duration="4.3"><span class="pill">sarcoidose: dor nos <b>nervos mais finos</b></span></div>
<div id="o5b" class="clip ov" data-start="51.0" data-duration="6.3" style="top:1080px"><div class="big"><span id="n28">0</span> dias</div><span class="pill" id="o5c">👁️ ↑ fibras nervosas na <b>córnea</b></span><div style="margin-top:10px;font-weight:700;font-size:28px;color:#F2EFE6" id="o5d">Culver et al., 2017</div></div>
{hd('h6',57.3,66.0,'<div class="m">Status pelo <span>mundo</span> 🌎</div>')}
<div id="o6" class="clip ov" data-start="58.7" data-duration="7.3"><div class="chips"><span class="pill" id="o6a">🇺🇸 status de <b>medicamento órfão</b></span><span class="pill" id="o6b">⏸️ parou após a <b>fase 2</b></span><span class="pill v" id="o6c">🌎 <b>não aprovado</b> em nenhum país</span></div></div>
{hd('h7',66.0,75.2,'<div class="m">Curiosidade<br><span>final</span> 🏅</div>')}
<div id="stamp2" class="clip" data-start="72.1" data-duration="3.1"><span>🚫 PROIBIDO PELA <b>WADA</b></span></div>
{hd('h8',75.2,T,'<div class="m">Salva e <span>manda</span> 📤</div><div class="s">pra quem ama ciência</div>')}
<div id="cta" class="clip" data-start="77.6" data-duration="{round(T-77.6,2)}"><span>Comenta GUIA 📩</span></div>
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
for h,t in [('#h1',6.8),('#h2',15.8),('#h3',24.6),('#h4',36.9),('#h5',45.6),('#h6',57.3),('#h7',66.0),('#h8',75.2)]:
    H+=f'tl.fromTo("{h}",{{y:30,opacity:0}},{{y:0,opacity:1,duration:0.3,ease:"power3.out"}},{t});\n'
S=json.load(open('scenes.json'))
for s_ in S[1:]:
    if s_[0] not in (35.5,): H+=f'tl.fromTo("#flash",{{opacity:0.3}},{{opacity:0,duration:0.18}},{s_[0]});\n'
for i,t in [('#o1a',9.5),('#o1b',13.3),('#o2a',20.2),('#o2b',21.8),('#o3',27.3),('#o4a',38.6),('#o4b',42.5),('#o4c',44.1),('#o5',46.6),('#o5c',52.8),('#o6a',58.7),('#o6b',61.2),('#o6c',64.1)]:
    H+=f'tl.fromTo("{i}",{{opacity:0,x:200}},{{opacity:1,x:0,duration:0.35,ease:"back.out(1.8)"}},{t});\n'
H+='''tl.fromTo("#o3b .big",{scale:2.2,opacity:0},{scale:1,opacity:1,duration:0.35,ease:"power4.out"},32.2);
tl.fromTo("#o3c",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},34.2);
tl.fromTo("#flash",{opacity:0.6},{opacity:0,duration:0.3},32.2);
tl.fromTo("#bg",{x:0},{x:-30,duration:0.05,yoyo:true,repeat:5},35.5);
tl.fromTo("#bg",{filter:"grayscale(0) brightness(1)"},{filter:"grayscale(1) brightness(0.6)",duration:0.15},35.5);
tl.to("#bg",{filter:"grayscale(0) brightness(1)",duration:0.2},36.8);
tl.fromTo("#flash",{opacity:0.8},{opacity:0,duration:0.3},35.5);
tl.fromTo("#stamp span",{scale:3,opacity:0},{scale:1,opacity:1,duration:0.25,ease:"power3.in"},35.55);
tl.fromTo("#o5b",{opacity:0},{opacity:1,duration:0.2},51.0);
tl.fromTo("#n28",{textContent:0},{textContent:28,duration:1.2,ease:"power2.out",snap:{textContent:1}},51.2);
tl.fromTo("#o5d",{opacity:0},{opacity:1,duration:0.3},53.5);
tl.fromTo("#stamp2 span",{scale:2.6,opacity:0,rotation:-15},{scale:1,opacity:1,rotation:-5,duration:0.3,ease:"power3.in"},72.1);
tl.fromTo("#bg",{x:0},{x:-20,duration:0.05,yoyo:true,repeat:3},72.4);
tl.fromTo("#cta span",{scale:0.6,opacity:0},{scale:1,opacity:1,duration:0.4,ease:"back.out(2.2)"},77.6);
tl.to("#cta span",{scale:1.06,duration:0.45,yoyo:true,repeat:3,ease:"sine.inOut"},78.1);
'''+'\n'.join(js)+'''
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
open('hf/index.html','w').write(H);print('ok',len(groups))
