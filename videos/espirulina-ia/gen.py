import json,re,html
from words import norm
# Reel espirulina, versão estilo editorial IA (fundo verde-escuro, clipe no topo, frase acendendo palavra a palavra).
T=77.7
W=[w for w in json.load(open('vwords.json')) if w['w']!='Obrigada!']
fix=[]
for w in W:
    if w['w'].startswith('-') and fix: fix[-1]={'w':fix[-1]['w']+w['w'],'s':fix[-1]['s']}; continue
    fix.append(dict(w))
for w in fix: w['w']=w['w'].replace('Obolary','Obolari').replace('aqui!','aqui.').replace('pseudo-vitamina','pseudovitamina')
words=norm(fix)
KEY={'azul','azul-esverdeado','Terra','espirulina','planta','cianobactéria','fotossíntese','3','bilhões','anos','ficocianina','proteína','metade','essenciais','NASA','espaço','oxigênio','pessoas','colesterol','pressão','câncer','laboratório','animais','surpresa','B12','pseudovitamina','falsa','usar','Comenta','aqui'}
sents=[];cur=[]
for w in words:
    cur.append(w)
    if re.search(r'[.?!]$',w['w']) and (len(cur)>=4 or w['w'].endswith('?')): sents.append(cur);cur=[]
if cur: sents.append(cur)
blocks=[];js=[]
for si,s in enumerate(sents):
    a=s[0]['s']; b=sents[si+1][0]['s'] if si+1<len(sents) else T
    sp=''.join(f'<span class="{"k" if re.sub(r"[,.?!:]+$","",w["w"]) in KEY else ""}" id="w{si}_{j}">{html.escape(w["w"])}</span> ' for j,w in enumerate(s))
    blocks.append(f'<div id="t{si}" class="clip tx" data-start="{a:.2f}" data-duration="{b-a:.2f}"><p>{sp}</p></div>')
    js.append(f'tl.fromTo("#t{si} p",{{opacity:0,y:24}},{{opacity:1,y:0,duration:0.25,ease:"power2.out"}},{a:.2f});')
    for j,w in enumerate(s): js.append(f'tl.fromTo("#w{si}_{j}",{{opacity:0.28}},{{opacity:1,duration:0.15}},{w["s"]:.2f});')
