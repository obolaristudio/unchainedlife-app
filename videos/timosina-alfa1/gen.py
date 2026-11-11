import sys,json,random;sys.path.insert(0,'../_lib')
from common import *
random.seed(11);T=57.6
S=[(0,5.4,'4779',2,.5),(5.4,8.9,'5485',1,.5),(8.9,13.8,'3784',1,.5),(13.8,20.8,'4733',1,.5),(20.8,26.1,'4766',1,.5),(26.1,30.7,'4834',1,.5),
   (30.7,37.9,'3957',1,.5),(37.9,43.5,'5579',1,.5),(43.5,47.0,'3775',1,.5),(47.0,53.3,'17469',1,.5),(53.3,T,'5636',1,.5)]
if 'bg' in sys.argv: build_bg(S,out='hf'); json.dump(S,open('scenes.json','w')); sys.exit()
W=json.load(open('vwords.json'))
rep={'dôndula':'glândula','Obolária':'Obolari','-1.':'1.','Remédios,':'remédios,','Agência':'agência'}
W=[{'w':rep.get(w['w'],w['w']),'s':w['s']} for w in W]
# junta "alfa" + "1."
out=[]
for w in W:
    if w['w']=='1.' and out and out[-1]['w']=='alfa': out[-1]['w']='alfa-1.'; continue
    out.append(w)
KEY={'remédio','estudo.','alfa-1.','colar','contas.','contas','timo,','defesa.','itália,','índia,','hepatite','estudos','aprovou.','registro','anvisa.','fda,','28','controlados.','educativo','próximo?','aqui!'}
KEY={k.strip('.,?!:').lower() for k in KEY}
caps,js=captions(out,T,KEY)
H=[hd('h0',0,5.4,'<div class="m">Um peptídeo que<br><span>já é remédio</span><br>em alguns países</div>'),
 hd('h1',5.4,8.9,'<div class="m"><span>Timosina alfa-1</span></div><div class="s">o nome dele</div>'),
 hd('h2',8.9,13.8,'<div class="m">Peptídeo =<br><span>colar de contas</span></div><div class="s">cada conta é um aminoácido</div>'),
 hd('h3',13.8,20.8,'<div class="m">O colar vem do <span>timo</span></div><div class="s">glândula no peito</div>'),
 hd('h4',20.8,26.1,'<div class="m"><span>Itália</span></div>'),
 hd('h5',26.1,30.7,'<div class="m"><span>Índia</span></div>'),
 hd('h6',30.7,37.9,'<div class="m">E os <span>estudos</span>?</div>'),
 hd('h7',37.9,43.5,'<div class="m"><span>EUA</span> · FDA</div>'),
 hd('h8',43.5,47.0,'<div class="m"><span>Brasil</span> · Anvisa</div>'),
 hd('h9',47.0,53.3,'<div class="m">Conteúdo <span>educativo</span></div>'),
 hd('h10',53.3,T,'<div class="m">Qual peptídeo<br><span>no próximo?</span></div>')]
beads=''.join(f'<span class="bead" id="b{i}"></span>' for i in range(14))
rain=''.join(f'<span class="fall" id="fl{i}" style="left:{random.randint(60,980)}px"><span class="bead" style="width:{random.randint(50,90)}px;height:{random.randint(50,90)}px"></span></span>' for i in range(28))
B=''.join(H)+f'''
<div id="ob" class="clip ov" data-start="9.0" data-duration="4.8" style="top:1100px"><div>{beads}</div><div style="margin-top:14px"><span class="pill">aminoácido = <b>uma conta</b></span></div></div>
<div id="o28" class="clip ov" data-start="14.6" data-duration="6.2" style="top:1100px"><div class="big"><span id="cnt">0</span> <span style="font-size:80px">contas</span></div><div id="p28a"><span class="pill">TIMO = glândula no <b>peito</b></span></div><div id="p28b"><span class="pill">treina as <b>células de defesa</b></span></div></div>
<div id="rain" class="clip" data-start="14.6" data-duration="3.2" style="position:absolute;inset:0;z-index:7">{rain}</div>
<div id="oit" class="clip ov" data-start="20.9" data-duration="5.2" style="top:1020px"><div class="flag">🇮🇹</div><div id="pit1"><span class="pill">ajuda a <b>vacina da gripe</b></span></div><div id="pit2"><span class="pill o">em quem tem a defesa <b>mais fraca</b></span></div></div>
<div id="oin" class="clip ov" data-start="26.2" data-duration="4.5" style="top:1020px"><div class="flag">🇮🇳</div><div id="pin1"><span class="pill v">hepatite B <b>crônica</b></span></div></div>
<div id="ost" class="clip ov" data-start="30.8" data-duration="7.1"><div id="k1"><span class="chip">✅ vacina da gripe</span></div><div id="k2"><span class="chip">✅ hepatite B</span></div><div id="k3"><span class="chip" style="border-color:#FF8A3D">❓ outros usos: faltam estudos grandes</span></div></div>
<div id="stamp" class="clip" data-start="33.7" data-duration="1.5"><span>ESPERA…</span></div>
<div id="ous" class="clip ov" data-start="38.0" data-duration="5.5" style="top:1020px"><div class="flag">🇺🇸</div><div id="pus1"><span class="pill">FDA = agência de <b>remédios</b> dos EUA</span></div><div id="pus2"><span class="pill o">ainda <b>não aprovou</b></span></div></div>
<div id="obr" class="clip ov" data-start="43.6" data-duration="3.4" style="top:1020px"><div class="flag">🇧🇷</div><div id="pbr1"><span class="pill">não localizamos <b>registro</b></span></div></div>
<div id="ocl" class="clip ov" data-start="47.2" data-duration="6.1"><div id="pc1"><span class="pill">Obolari <b>Academy</b></span></div><div id="pc2"><span class="pill">Não é recomendação médica<br>nem sugestão de uso</span></div></div>
<div id="cta" class="clip" data-start="54.0" data-duration="{round(T-54.0,2)}"><span>Comenta aqui 💬</span></div>
'''+'\n'.join(caps)
J='''tl.fromTo("#h0 .m",{scale:1.6,opacity:0},{scale:1,opacity:1,duration:0.3,ease:"power4.out"},0);
tl.fromTo("#flash",{opacity:0.5},{opacity:0,duration:0.25},0);
'''
for h,t in [('#h1',5.4),('#h2',8.9),('#h3',13.8),('#h4',20.8),('#h5',26.1),('#h6',30.7),('#h7',37.9),('#h8',43.5),('#h9',47.0),('#h10',53.3)]:
    J+=f'tl.fromTo("{h}",{{y:30,opacity:0}},{{y:0,opacity:1,duration:0.3,ease:"power3.out"}},{t});\n'
