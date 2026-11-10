import json,re,html,random
random.seed(7)
W=json.load(open('vwords.json')); T=51.5
rep={'proantocyanidinas,':'proantocianidinas,','Albolari':'Obolari','guia':'GUIA'}
words=[];skip=False
for i,w in enumerate(W):
    t=rep.get(w['w'],w['w'])
    if t=='a' and i+1<len(W) and W[i+1]['w']=='guia' and i>0 and W[i-1]['w']=='Comenta': continue
    words.append({'w':t,'s':w['s']})
words[-6]['w']=words[-6]['w']  # noop
groups=[];cur=[]
for w in words:
    cur.append(w)
    if len(cur)==3 or re.search(r'[,.?!:]$',w['w']): groups.append(cur);cur=[]
if cur: groups.append(cur)
KEY={'lixo?','casca','resveratrol.','semente','tesouro,','proantocianidinas,','antioxidante.','2006,','camundongos','viveram','espera,','surpresa.','100','garrafas','pequenos,','interessantes.','pressão','açúcar','diabetes','2.','extrato','milagre,','olho','uva.','GUIA'}
caps=[];js=[]
for gi,g in enumerate(groups):
    a=g[0]['s']; b=groups[gi+1][0]['s'] if gi+1<len(groups) else T-0.1
    spans=''.join(f'<span class="{"k" if w["w"] in KEY else ""}" id="c{gi}_{j}">{html.escape(w["w"])}</span> ' for j,w in enumerate(g))
    caps.append(f'<div id="cg{gi}" class="clip cap" data-start="{a:.2f}" data-duration="{b-a:.2f}">{spans}</div>')
    for j,w in enumerate(g): js.append(f'tl.fromTo("#c{gi}_{j}",{{opacity:0.25,y:8}},{{opacity:1,y:0,duration:0.12}},{w["s"]:.2f});')
