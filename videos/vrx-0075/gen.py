import json,re,html
W=json.load(open('words.json')); T=39.6
# caption groups (<=3 words, break on punctuation)
fix={'-0075?':'0075?','-5.':'5.','reta':'retatrutida.','trutida.':'','a':None}
words=[]
for i,w in enumerate(W):
    t=w['w']
    if t=='VRX': t='VRX-0075?'
    elif t=='-0075?': continue
    elif t=='GLP': t='“GLP-5”.'
    elif t=='-5.': continue
    elif t=='reta': t='retatrutida.'
    elif t=='trutida.': continue
    elif t=='a' and i+1<len(W) and W[i+1]['w']=='guia,': continue
    elif t=='guia,': t='GUIA,'
    words.append({'w':t,'s':w['s']})
groups=[];cur=[]
for w in words:
    cur.append(w)
    if len(cur)==3 or re.search(r'[,.?!:]$',w['w']): groups.append(cur);cur=[]
if cur: groups.append(cur)
KEY={'VRX-0075?','“GLP-5”.','cinco','ratos','obesos','retatrutida.','humanos,','aprovado','FDA','Anvisa.','garantia','GUIA,','2026,'}
caps=[];js=[]
for gi,g in enumerate(groups):
    a=g[0]['s']; b=groups[gi+1][0]['s'] if gi+1<len(groups) else T-0.2
    spans=''.join(f'<span class="w{" k" if w["w"] in KEY else ""}" id="c{gi}_{j}">{html.escape(w["w"])}</span> ' for j,w in enumerate(g))
    caps.append(f'<div id="cg{gi}" class="clip cap" data-start="{a:.2f}" data-duration="{b-a:.2f}">{spans}</div>')
    for j,w in enumerate(g):
        js.append(f'tl.fromTo("#c{gi}_{j}",{{opacity:0.25,y:8}},{{opacity:1,y:0,duration:0.12}},{w["s"]:.2f});')
