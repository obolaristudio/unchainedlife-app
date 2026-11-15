import json,re,html,random
random.seed(7)
W=json.load(open('vwords.json')); T=89.8
rep={'guia,':'GUIA,','Obolária':'Obolari','Salve':'Salva'}
words=[];skip=set()
for i,w in enumerate(W):
    if i in skip: continue
    t=rep.get(w['w'],w['w'])
    if t=='GHK' and i+1<len(W) and W[i+1]['w'].startswith('-CU'): t='GHK-Cu,'; skip.add(i+1)
    if t=='58' and i+1<len(W) and W[i+1]['w']=='%': t='58%'; skip.add(i+1)
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
KEY={'cobre.','cobre,','esquecidos','defesa.','neutrófilos,','soldados','vírus','bactérias','encostar.','58%','infecções.','ferro.','anemia','surpreendente.','Zinco','zinco','roubar','porta','intestino.','espelho.','GHK-Cu,','colágeno.','cérebro,','equilíbrio,','excesso.','fígado,','ostras,','castanhas,','cacau','feijão.','GUIA,'}
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
{hd('h0',0,2.1,'<div class="s">Verdades escondidas sobre o</div><div class="m" style="font-size:130px"><span>COBRE</span> 🟠</div>')}
{hd('h1',2.1,9.2,'<div class="m">O mineral<br><span>esquecido</span></div>')}
<div id="o1" class="clip ov" data-start="6.3" data-duration="2.9"><span class="pill">sem ele, muita coisa <b>para de funcionar</b></span></div>
{hd('h2',9.2,21.1,'<div class="m">Verdade nº <span>1</span> 🛡️</div><div class="s">ele trabalha na sua defesa</div>')}
<div id="o2" class="clip ov" data-start="13.2" data-duration="7.9"><span class="pill">🦠 <b>neutrófilos</b> = os primeiros soldados de defesa</span><div style="margin-top:14px" id="o2b"><span class="pill">sem cobre: <b>menos soldados, menos força</b></span></div></div>
{hd('h3',21.1,35.5,'<div class="m">Verdade nº <span>2</span> 🦠</div><div class="s">mata micróbios só de encostar</div>')}
<div id="o3" class="clip ov" data-start="26.2" data-duration="3.0"><span class="pill">hospitais testam <b>maçanetas de cobre</b> 🚪</span></div>
<div id="o4" class="clip ov" data-start="29.4" data-duration="6.1"><div class="big"><span id="n58">0</span>%</div><span class="pill"><b>menos infecções</b> em UTIs com cobre (EUA, 2013)</span></div>
{hd('h4',35.5,46.1,'<div class="m">Verdade nº <span>3</span> 🩸</div><div class="s">o parceiro escondido do ferro</div>')}
<div id="o5" class="clip ov" data-start="39.8" data-duration="6.3"><span class="pill">sem cobre, o corpo <b>não usa o ferro direito</b></span><div style="margin-top:14px" id="o5b"><span class="pill">anemia que <b>não melhora só com ferro</b></span></div></div>
<div id="stamp" class="clip" data-start="46.1" data-duration="2.0"><span>ESPERA…</span></div>
{hd('h5',48.1,57.8,'<div class="m">Zinco demais<br><span>rouba</span> o cobre 😮</div>')}
<div id="o6" class="clip ov" data-start="49.0" data-duration="8.8"><div class="chips" style="flex-direction:row;flex-wrap:wrap;justify-content:center;gap:12px;align-items:center"><span class="chip" id="z1" style="border-color:#4FC3F7">🔵 zinco</span><span class="arr" id="za">⚔️</span><span class="chip" id="z2" style="border-color:#FF8A65">🟠 cobre</span></div><div style="margin-top:14px" id="z3"><span class="pill">disputam a <b>mesma porta</b> no intestino 🚪</span></div><div style="margin-top:14px" id="z4"><span class="pill">excesso de zinco por muito tempo → <b>falta de cobre</b></span></div></div>
{hd('h6',57.8,72.4,'<div class="m">Verdade nº <span>4</span> 🪞</div><div class="s">no espelho e no cérebro</div>')}
<div id="o7" class="clip ov" data-start="61.7" data-duration="5.7"><span class="pill">✨ <b>GHK-Cu</b>: peptídeo de cobre estudado para o <b>colágeno</b></span></div>
<div id="o8" class="clip ov" data-start="67.6" data-duration="4.8"><span class="pill">🧠 cientistas estudam o <b>equilíbrio do cobre</b> no envelhecimento</span></div>
{hd('h7',72.4,81.0,'<div class="m">A palavra é<br><span>equilíbrio</span> ⚖️</div><div class="s">não excesso</div>')}
<div id="o9" class="clip ov" data-start="77.5" data-duration="3.5"><div class="chips" style="flex-direction:row;flex-wrap:wrap;justify-content:center;gap:12px"><span class="chip" id="f1">🥩 fígado</span><span class="chip" id="f2">🦪 ostras</span><span class="chip" id="f3">🌰 castanhas</span><span class="chip" id="f4">🍫 cacau</span><span class="chip" id="f5">🫘 feijão</span></div></div>
{hd('h8',81.0,T,'<div class="m">Salva e <span>manda</span> 📤</div><div class="s">pra quem só lembra do zinco e da vitamina C</div>')}
<div id="cta" class="clip" data-start="84.4" data-duration="{round(T-84.4,2)}"><span>Comenta GUIA 📩</span></div>
{chr(10).join(caps)}
<div id="flash" class="clip" data-start="0" data-duration="{T}"></div>
<div id="frame" class="clip" data-start="0" data-duration="{T}"></div>
<div id="tag" class="clip" data-start="0" data-duration="{T}"><span class="d"></span>OBOLARI ACADEMY<span class="c">· MINERAIS</span></div>
<div id="foot" class="clip" data-start="0" data-duration="{T}">@OBOLARI_ACADEMY · CONTEÚDO EDUCATIVO · NÃO É RECOMENDAÇÃO MÉDICA</div>
</div><script>
const tl=gsap.timeline({{paused:true}});
tl.set("#flash",{{opacity:0}},0);
tl.fromTo("#h0 .m",{{scale:1.6,opacity:0}},{{scale:1,opacity:1,duration:0.3,ease:"power4.out"}},0.0);
tl.fromTo("#flash",{{opacity:0.5}},{{opacity:0,duration:0.25}},0.0);
'''
for h,t in [('#h1',2.1),('#h2',9.2),('#h3',21.1),('#h4',35.5),('#h5',48.1),('#h6',57.8),('#h7',72.4),('#h8',81.0)]:
    H+=f'tl.fromTo("{h}",{{y:30,opacity:0}},{{y:0,opacity:1,duration:0.3,ease:"power3.out"}},{t});\n'
S=json.load(open('scenes.json'))
for s_ in S[1:]:
    if s_[0] not in (46.1,48.1): H+=f'tl.fromTo("#flash",{{opacity:0.3}},{{opacity:0,duration:0.18}},{s_[0]});\n'
for o,t in [('#o1',6.3),('#o3',26.2),('#o7',61.7),('#o8',67.6)]:
    H+=f'tl.fromTo("{o}",{{opacity:0,x:200}},{{opacity:1,x:0,duration:0.35,ease:"back.out(1.8)"}},{t});\n'
H+='''tl.fromTo("#o2",{opacity:0,x:200},{opacity:1,x:0,duration:0.35,ease:"back.out(1.8)"},13.2);
tl.fromTo("#o2b",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},18.8);
tl.fromTo("#o4",{opacity:0},{opacity:1,duration:0.2},29.4);
tl.fromTo("#n58",{textContent:0},{textContent:58,duration:2.6,ease:"power2.out",snap:{textContent:1}},30.0);
tl.fromTo("#o5",{opacity:0,x:200},{opacity:1,x:0,duration:0.35,ease:"back.out(1.8)"},39.8);
tl.fromTo("#o5b",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},43.5);
tl.fromTo("#bg",{x:0},{x:-30,duration:0.05,yoyo:true,repeat:5},46.1);
tl.fromTo("#bg",{filter:"grayscale(0) brightness(1)"},{filter:"grayscale(1) brightness(0.6)",duration:0.15},46.1);
tl.to("#bg",{filter:"grayscale(0) brightness(1)",duration:0.2},48.0);
tl.fromTo("#flash",{opacity:0.8},{opacity:0,duration:0.3},46.1);
tl.fromTo("#stamp span",{scale:3,opacity:0},{scale:1,opacity:1,duration:0.25,ease:"power3.in"},46.15);
tl.fromTo("#o6",{opacity:0},{opacity:1,duration:0.2},49.0);
tl.fromTo("#z1",{x:-500,opacity:0},{x:0,opacity:1,duration:0.4,ease:"power3.out"},49.0);
tl.fromTo("#z2",{x:500,opacity:0},{x:0,opacity:1,duration:0.4,ease:"power3.out"},49.8);
tl.fromTo("#za",{scale:0},{scale:1.3,duration:0.3,ease:"back.out(3)"},50.4);
tl.fromTo("#z3",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},51.3);
tl.fromTo("#z4",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},54.2);
tl.fromTo("#f1",{opacity:0,y:-300},{opacity:1,y:0,duration:0.4,ease:"bounce.out"},77.5);
tl.fromTo("#f2",{opacity:0,y:-300},{opacity:1,y:0,duration:0.4,ease:"bounce.out"},78.3);
tl.fromTo("#f3",{opacity:0,y:-300},{opacity:1,y:0,duration:0.4,ease:"bounce.out"},78.9);
tl.fromTo("#f4",{opacity:0,y:-300},{opacity:1,y:0,duration:0.4,ease:"bounce.out"},79.7);
tl.fromTo("#f5",{opacity:0,y:-300},{opacity:1,y:0,duration:0.4,ease:"bounce.out"},80.3);
tl.fromTo("#cta span",{scale:0.6,opacity:0},{scale:1,opacity:1,duration:0.4,ease:"back.out(2.2)"},84.5);
tl.to("#cta span",{scale:1.06,duration:0.45,yoyo:true,repeat:5,ease:"sine.inOut"},85.0);
'''+'\n'.join(js)+'''
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
open('hf/index.html','w').write(H);print('ok',len(groups))