def hd(id,a,b,inner): return f'<div id="{id}" class="clip hd" data-start="{a}" data-duration="{round(b-a,2)}">{inner}</div>'
rain=''.join(f'<span class="drop" id="dr{i}" style="left:{random.randint(60,960)}px;font-size:{random.randint(70,130)}px">🍷</span>' for i in range(16))
for i in range(16): js.append(f'tl.fromTo("#dr{i}",{{y:-300,rotation:{random.randint(-40,40)}}},{{y:{random.randint(1500,2100)},rotation:{random.randint(-120,120)},duration:{random.uniform(1.2,2.2):.2f},ease:"power1.in"}},{23.3+random.uniform(0,2.6):.2f});')
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
.drop{{position:absolute;top:0;z-index:7;line-height:1}}
#stamp{{position:absolute;z-index:7;left:0;right:0;top:820px;text-align:center}}
#stamp span{{display:inline-block;background:#CBEF4B;color:#141414;font-weight:800;font-size:150px;padding:6px 40px;border-radius:24px;transform:rotate(-4deg);box-shadow:0 20px 60px rgba(0,0,0,.6)}}
#flash{{position:absolute;inset:0;z-index:8;background:#fff;opacity:0}}
#cta{{position:absolute;z-index:6;left:0;right:0;top:1230px;text-align:center}}
#cta span{{display:inline-block;background:#CBEF4B;color:#141414;font-weight:800;font-size:70px;padding:18px 46px;border-radius:60px;box-shadow:0 0 50px rgba(203,239,75,.6)}}
#foot{{position:absolute;z-index:9;top:1800px;left:0;right:0;text-align:center;font-weight:700;font-size:20px;letter-spacing:2px;color:rgba(255,255,255,.75)}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{T}" data-width="1080" data-height="1920">
<video id="bg" class="clip" data-start="0" data-duration="{T}" src="assets/bg.mp4" muted></video>
<div id="shade" class="clip" data-start="0" data-duration="{T}"></div>
{hd('h0',0,4.4,'<div class="m">A parte mais estudada<br>da uva vai pro <span>lixo?</span> 🗑️</div>')}
{hd('h1',4.4,13.6,'<div class="m">Uva roxa 🍇<br><span>casca + semente</span></div>')}
<div id="o1" class="clip ov" data-start="4.7" data-duration="2.3"><span class="pill v">CASCA → <b>resveratrol</b></span></div>
<div id="o2" class="clip ov" data-start="7.3" data-duration="6.3"><span class="pill">SEMENTE → <b>proantocianidinas</b></span><div style="margin-top:16px"><span class="pill">= um tipo de <b>antioxidante</b> 🛡️</span></div></div>
{hd('h2',13.6,20.9,'<div class="m">Ficou famoso<br>em <span>2006</span></div><div class="s">revista Nature</div>')}
<div id="o3" class="clip ov" data-start="16.3" data-duration="4.6"><div class="big" id="mouse">🐭</div><span class="pill">camundongos + muita gordura → <b>viveram mais</b></span></div>
<div id="stamp" class="clip" data-start="20.9" data-duration="2.0"><span>ESPERA…</span></div>
{hd('h3',22.9,29.0,'<div class="m">Só com <span>vinho</span>?</div>')}
<div id="o4" class="clip ov" data-start="23.2" data-duration="5.8"><div class="big"><span id="cnt">0</span>+ 🍷</div><span class="pill"><b>garrafas por dia</b> para chegar na quantidade dos estudos</span></div>
<div id="rain" class="clip" data-start="23.2" data-duration="5.8" style="position:absolute;inset:0;z-index:7">{rain}</div>
{hd('h4',29.0,38.7,'<div class="m">E em <span>pessoas</span>?</div><div class="s">efeito pequeno, mas interessante</div>')}
<div id="o5" class="clip ov" data-start="33.3" data-duration="5.4"><div class="chips"><span class="chip" id="k1">❤️ pressão: leve melhora</span><span class="chip" id="k2">🩸 açúcar no sangue: leve melhora</span><span class="chip" id="k3" style="border-color:#B388FF">mais visível no <b style="color:#B388FF">diabetes tipo 2</b></span></div></div>
{hd('h5',38.7,43.2,'<div class="m">Extrato da<br><span>semente de uva</span></div>')}
<div id="o6" class="clip ov" data-start="39.4" data-duration="3.8"><span class="pill">❤️ pressão: <b>baixou um pouquinho</b></span></div>
{hd('h6',43.2,T,'<div class="m">Não é <span>milagre</span>…</div><div class="s">mas a ciência está de olho 👀</div>')}
<div id="cta" class="clip" data-start="46.4" data-duration="{round(T-46.4,2)}"><span>Comenta GUIA 📩</span></div>
{chr(10).join(caps)}
<div id="flash" class="clip" data-start="0" data-duration="{T}"></div>
<div id="frame" class="clip" data-start="0" data-duration="{T}"></div>
<div id="tag" class="clip" data-start="0" data-duration="{T}"><span class="d"></span>OBOLARI ACADEMY<span class="c">· LONGEVIDADE</span></div>
<div id="foot" class="clip" data-start="0" data-duration="{T}">@OBOLARI_ACADEMY · CONTEÚDO EDUCATIVO · NÃO É RECOMENDAÇÃO MÉDICA</div>
</div><script>
const tl=gsap.timeline({{paused:true}});
tl.set("#flash",{{opacity:0}},0);
tl.fromTo("#h0 .m",{{scale:1.6,opacity:0}},{{scale:1,opacity:1,duration:0.3,ease:"power4.out"}},0.0);
tl.fromTo("#flash",{{opacity:0.5}},{{opacity:0,duration:0.25}},0.0);
'''
for h,t in [('#h1',4.4),('#h2',13.6),('#h3',22.9),('#h4',29.0),('#h5',38.7),('#h6',43.2)]:
    H+=f'tl.fromTo("{h}",{{y:30,opacity:0}},{{y:0,opacity:1,duration:0.3,ease:"power3.out"}},{t});\n'
S=json.load(open('scenes.json'))
for s in S[1:]:
    if s[0] not in (20.9,): H+=f'tl.fromTo("#flash",{{opacity:0.3}},{{opacity:0,duration:0.18}},{s[0]});\n'
for o,t in [('#o1',4.7),('#o2',7.3),('#o6',39.4)]:
    H+=f'tl.fromTo("{o}",{{opacity:0,x:200}},{{opacity:1,x:0,duration:0.35,ease:"back.out(1.8)"}},{t});\n'
H+='''tl.fromTo("#o2 > div",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},11.0);
tl.fromTo("#o3",{opacity:0},{opacity:1,duration:0.2},16.3);
tl.fromTo("#mouse",{y:-900,scale:0.5},{y:0,scale:1,duration:0.6,ease:"bounce.out"},16.3);
tl.fromTo("#o3 .pill",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},18.2);
tl.to("#bg",{scale:1.0,duration:0.01},0);
tl.fromTo("#bg",{x:0},{x:-30,duration:0.05,yoyo:true,repeat:5},20.9);
tl.fromTo("#bg",{filter:"grayscale(0) brightness(1)"},{filter:"grayscale(1) brightness(0.6)",duration:0.15},20.9);
tl.to("#bg",{filter:"grayscale(0) brightness(1)",duration:0.2},22.8);
tl.fromTo("#flash",{opacity:0.8},{opacity:0,duration:0.3},20.9);
tl.fromTo("#stamp span",{scale:3,opacity:0},{scale:1,opacity:1,duration:0.25,ease:"power3.in"},20.95);
tl.fromTo("#o4",{opacity:0},{opacity:1,duration:0.2},23.2);
tl.fromTo("#cnt",{textContent:0},{textContent:100,duration:4.3,ease:"power2.out",snap:{textContent:1}},23.4);
tl.fromTo("#o4 .pill",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},25.0);
tl.fromTo("#k1",{opacity:0,scale:0.5},{opacity:1,scale:1,duration:0.3,ease:"back.out(2.5)"},34.3);
tl.fromTo("#k2",{opacity:0,scale:0.5},{opacity:1,scale:1,duration:0.3,ease:"back.out(2.5)"},35.1);
tl.fromTo("#k3",{opacity:0,scale:0.5},{opacity:1,scale:1,duration:0.3,ease:"back.out(2.5)"},37.3);
tl.fromTo("#cta span",{scale:0.6,opacity:0},{scale:1,opacity:1,duration:0.4,ease:"back.out(2.2)"},46.5);
tl.to("#cta span",{scale:1.06,duration:0.45,yoyo:true,repeat:5,ease:"sine.inOut"},47.0);
'''+'\n'.join(js)+'''
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
open('hf/index.html','w').write(H);print('ok',len(groups))