for s in S[1:]: J+=f'tl.fromTo("#flash",{{opacity:0.3}},{{opacity:0,duration:0.18}},{s[0]});\n'
J+='''tl.fromTo("#bg",{scale:1.14,filter:"blur(5px)"},{scale:1,filter:"blur(0px)",duration:0.3,ease:"power2.out"},5.4);
for(let i=0;i<14;i++)tl.fromTo("#b"+i,{scale:0,opacity:0},{scale:1,opacity:1,duration:0.18,ease:"back.out(3)"},9.6+i*0.22);
tl.fromTo("#ob .pill",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},12.3);
tl.fromTo("#cnt",{textContent:0},{textContent:28,duration:1.3,ease:"power2.out",snap:{textContent:1}},14.7);
tl.fromTo("#p28a",{opacity:0,x:200},{opacity:1,x:0,duration:0.35,ease:"back.out(1.8)"},16.7);
tl.fromTo("#p28b",{opacity:0,x:200},{opacity:1,x:0,duration:0.35,ease:"back.out(1.8)"},18.7);
'''
for i in range(28): J+=f'tl.fromTo("#fl{i}",{{y:-200,rotation:{random.randint(-40,40)}}},{{y:{random.randint(1500,2000)},rotation:{random.randint(-160,160)},duration:{random.uniform(1.1,2.0):.2f},ease:"power1.in"}},{14.6+random.uniform(0,1.2):.2f});\n'
J+='''tl.fromTo("#oit .flag",{scale:0,rotation:-30},{scale:1,rotation:0,duration:0.4,ease:"back.out(2.5)"},20.95);
tl.fromTo("#pit1",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},22.8);
tl.fromTo("#pit2",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},24.8);
tl.fromTo("#oin .flag",{scale:0,rotation:30},{scale:1,rotation:0,duration:0.4,ease:"back.out(2.5)"},26.25);
tl.fromTo("#pin1",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},27.9);
tl.fromTo("#k1",{opacity:0,scale:0.5},{opacity:1,scale:1,duration:0.3,ease:"back.out(2.5)"},31.2);
tl.fromTo("#k2",{opacity:0,scale:0.5},{opacity:1,scale:1,duration:0.3,ease:"back.out(2.5)"},32.2);
tl.fromTo("#bg",{x:0},{x:-30,duration:0.05,yoyo:true,repeat:5},33.7);
tl.fromTo("#bg",{filter:"grayscale(0) brightness(1)"},{filter:"grayscale(1) brightness(0.6)",duration:0.15},33.7);
tl.to("#bg",{filter:"grayscale(0) brightness(1)",duration:0.2},35.1);
tl.fromTo("#flash",{opacity:0.8},{opacity:0,duration:0.3},33.7);
tl.fromTo("#stamp span",{scale:3,opacity:0},{scale:1,opacity:1,duration:0.25,ease:"power3.in"},33.75);
tl.fromTo("#k3",{opacity:0,scale:0.5},{opacity:1,scale:1,duration:0.3,ease:"back.out(2.5)"},35.4);
tl.fromTo("#ous .flag",{scale:0,rotation:-30},{scale:1,rotation:0,duration:0.4,ease:"back.out(2.5)"},38.05);
tl.fromTo("#pus1",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},40.7);
tl.fromTo("#pus2",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},42.4);
tl.fromTo("#obr .flag",{scale:0,rotation:30},{scale:1,rotation:0,duration:0.4,ease:"back.out(2.5)"},43.65);
tl.fromTo("#pbr1",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},44.8);
tl.fromTo("#pc1",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},47.3);
tl.fromTo("#pc2",{opacity:0,y:20},{opacity:1,y:0,duration:0.3},50.0);
tl.fromTo("#cta span",{scale:0.6,opacity:0},{scale:1,opacity:1,duration:0.4,ease:"back.out(2.2)"},54.1);
tl.to("#cta span",{scale:1.06,duration:0.45,yoyo:true,repeat:5,ease:"sine.inOut"},54.6);
'''+'\n'.join(js)
open('hf/index.html','w').write(page(T,B,J,'PEPTÍDEOS · TIMOSINA')); print('ok',len(caps))
