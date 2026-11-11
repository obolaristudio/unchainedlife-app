import sys,json,random;sys.path.insert(0,'../_lib')
from common import *
random.seed(23);T=59.0
S=[(0,5.2,'5844',2,.5),(5.2,8.1,'4773',1,.5),(8.1,16.9,'3955',1,.5),(16.9,23.2,'5511',1,.5),(23.2,29.9,'4326',1,.5),(29.9,33.3,'5491',1,.5),
   (33.3,37.2,'3786',1,.5),(37.2,45.6,'12913',1,.5),(45.6,48.5,'5637',1,.5),(48.5,55.1,'5550',1,.5),(55.1,T,'4478',1,.5)]
if 'bg' in sys.argv: build_bg(S,out='hf'); json.dump(S,open('scenes.json','w')); sys.exit()
W=json.load(open('vwords.json'))
rep={'Obolária':'Obolari','9604':'9604'}
out=[]
for w in W:
    if w['w']=='9604' and out and out[-1]['w']=='AOD': out[-1]['w']='AOD-9604'; continue
    out.append({'w':rep.get(w['w'],w['w']),'s':w['s']})
KEY={'hormônio','prometia','fragmento','aminoácidos','quebra','-cabeça.','interessante','metabolismo','gordura','536','12','placebo.','placebo','diferença','2024','fda','anvisa.','educativo','próximo?','aqui!','AOD-9604'}
KEY={k.strip('.,?!:').lower() for k in KEY}
caps,js=captions(out,T,KEY)
H=[hd('h0',0,5.2,'<div class="m">Um pedacinho de hormônio que <span>prometia muito</span></div><div class="s" id="h0s">o que os estudos mostraram?</div>'),
 hd('h1',5.2,8.1,'<div class="m">Hormônio do <span>crescimento</span></div><div class="s">o corpo já produz</div>'),
 hd('h2',8.1,16.9,'<div class="m"><span>AOD-9604</span></div><div class="s">só um fragmento do hormônio</div>'),
 hd('h3',16.9,23.2,'<div class="m">A ideia era <span>interessante</span></div><div class="s">só a parte do metabolismo</div>'),
 hd('h4',23.2,29.9,'<div class="m">Estudo com <span>536 pessoas</span></div>'),
 hd('h5',29.9,33.3,'<div class="m">O resultado <span>principal</span></div>'),
 hd('h6',33.3,37.2,'<div class="m"><span>Placebo</span> = tratamento<br>sem efeito</div><div class="s">usado para comparar</div>'),
 hd('h7',37.2,45.6,'<div class="m"><span>2024</span> · FDA</div><div class="s">comitê de especialistas</div>'),
 hd('h8',45.6,48.5,'<div class="m"><span>Brasil</span> · Anvisa</div>'),
 hd('h9',48.5,55.1,'<div class="m">Conteúdo <span>educativo</span></div>'),
 hd('h10',55.1,T,'<div class="m">Qual peptídeo<br><span>no próximo?</span></div>')]
B=''.join(H)+'''
<div id="o16" class="clip ov" data-start="12.4" data-duration="4.4" style="top:1100px"><div class="big"><span id="cnt">0</span> <span style="font-size:70px">aminoácidos</span></div><div id="ppz"><span class="pill">como uma <b>peça solta</b> de quebra-cabeça</span></div></div>
<div id="puz" class="clip" data-start="14.2" data-duration="2.6" style="position:absolute;inset:0;z-index:7"><span class="fall" id="pz" style="left:420px;font-size:260px">🧩</span></div>
<div id="oi" class="clip ov" data-start="19.3" data-duration="3.8"><div id="pi1"><span class="pill">pegar só <b>uma parte</b></span></div><div id="pi2"><span class="pill v">sem o resto do hormônio</span></div></div>
<div id="o536" class="clip ov" data-start="24.5" data-duration="5.3" style="top:1080px"><div class="big"><span id="c536">0</span> <span style="font-size:70px">pessoas</span></div><div id="p12"><span class="pill"><b>12 semanas</b> de estudo</span></div></div>
<div id="stamp" class="clip" data-start="29.95" data-duration="1.3"><span>ESPERA…</span></div>
<div id="ore" class="clip ov" data-start="30.3" data-duration="3.0"><div id="pre"><span class="pill o">sem diferença <b>importante</b> do placebo</span></div></div>
<div id="opl" class="clip ov" data-start="33.4" data-duration="3.7"><div id="ppl"><span class="pill">comparar com <b>quem não recebeu</b> o remédio</span></div></div>
<div id="ofd" class="clip ov" data-start="39.6" data-duration="5.9" style="top:1080px"><div class="big"><span id="v12">0</span> × 0</div><div id="pfd"><span class="pill o">contra incluir na lista de manipulação</span></div></div>
<div id="obr" class="clip ov" data-start="45.7" data-duration="2.8" style="top:1020px"><div class="flag">🇧🇷</div><div id="pbr"><span class="pill">não localizamos <b>registro</b></span></div></div>
<div id="ocl" class="clip ov" data-start="48.7" data-duration="6.3"><div id="pc1"><span class="pill">Obolari <b>Academy</b></span></div><div id="pc2"><span class="pill">Não é recomendação médica<br>nem sugestão de uso</span></div></div>
<div id="cta" class="clip" data-start="56.0" data-duration="3.0"><span>Comenta aqui 💬</span></div>
'''+'\n'.join(caps)
J='''tl.fromTo("#h0 .m",{scale:1.6,opacity:0},{scale:1,opacity:1,duration:0.3,ease:"power4.out"},0);
tl.fromTo("#flash",{opacity:0.5},{opacity:0,duration:0.25},0);
tl.fromTo("#h0s",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},3.4);
'''
for h,t in [('#h1',5.2),('#h2',8.1),('#h3',16.9),('#h4',23.2),('#h5',29.9),('#h6',33.3),('#h7',37.2),('#h8',45.6),('#h9',48.5),('#h10',55.1)]:
    J+=f'tl.fromTo("{h}",{{y:30,opacity:0}},{{y:0,opacity:1,duration:0.3,ease:"power3.out"}},{t});\n'