S=json.load(open('scenes.json'))
H=f'''<!doctype html><html lang="pt-BR"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script><style>
@font-face{{font-family:"Bric";src:url("assets/fonts/Bricolage-800.ttf");font-weight:800}}
@font-face{{font-family:"Bric";src:url("assets/fonts/Bricolage-700.ttf");font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}html,body{{width:1080px;height:1920px;overflow:hidden;background:#1D3324}}
#root{{position:relative;width:1080px;height:1920px;font-family:"Bric",sans-serif;color:#fff;overflow:hidden;background:#1D3324}}
#bg{{position:absolute;inset:0;width:1080px;height:1920px;object-fit:cover;z-index:1}}
#fade{{position:absolute;left:0;top:1000px;width:1080px;height:420px;z-index:2;background:linear-gradient(rgba(29,51,36,0),#1D3324 92%)}}
#bar{{position:absolute;left:0;top:0;width:1080px;height:150px;z-index:9;background:linear-gradient(rgba(18,32,22,.85),rgba(18,32,22,0));display:flex;align-items:center;justify-content:center;font-weight:800;font-size:46px;letter-spacing:-.5px;padding-top:20px}}
#bar i{{display:inline-block;width:18px;height:18px;border-radius:50%;background:#CBEF4B;margin-right:14px;box-shadow:0 0 12px #CBEF4B}}
.tx{{position:absolute;z-index:6;left:70px;right:70px;top:1290px;height:380px;display:flex;align-items:center;justify-content:center;text-align:center}}
.tx p{{font-weight:800;font-size:60px;line-height:1.22;letter-spacing:-1px}} .tx .k{{color:#CBEF4B}}
.big{{position:absolute;z-index:7;left:0;right:0;text-align:center;font-weight:800;color:#CBEF4B;text-shadow:0 10px 40px rgba(0,0,0,.75)}}
.stamp{{position:absolute;z-index:7;left:0;right:0;top:560px;text-align:center}}
.stamp span{{display:inline-block;background:#E53935;color:#fff;font-weight:800;font-size:110px;padding:10px 44px;border-radius:24px;transform:rotate(-4deg);box-shadow:0 20px 60px rgba(0,0,0,.6)}}
#flash{{position:absolute;inset:0;z-index:8;background:#fff;opacity:0}}
#cta{{position:absolute;z-index:7;left:0;right:0;top:1130px;text-align:center}}
#cta span{{display:inline-block;background:#CBEF4B;color:#141414;font-weight:800;font-size:64px;padding:16px 44px;border-radius:60px;box-shadow:0 0 50px rgba(203,239,75,.5)}}
#foot{{position:absolute;z-index:9;top:1820px;left:0;right:0;text-align:center;font-weight:700;font-size:20px;letter-spacing:2px;color:rgba(255,255,255,.55)}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{T}" data-width="1080" data-height="1920">
<video id="bg" class="clip" data-start="0" data-duration="{T}" src="assets/bg.mp4" muted></video>
<div id="fade" class="clip" data-start="0" data-duration="{T}"></div>
<div id="nm" class="clip big" data-start="7.3" data-duration="0.9" style="top:520px;font-size:150px">ESPIRULINA</div>
<div id="n3b" class="clip big" data-start="17.7" data-duration="1.8" style="top:500px;font-size:170px;line-height:1"><span id="n3">0</span> bilhões<div style="font-size:70px;color:#fff">de anos</div></div>
<div id="p50" class="clip big" data-start="29.3" data-duration="5.0" style="top:520px;font-size:200px;line-height:1">+<span id="n50">0</span>%<div style="font-size:60px;color:#fff">do peso seco é proteína</div></div>
<div id="fake" class="clip stamp" data-start="60.0" data-duration="4.8"><span>B12 "FALSA" ❌</span></div>
<div id="cta" class="clip" data-start="75.3" data-duration="{round(T-75.3,2)}"><span>Comenta aqui 💬</span></div>
{chr(10).join(blocks)}
<div id="flash" class="clip" data-start="0" data-duration="{T}"></div>
<div id="bar" class="clip" data-start="0" data-duration="{T}"><i></i>obolari_academy</div>
<div id="foot" class="clip" data-start="0" data-duration="{T}">CONTEÚDO EDUCATIVO · NÃO É RECOMENDAÇÃO MÉDICA NEM SUGESTÃO DE USO</div>
</div><script>
const tl=gsap.timeline({{paused:true}});
tl.set("#flash",{{opacity:0}},0);
'''
for a,b,c in S[1:]: H+=f'tl.fromTo("#flash",{{opacity:0.25}},{{opacity:0,duration:0.2}},{a});\n'
H+='''tl.fromTo("#nm",{scale:2.4,opacity:0},{scale:1,opacity:1,duration:0.25,ease:"power4.out"},7.38);
tl.fromTo("#n3b",{scale:2,opacity:0},{scale:1,opacity:1,duration:0.25,ease:"power4.out"},17.7);
tl.fromTo("#n3",{textContent:0},{textContent:3,duration:0.5,snap:{textContent:1}},17.78);
tl.fromTo("#p50",{scale:2,opacity:0},{scale:1,opacity:1,duration:0.25,ease:"power4.out"},29.3);
tl.fromTo("#n50",{textContent:0},{textContent:50,duration:1.0,ease:"power2.out",snap:{textContent:1}},29.4);
tl.fromTo("#fake span",{y:-1100,rotation:-25},{y:0,rotation:-4,duration:0.5,ease:"bounce.out"},60.0);
tl.fromTo("#bg",{x:0},{x:-24,duration:0.05,yoyo:true,repeat:5},60.4);
tl.fromTo("#flash",{opacity:0.7},{opacity:0,duration:0.25},60.4);
tl.fromTo("#cta span",{scale:0.6,opacity:0},{scale:1,opacity:1,duration:0.4,ease:"back.out(2.2)"},75.35);
tl.fromTo("#bg",{scale:1.0},{scale:1.05,duration:'''+str(T)+''',ease:"none",transformOrigin:"50% 30%"},0);
'''+'\n'.join(js)+'''
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
open('hf/index.html','w').write(H);print('ok',len(sents))
