import json
from words import norm,captions
# Reel espirulina (estrutura do carrossel de @só verde*, roteiro e imagens originais, fatos checados). Template: videos/ll37/gen.py
T=77.7
W=[w for w in json.load(open('vwords.json')) if w['w']!='Obrigada!']
fix=[]
for i,w in enumerate(W):
    if w['w'].startswith('-') and fix: fix[-1]={'w':fix[-1]['w']+w['w'],'s':fix[-1]['s']}; continue
    fix.append(dict(w))
for w in fix: w['w']=w['w'].replace('Obolary','Obolari').replace('aqui!','aqui.')
words=norm(fix)
KEY={'azul','azul-esverdeado','Terra','espirulina','planta','cianobactéria','fotossíntese','3','bilhões','ficocianina','proteína','metade','essenciais','NASA','espaço','oxigênio','pessoas','colesterol','pressão','câncer','animais','surpresa','B12','pseudo-vitamina','falsa','usar','Comenta'}
caps,js=captions(words,T,KEY)
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
.eq{{display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:14px}} .eq .op{{font-weight:800;font-size:64px;color:#CBEF4B;text-shadow:0 4px 18px rgba(0,0,0,.8)}}
.chip.b{{border-color:#3D7BFF}} .chip.b b{{color:#3D7BFF}} .chip.o{{border-color:#FF8A3D}} .chip.o b{{color:#FF8A3D}} .chip b{{color:#CBEF4B}}
.card{{display:inline-block;max-width:920px;background:rgba(14,14,14,.9);border:3px solid #CBEF4B;border-radius:22px;padding:22px 30px;text-align:center}}
.card .n{{font-weight:800;font-size:72px;color:#CBEF4B;line-height:1}} .card .d{{font-weight:700;font-size:42px;margin-top:10px}} .card .e{{font-weight:700;font-size:36px;margin-top:8px;color:#FF8A3D}}
.stampR{{position:absolute;z-index:7;left:0;right:0;top:820px;text-align:center}}
.stampR span{{display:inline-block;background:#E53935;color:#fff;font-weight:800;font-size:96px;line-height:1.05;padding:14px 40px;border-radius:24px;border:6px solid #141414;transform:rotate(-4deg);box-shadow:14px 14px 0 #141414}}
.stampL{{position:absolute;z-index:7;left:0;right:0;top:760px;text-align:center}}
.stampL span{{display:inline-block;background:#CBEF4B;color:#141414;font-weight:800;font-size:170px;padding:6px 44px;border-radius:24px;border:6px solid #141414;transform:rotate(-3deg);box-shadow:14px 14px 0 #141414}}
.rows{{display:flex;flex-direction:column;gap:16px;align-items:stretch;max-width:940px;margin:0 auto}}
.row{{background:rgba(14,14,14,.9);border:3px solid #CBEF4B;border-radius:18px;padding:14px 24px;font-weight:800;font-size:48px;text-align:left}} .row b{{color:#CBEF4B}}
.cu{{background:#FF8A3D!important;color:#141414!important}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{T}" data-width="1080" data-height="1920">
<video id="bg" class="clip" data-start="0" data-duration="{T}" src="assets/bg.mp4" muted></video>
<div id="shade" class="clip" data-start="0" data-duration="{T}"></div>
{hd('h0',0,8.2,'<div class="s">um dos seres vivos mais antigos da Terra</div><div class="m">e deixa a água <span>azul</span> 💙</div>')}
<div id="nm" class="clip stampL" data-start="7.3" data-duration="0.9"><span style="font-size:130px">ESPIRULINA</span></div>
{hd('h1',8.2,19.5,'<div class="m">Não é <span>planta</span></div><div class="s">é uma cianobactéria 🦠</div>')}
<div id="o1" class="clip ov" data-start="13.4" data-duration="4.2"><span class="pill">faz <b>fotossíntese</b>, como as plantas ☀️</span></div>
<div id="o2" class="clip ov" data-start="17.7" data-duration="1.8" style="top:900px"><div class="big"><span id="n3" style="color:#CBEF4B">0</span> bilhões</div><div class="s" style="font-weight:800;font-size:56px">de anos ⏳</div></div>
{hd('h2',19.5,27.1,'<div class="m">De onde vem o <span>azul</span>?</div><div class="s">um pigmento: ficocianina</div>')}
<div id="o3" class="clip ov" data-start="23.5" data-duration="3.6"><span class="pill" style="border-color:#3D7BFF">pinta a água e <b style="color:#3D7BFF">doces azuis "naturais"</b> 🍬</span></div>
{hd('h3',27.1,35.3,'<div class="m">A fama de <span>proteína</span></div><div class="s">é verdadeira ✅</div>')}
<div id="o4" class="clip ov" data-start="29.3" data-duration="6.0" style="top:960px"><div class="big">+<span id="n50" style="color:#CBEF4B">0</span>%</div><div class="s" style="font-weight:800;font-size:50px;margin-bottom:20px">do peso seco é proteína</div><span class="pill" id="aa">todos os <b>aminoácidos essenciais</b></span></div>
{hd('h4',35.3,42.8,'<div class="m">🚀 A <span>NASA</span> estudou</div><div class="s">comida para missões longas no espaço</div>')}
<div id="o5" class="clip ov" data-start="40.3" data-duration="2.5"><div class="chips"><span class="chip" id="c1">⚡ cresce rápido</span><span class="chip b" id="c2"><b>🫧 produz oxigênio</b></span></div></div>
{hd('h5',42.8,53.0,'<div class="m">E em <span>pessoas</span>?</div><div class="s">estudos pequenos</div>')}
<div id="o6" class="clip ov" data-start="46.7" data-duration="6.3" style="top:1030px"><div class="chips" style="flex-direction:column;align-items:center"><span class="chip" id="p1">📉 colesterol: leve queda</span><span class="chip" id="p2">📉 pressão: leve queda</span><span class="chip o" id="p3"><b>câncer: só laboratório e animais 🐭</b></span></div></div>
<div id="mito" class="clip stampR" data-start="53.0" data-duration="1.6"><span>MITO? 🤔</span></div>
{hd('h6',54.5,64.8,'<div class="m">Espirulina tem <span>B12</span>?</div><div class="s">muita gente acha que sim</div>')}
<div id="fake" class="clip stampR" data-start="60.0" data-duration="4.8"><span>B12 "FALSA" ❌</span></div>
<div id="o7" class="clip ov" data-start="62.9" data-duration="1.9" style="top:1150px"><span class="pill">uma pseudovitamina que <b>o corpo não usa</b></span></div>
<div id="sum" class="clip" data-start="64.8" data-duration="5.1"><div id="sa">Antiga. Rica em proteína.</div><div id="sb"><span>Mas não é fonte de B12.</span></div></div>
{hd('h7',69.9,T,'<div class="m">Você já provou <span>espirulina</span>?</div><div class="s">conteúdo educativo</div>')}
<div id="cta" class="clip" data-start="75.3" data-duration="{round(T-75.3,2)}"><span>Comenta aqui 💬</span></div>
<div id="handle" class="clip" data-start="75.5" data-duration="{round(T-75.5,2)}"><span>@obolari_academy</span></div>
{chr(10).join(caps)}
<div id="flash" class="clip" data-start="0" data-duration="{T}"></div>
<div id="tag" class="clip" data-start="0" data-duration="{T}"><span class="d"></span>OBOLARI ACADEMY<span class="c">· NUTRIÇÃO</span></div>
<div id="foot" class="clip" data-start="0" data-duration="{T}">@OBOLARI_ACADEMY · CONTEÚDO EDUCATIVO · NÃO É RECOMENDAÇÃO MÉDICA</div>
</div><script>
const tl=gsap.timeline({{paused:true}});
tl.set("#flash",{{opacity:0}},0);
tl.fromTo("#h0 .m",{{scale:1.6,opacity:0}},{{scale:1,opacity:1,duration:0.3,ease:"power4.out"}},0.0);
tl.fromTo("#flash",{{opacity:0.5}},{{opacity:0,duration:0.25}},0.0);
'''
for h,t in [('#h1',8.2),('#h2',19.5),('#h3',27.1),('#h4',35.3),('#h5',42.8),('#h6',54.5),('#h7',69.9)]:
    H+=f'tl.fromTo("{h}",{{y:30,opacity:0}},{{y:0,opacity:1,duration:0.3,ease:"power3.out"}},{t});\n'
for s_ in json.load(open('scenes.json'))[1:]: H+=f'tl.fromTo("#flash",{{opacity:0.3}},{{opacity:0,duration:0.18}},{s_[0]});\n'
for o,t in [('#o1',13.4),('#o3',23.5),('#o7',62.9)]:
    H+=f'tl.fromTo("{o}",{{opacity:0,x:200}},{{opacity:1,x:0,duration:0.35,ease:"back.out(1.8)"}},{t});\n'
for k,t in [('#c1',40.38),('#c2',41.6),('#p1',46.8),('#p2',47.72),('#p3',49.3)]:
    H+=f'tl.fromTo("{k}",{{opacity:0,scale:0.4}},{{opacity:1,scale:1,duration:0.26,ease:"back.out(2.5)"}},{t});\n'
H+='''tl.fromTo("#nm span",{scale:2.6,opacity:0},{scale:1,opacity:1,duration:0.25,ease:"power4.out"},7.38);
tl.fromTo("#flash",{opacity:0.5},{opacity:0,duration:0.2},7.38);
tl.fromTo("#o2",{opacity:0,scale:2},{opacity:1,scale:1,duration:0.25,ease:"power4.out"},17.7);
tl.fromTo("#n3",{textContent:0},{textContent:3,duration:0.5,snap:{textContent:1}},17.78);
tl.fromTo("#o4",{opacity:0},{opacity:1,duration:0.2},29.3);
tl.fromTo("#n50",{textContent:0},{textContent:50,duration:1.0,ease:"power2.out",snap:{textContent:1}},29.4);
tl.fromTo("#aa",{opacity:0,y:20},{opacity:1,y:0,duration:0.3,ease:"back.out(2)"},32.7);
tl.fromTo("#mito span",{scale:2.8,opacity:0,rotation:-18},{scale:1,opacity:1,rotation:-4,duration:0.25,ease:"power3.in"},53.05);
tl.fromTo("#bg",{x:0},{x:-24,duration:0.05,yoyo:true,repeat:5},53.3);
tl.fromTo("#flash",{opacity:0.6},{opacity:0,duration:0.25},53.3);
tl.fromTo("#fake span",{y:-1100,rotation:-25},{y:0,rotation:-4,duration:0.5,ease:"bounce.out"},60.0);
tl.fromTo("#bg",{x:0},{x:-30,duration:0.05,yoyo:true,repeat:5},60.4);
tl.fromTo("#flash",{opacity:0.7},{opacity:0,duration:0.25},60.4);
tl.fromTo("#sa",{opacity:0,x:-300},{opacity:1,x:0,duration:0.3,ease:"back.out(2)"},65.6);
tl.fromTo("#sb",{opacity:0,scale:2.2},{opacity:1,scale:1,duration:0.25,ease:"power4.out"},68.0);
tl.fromTo("#flash",{opacity:0.5},{opacity:0,duration:0.2},68.0);
tl.fromTo("#cta span",{scale:0.6,opacity:0},{scale:1,opacity:1,duration:0.4,ease:"back.out(2.2)"},75.35);
tl.to("#cta span",{scale:1.06,duration:0.45,yoyo:true,repeat:2,ease:"sine.inOut"},75.8);
tl.fromTo("#handle span",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},75.5);
tl.fromTo("#bg",{scale:1.0},{scale:1.06,duration:'''+str(T)+''',ease:"none"},0);
'''+'\n'.join(js)+'''
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
open('hf/index.html','w').write(H);print('ok')
