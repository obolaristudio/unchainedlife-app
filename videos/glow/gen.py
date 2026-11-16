import json
from words import norm,captions
# Reel GHK-Cu x GLOW x KLOW (roteiro do Maxwell ajustado à Regra nº 1). Template: videos/ll37/gen.py
T=70.3
words=norm(json.load(open('vwords.json')))
KEY={'GHK-Cu','GLOW','KLOW','KPV','BPC-157','TB-500','BPC','TB','cobre','sangue','pele','colágeno','creme','três','tecidos','intestino','camundongos','só','nunca','juntas','pesquisa','não','visto','Comenta'}
caps,js=captions(words,T,KEY)
def hd(id,a,b,inner): return f'<div id="{id}" class="clip hd" data-start="{a}" data-duration="{round(b-a,2)}">{inner}</div>'
beads=''.join(f'<i id="bd{i}">{c}</i>' for i,c in enumerate(['G','H','K']))+'<i id="bd3" class="cu">Cu</i>'
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
<div id="h0" class="clip hd" data-start="0" data-duration="7.5"><div class="eq"><span class="chip" id="t1">GHK-Cu</span><span class="chip" id="t2">GLOW</span><span class="chip b" id="t3"><b>KLOW</b></span></div><div class="s" id="t4" style="margin-top:16px">3 nomes que confundem todo mundo 🤯</div></div>
<div id="o0" class="clip ov" data-start="5.5" data-duration="2.0"><span class="pill">a diferença em <b>1 minuto</b> ⏱️</span></div>
{hd('h1',7.5,24.7,'<div class="m">1 · <span>GHK-Cu</span></div><div class="s">um peptídeo só</div>')}
<div id="o1" class="clip ov" data-start="10.3" data-duration="2.8" style="top:1100px"><div class="beads">{beads}</div><div style="margin-top:16px"><span class="pill">3 aminoácidos + <b style="color:#FF8A3D">cobre</b></span></div></div>
<div id="o2" class="clip ov" data-start="13.15" data-duration="4.5"><span class="pill">existe no nosso <b>próprio sangue</b> 🩸</span></div>
<div id="o3" class="clip ov" data-start="17.7" data-duration="3.4"><span class="pill">em laboratório: <b>+ colágeno</b></span></div>
<div id="o4" class="clip ov" data-start="21.15" data-duration="3.55"><span class="pill" style="border-color:#3D7BFF">estudos em pessoas: <b style="color:#3D7BFF">creme na pele</b> 🧴</span></div>
{hd('h2',24.7,35.9,'<div class="m">2 · <span>GLOW</span></div><div class="s">uma mistura de 3</div>')}
<div id="o5" class="clip ov" data-start="27.4" data-duration="8.5" style="top:1060px"><div class="eq"><span class="chip" id="g1">GHK-Cu</span><span class="op" id="g2">+</span><span class="chip" id="g3">BPC-157</span><span class="op" id="g4">+</span><span class="chip" id="g5">TB-500</span></div><div style="margin-top:20px"><span class="pill" id="g6">pele + <b>reparo de tecidos</b></span></div></div>
{hd('h3',35.9,45.2,'<div class="m">3 · <span>KLOW</span></div><div class="s">o GLOW + 1</div>')}
<div id="o6" class="clip ov" data-start="37.3" data-duration="7.9" style="top:1060px"><div class="eq"><span class="chip" id="w1">GLOW</span><span class="op" id="w2">+</span><span class="chip b" id="w3"><b>KPV</b></span></div><div style="margin-top:20px"><span class="pill" id="w4" style="border-color:#3D7BFF">KPV: <b style="color:#3D7BFF">inflamação do intestino</b>, em camundongos 🐭</span></div><div style="margin-top:14px"><span class="pill" id="w5">o resto é <b>igual ao GLOW</b></span></div></div>
{hd('h4',45.2,54.2,'<div class="m"><span>Resumindo</span> ✅</div>')}
<div id="o7" class="clip ov" data-start="46.0" data-duration="8.2" style="top:1000px"><div class="rows"><div class="row" id="r1"><b>GHK-Cu</b> = 1 peptídeo</div><div class="row" id="r2"><b>GLOW</b> = GHK-Cu + BPC + TB</div><div class="row" id="r3" style="border-color:#3D7BFF"><b style="color:#3D7BFF">KLOW</b> = GLOW + KPV</div></div></div>
{hd('h5',54.2,62.0,'<div class="m">O ponto <span>principal</span> ☝️</div>')}
<div id="nv" class="clip stampR" data-start="56.5" data-duration="5.5"><span>misturas: NUNCA<br>estudadas juntas</span></div>
{hd('h6',62.0,T,'<div class="m">Qual desses você já tinha <span>visto</span>?</div><div class="s">conteúdo educativo</div>')}
<div id="cta" class="clip" data-start="67.1" data-duration="{round(T-67.1,2)}"><span>Comenta aqui 💬</span></div>
<div id="handle" class="clip" data-start="67.3" data-duration="{round(T-67.3,2)}"><span>@obolari_academy</span></div>
{chr(10).join(caps)}
<div id="flash" class="clip" data-start="0" data-duration="{T}"></div>
<div id="tag" class="clip" data-start="0" data-duration="{T}"><span class="d"></span>OBOLARI ACADEMY<span class="c">· PEPTÍDEOS</span></div>
<div id="foot" class="clip" data-start="0" data-duration="{T}">@OBOLARI_ACADEMY · CONTEÚDO EDUCATIVO · NÃO É RECOMENDAÇÃO MÉDICA</div>
</div><script>
const tl=gsap.timeline({{paused:true}});
tl.set("#flash",{{opacity:0}},0);
tl.fromTo("#flash",{{opacity:0.5}},{{opacity:0,duration:0.25}},0.0);
'''
for h,t in [('#h1',7.5),('#h2',24.7),('#h3',35.9),('#h4',45.2),('#h5',54.2),('#h6',62.0)]:
    H+=f'tl.fromTo("{h}",{{y:30,opacity:0}},{{y:0,opacity:1,duration:0.3,ease:"power3.out"}},{t});\n'
for s_ in json.load(open('scenes.json'))[1:]: H+=f'tl.fromTo("#flash",{{opacity:0.3}},{{opacity:0,duration:0.18}},{s_[0]});\n'
for o,t in [('#o0',5.5),('#o2',13.15),('#o3',17.7),('#o4',21.15)]:
    H+=f'tl.fromTo("{o}",{{opacity:0,x:200}},{{opacity:1,x:0,duration:0.35,ease:"back.out(1.8)"}},{t});\n'
pops=[('#t1',0.0),('#t2',1.68),('#t3',2.48),('#g1',27.46),('#g2',29.0),('#g3',29.02),('#g4',31.5),('#g5',31.54),('#w1',37.38),('#w2',37.64),('#w3',38.68)]
for k,t in pops: H+=f'tl.fromTo("{k}",{{opacity:0,scale:0.4}},{{opacity:1,scale:1,duration:0.26,ease:"back.out(2.5)"}},{t});\n'
for i in range(3): H+=f'tl.fromTo("#bd{i}",{{scale:0}},{{scale:1,duration:0.16,ease:"back.out(3)"}},{10.4+i*0.15:.2f});\n'
for k,t in [('#g6',33.0),('#w4',39.5),('#w5',43.5),('#r1',46.04),('#r2',48.08),('#r3',52.02)]:
    H+=f'tl.fromTo("{k}",{{opacity:0,x:200}},{{opacity:1,x:0,duration:0.32,ease:"back.out(1.8)"}},{t});\n'
H+='''tl.fromTo("#t4",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},3.18);
tl.fromTo("#o1",{opacity:0},{opacity:1,duration:0.2},10.3);
tl.fromTo("#bd3",{scale:0,y:-500},{scale:1,y:0,duration:0.5,ease:"bounce.out"},12.16);
tl.fromTo("#flash",{opacity:0.45},{opacity:0,duration:0.2},12.5);
tl.fromTo("#o5",{opacity:0},{opacity:1,duration:0.2},27.4);
tl.fromTo("#o6",{opacity:0},{opacity:1,duration:0.2},37.3);
tl.fromTo("#o7",{opacity:0},{opacity:1,duration:0.2},46.0);
tl.fromTo("#nv span",{y:-1100,rotation:-25},{y:0,rotation:-4,duration:0.5,ease:"bounce.out"},56.54);
tl.fromTo("#bg",{x:0},{x:-30,duration:0.05,yoyo:true,repeat:5},56.9);
tl.fromTo("#flash",{opacity:0.7},{opacity:0,duration:0.25},56.9);
tl.fromTo("#cta span",{scale:0.6,opacity:0},{scale:1,opacity:1,duration:0.4,ease:"back.out(2.2)"},67.15);
tl.to("#cta span",{scale:1.06,duration:0.45,yoyo:true,repeat:3,ease:"sine.inOut"},67.6);
tl.fromTo("#handle span",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},67.3);
tl.fromTo("#bg",{scale:1.0},{scale:1.06,duration:'''+str(T)+''',ease:"none"},0);
'''+'\n'.join(js)+'''
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
open('hf/index.html','w').write(H);print('ok')