chips=['GLP-1','GIP','GLUCAGON','AMILINA','CALCITONINA']
chip_html=''.join(f'<span class="chip" id="ch{i}">{c}</span>' for i,c in enumerate(chips))
for i,t in enumerate([8.75,9.2,9.6,10.1,10.6]): js.append(f'tl.fromTo("#ch{i}",{{scale:0,opacity:0}},{{scale:1,opacity:1,duration:0.3,ease:"back.out(2.5)"}},{t});')
H=f'''<!doctype html><html lang="pt-BR"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script><style>
@font-face{{font-family:"Bric";src:url("assets/fonts/Bricolage-800.ttf");font-weight:800}}
@font-face{{font-family:"Bric";src:url("assets/fonts/Bricolage-700.ttf");font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}html,body{{width:1080px;height:1920px;overflow:hidden;background:#0E0E0E}}
#root{{position:relative;width:1080px;height:1920px;font-family:"Bric",sans-serif;color:#fff;overflow:hidden}}
#bg{{position:absolute;inset:0;width:1080px;height:1920px;object-fit:cover;z-index:1}}
#panel{{position:absolute;left:0;top:420px;width:1080px;height:1100px;z-index:2;box-shadow:inset 0 0 0 3px rgba(203,239,75,.0);background:linear-gradient(rgba(0,0,0,.0) 70%,rgba(0,0,0,.55) 100%)}}
#frame{{position:absolute;inset:26px;z-index:9;border:4px solid #CBEF4B;border-radius:34px;box-shadow:0 0 0 40px #0E0E0E}}
#tag{{position:absolute;z-index:9;top:80px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:16px;font-weight:700;font-size:26px;letter-spacing:8px}}
#tag .d{{width:18px;height:18px;border-radius:50%;background:#CBEF4B;box-shadow:0 0 14px #CBEF4B}}#tag .c{{color:#CBEF4B}}
.hd{{position:absolute;z-index:6;left:40px;right:40px;top:150px;height:260px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}}
.hd .s{{font-weight:700;font-size:44px;color:#F2EFE6}}
.hd .b{{font-weight:800;font-size:150px;line-height:.95;letter-spacing:-5px;color:#CBEF4B;text-shadow:0 0 40px rgba(203,239,75,.35)}}
.hd .m{{font-weight:800;font-size:84px;line-height:1;letter-spacing:-2px}}
.hd .m span{{color:#CBEF4B}} .hd .r{{color:#E53935}}
.cap{{position:absolute;z-index:6;left:60px;right:60px;top:1555px;text-align:center;font-weight:800;font-size:62px;line-height:1.1;letter-spacing:-1px;text-shadow:0 4px 18px rgba(0,0,0,.8)}}
.cap .k{{color:#CBEF4B}}
#chips{{position:absolute;z-index:5;left:50px;right:50px;top:1280px;display:flex;flex-wrap:wrap;justify-content:center;gap:16px}}
.chip{{background:#CBEF4B;color:#141414;font-weight:800;font-size:40px;padding:10px 22px;border-radius:14px;box-shadow:0 8px 24px rgba(0,0,0,.5)}}
.stamp{{position:absolute;z-index:5;left:0;right:0;top:1180px;text-align:center}}
.stamp span{{display:inline-block;border:8px solid #E53935;color:#E53935;background:rgba(14,14,14,.82);font-weight:800;font-size:96px;letter-spacing:2px;padding:8px 34px;border-radius:18px;transform:rotate(-6deg)}}
#cmp{{position:absolute;z-index:5;left:90px;right:90px;top:1150px;background:rgba(14,14,14,.85);border-radius:24px;padding:26px 32px}}
#cmp .row{{display:flex;align-items:center;gap:18px;margin:10px 0;font-weight:800;font-size:36px}}
#cmp .lab{{width:270px}} #cmp .bar{{height:42px;border-radius:10px;transform-origin:0 50%}}
#cmp .n{{font-weight:700;font-size:24px;color:rgba(255,255,255,.7);margin-top:10px;text-align:center}}
#badge{{position:absolute;z-index:5;left:0;right:0;top:1290px;text-align:center}}
#badge span{{display:inline-block;background:rgba(14,14,14,.85);border:3px solid #CBEF4B;font-weight:800;font-size:40px;padding:14px 28px;border-radius:16px}}
#badge b{{color:#CBEF4B}}
#cta{{position:absolute;z-index:6;left:0;right:0;top:1250px;text-align:center}}
#cta span{{display:inline-block;background:#CBEF4B;color:#141414;font-weight:800;font-size:72px;padding:18px 48px;border-radius:60px;box-shadow:0 0 50px rgba(203,239,75,.6)}}
#flash{{position:absolute;inset:0;z-index:8;background:#fff;opacity:0}}
#foot{{position:absolute;z-index:9;top:1800px;left:0;right:0;text-align:center;font-weight:700;font-size:20px;letter-spacing:2px;color:rgba(255,255,255,.75)}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{T}" data-width="1080" data-height="1920">
<video id="bg" class="clip" data-start="0" data-duration="{T}" src="assets/bg.mp4" muted></video>
<div id="panel" class="clip" data-start="0" data-duration="{T}"></div>
<div id="h1" class="clip hd" data-start="0" data-duration="3.9"><div class="s">Você já ouviu falar do</div><div class="b" id="vrx">VRX-0075?</div></div>
<div id="h2" class="clip hd" data-start="3.9" data-duration="3.1"><div class="s">o apelido da internet</div><div class="m"><span>“GLP-5”</span></div></div>
<div id="h3" class="clip hd" data-start="7.0" data-duration="5.5"><div class="m">1 molécula<br><span>5 alvos</span> hormonais</div></div>
<div id="chips" class="clip" data-start="8.6" data-duration="3.9">{chip_html}</div>
<div id="h4" class="clip hd" data-start="12.5" data-duration="5.1"><div class="m">Novo estudo<br><span>ADA 2026</span></div></div>
<div id="badge" class="clip" data-start="12.8" data-duration="4.8"><span>Revista <b>Diabetes</b> · resumo 2839-LB</span></div>
<div id="h5" class="clip hd" data-start="17.6" data-duration="3.7"><div class="m">Mais perda de peso<br>que a <span>retatrutida</span></div></div>
<div id="cmp" class="clip" data-start="17.9" data-duration="3.4"><div class="row"><div class="lab">VRX-0075</div><div class="bar" id="b1" style="width:520px;background:#CBEF4B"></div></div><div class="row"><div class="lab">Retatrutida</div><div class="bar" id="b2" style="width:400px;background:#9AA0A6"></div></div><div class="n">em ratos obesos · ilustrativo, sem escala</div></div>
<div id="h6" class="clip hd" data-start="21.3" data-duration="2.5"><div class="m r">Mas atenção</div></div>
<div id="st1" class="clip stamp" data-start="21.9" data-duration="1.9"><span>SÓ EM RATOS</span></div>
<div id="h7" class="clip hd" data-start="23.8" data-duration="5.2"><div class="m"><span class="r" style="color:#E53935">0</span> estudos<br>em humanos</div></div>
<div id="st2" class="clip stamp" data-start="26.5" data-duration="2.5"><span>NÃO APROVADO</span></div>
<div id="h8" class="clip hd" data-start="29.0" data-duration="4.6"><div class="m r">⚠️ Cuidado<br><span style="color:#fff">com quem vende</span></div></div>
<div id="h9" class="clip hd" data-start="33.6" data-duration="6.0"><div class="m">Peptídeos<br><span>explicados com ciência</span></div></div>
<div id="cta" class="clip" data-start="33.7" data-duration="5.9"><span>Comenta GUIA 📩</span></div>
{chr(10).join(caps)}
<div id="flash" class="clip" data-start="0" data-duration="{T}"></div>
<div id="frame" class="clip" data-start="0" data-duration="{T}"></div>
<div id="tag" class="clip" data-start="0" data-duration="{T}"><span class="d"></span>OBOLARI ACADEMY<span class="c">· PEPTÍDEOS</span></div>
<div id="foot" class="clip" data-start="0" data-duration="{T}">@OBOLARI_ACADEMY · CONTEÚDO EDUCATIVO · NÃO É RECOMENDAÇÃO MÉDICA</div>
</div><script>
const tl=gsap.timeline({{paused:true}});
tl.set("#flash",{{opacity:0}},0);
tl.fromTo("#vrx",{{scale:2.2,opacity:0}},{{scale:1,opacity:1,duration:0.35,ease:"power4.out"}},1.0);
tl.fromTo("#flash",{{opacity:0.6}},{{opacity:0,duration:0.25}},1.0);
tl.fromTo("#h1 .s",{{y:20,opacity:0}},{{y:0,opacity:1,duration:0.3}},0.05);
tl.to("#vrx",{{scale:1.05,duration:0.4,yoyo:true,repeat:3,ease:"sine.inOut"}},1.5);
'''
for h,t in [('#h2',3.9),('#h3',7.0),('#h4',12.5),('#h5',17.6),('#h6',21.3),('#h7',23.8),('#h8',29.0),('#h9',33.6)]:
    H+=f'tl.fromTo("{h}",{{y:30,opacity:0}},{{y:0,opacity:1,duration:0.3,ease:"power3.out"}},{t});\n'