for s in S[1:]: J+=f'tl.fromTo("#flash",{{opacity:0.3}},{{opacity:0,duration:0.18}},{s[0]});\n'
J+='''tl.fromTo("#bg",{scale:1.14,filter:"blur(5px)"},{scale:1,filter:"blur(0px)",duration:0.3,ease:"power2.out"},5.2);
tl.fromTo("#cnt",{textContent:0},{textContent:16,duration:1.2,ease:"power2.out",snap:{textContent:1}},12.6);
tl.fromTo("#pz",{y:-300,rotation:-30},{y:900,rotation:12,duration:0.9,ease:"bounce.out"},14.2);
tl.fromTo("#flash",{opacity:0.5},{opacity:0,duration:0.25},14.2);
tl.fromTo("#ppz",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},15.0);
tl.fromTo("#pi1",{opacity:0,x:200},{opacity:1,x:0,duration:0.35,ease:"back.out(1.8)"},19.6);
tl.fromTo("#pi2",{opacity:0,x:200},{opacity:1,x:0,duration:0.35,ease:"back.out(1.8)"},22.0);
tl.fromTo("#c536",{textContent:0},{textContent:536,duration:1.1,ease:"power2.out",snap:{textContent:1}},24.7);
tl.fromTo("#p12",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},28.7);
tl.fromTo("#bg",{x:0},{x:-30,duration:0.05,yoyo:true,repeat:5},29.95);
tl.fromTo("#bg",{filter:"grayscale(0) brightness(1)"},{filter:"grayscale(1) brightness(0.6)",duration:0.15},29.95);
tl.to("#bg",{filter:"grayscale(0) brightness(1)",duration:0.2},31.2);
tl.fromTo("#flash",{opacity:0.8},{opacity:0,duration:0.3},29.95);
tl.fromTo("#stamp span",{scale:3,opacity:0},{scale:1,opacity:1,duration:0.25,ease:"power3.in"},30.0);
tl.fromTo("#pre",{opacity:0,scale:0.5},{opacity:1,scale:1,duration:0.3,ease:"back.out(2.5)"},31.4);
tl.fromTo("#ppl",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},34.2);
tl.fromTo("#v12",{textContent:0},{textContent:12,duration:0.6,ease:"power2.out",snap:{textContent:1}},40.4);
tl.fromTo("#pfd",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},42.3);
tl.fromTo("#obr .flag",{scale:0,rotation:30},{scale:1,rotation:0,duration:0.4,ease:"back.out(2.5)"},45.75);
tl.fromTo("#pbr",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},46.9);
tl.fromTo("#pc1",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},48.8);
tl.fromTo("#pc2",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},51.9);
tl.fromTo("#cta span",{scale:0.6,opacity:0},{scale:1,opacity:1,duration:0.4,ease:"back.out(2.2)"},56.1);
tl.to("#cta span",{scale:1.06,duration:0.45,yoyo:true,repeat:5,ease:"sine.inOut"},56.6);
'''+'\n'.join(js)
open('hf/index.html','w').write(page(T,B,J,'PEPTÍDEOS · AOD-9604')); print('ok',len(caps))