for t in [3.9,7.0,9.4,12.5,15.0,17.6,19.6,21.3,23.8,26.3,29.0,31.3,33.6]:
    H+=f'tl.fromTo("#flash",{{opacity:0.35}},{{opacity:0,duration:0.18}},{t});\n'
H+='''tl.fromTo("#badge",{opacity:0,y:20},{opacity:1,y:0,duration:0.35},12.8);
tl.fromTo("#cmp",{opacity:0},{opacity:1,duration:0.25},17.9);
tl.fromTo("#b1",{scaleX:0},{scaleX:1,duration:0.8,ease:"power2.out"},18.1);
tl.fromTo("#b2",{scaleX:0},{scaleX:1,duration:0.8,ease:"power2.out"},18.3);
tl.fromTo("#st1 span",{scale:2.5,opacity:0},{scale:1,opacity:1,duration:0.25,ease:"power3.in"},21.9);
tl.fromTo("#st2 span",{scale:2.5,opacity:0},{scale:1,opacity:1,duration:0.25,ease:"power3.in"},26.5);
tl.fromTo("#cta span",{scale:0.6,opacity:0},{scale:1,opacity:1,duration:0.4,ease:"back.out(2.2)"},33.8);
tl.to("#cta span",{scale:1.06,duration:0.45,yoyo:true,repeat:7,ease:"sine.inOut"},34.4);
'''+'\n'.join(js)+'''
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
open('hf/index.html','w').write(H); print(len(groups),'grupos')
