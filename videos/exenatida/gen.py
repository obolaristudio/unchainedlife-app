import sys; sys.path.insert(0,'..')
from common import *
T=88.3
fixes={'ozenpik':'Ozempic','Gila,':'gila,','Iorque,':'York,','escendina':'exendina','escenatida,':'exenatida,','escenatida':'exenatida','GLP1.':'GLP-1.','GLP1':'GLP-1','Agência':'agência','Remédios':'remédios','Obolária':'Obolari','Veredito,':'Veredito:'}
merges={('monstro','de'):'monstro-de','exendina':None,('sema','-glutida'):'semaglutida'}
merges={k:v for k,v in merges.items() if v}
merges[('exendina','4.')]='exendina-4.'
KEY={'Ozempic','lagarto?','veneno','gila,','meses','1992,','saliva','exendina-4.','aminoácidos,','colar.','39','GLP-1.','GLP-1','insulina.','minutos.','fechadura','horas!','exenatida,','2005,','FDA,','primeiro','2006,','Anvisa','semaglutida','humano,','possível.','meia','verdade.','próximo?'}
beads=''.join(f'<i id="bd{i}" style="background:{c}"></i>' for i,c in enumerate((['#CBEF4B','#3D7BFF','#F2EFE6','#7B5CFF']*10)[:39]))
body='\n'.join([
hd('h0',0,4.5,'<div class="s">Mito ou verdade? 🤔</div><div class="m">O Ozempic veio de<br>um <span>lagarto</span>? 🦎</div>'),
hd('h1',4.5,11.4,'<div class="m">O <span>monstro-de-gila</span></div><div class="s">deserto dos EUA 🌵</div>'),
ov('o1',8.4,11.4,'<span class="pill">🦎 pode passar <b>meses sem comer</b></span>'),
hd('h2',11.4,18.9,'<div class="m"><span>1992</span> · Nova York 🏥</div>'),
ov('o2',14.8,18.9,'<span class="pill">🔬 Dr. John Eng estuda a <b>saliva</b> do lagarto</span>'),
hd('h3',18.9,24.3,'<div class="s">e achou um peptídeo…</div>'),
ov('o3',22.0,24.3,'<div class="big" style="font-size:130px">EXENDINA-<span style="color:#CBEF4B">4</span></div>',1150),
'<div id="st1" class="clip stamp" data-start="20.6" data-duration="1.4"><span>ESPERA…</span></div>',
hd('h4',24.3,30.9,'<div class="m">Contas de um <span>colar</span> 📿</div><div class="s">peptídeo = corrente de aminoácidos</div>'),
ov('o4',26.6,30.9,f'<div class="beads">{beads}</div><div style="margin-top:14px"><span class="pill"><b id="n39">0</b> aminoácidos</span></div>',1060),
hd('h5',30.9,39.4,'<div class="m">O nosso <span>GLP-1</span> 🍽️</div><div class="s">fabricado no intestino</div>'),
ov('o5',35.6,39.4,'<div class="chips"><span class="pill" id="o5a">🍽️ você come</span><span class="pill" id="o5b">➡️ pâncreas solta <b>insulina</b></span></div>'),
hd('h6',39.4,47.3,'<div class="m">Humano <span style="color:#FF8A3D">×</span> <span>lagarto</span></div>'),
ov('o6',40.6,47.3,'<div class="chips"><span class="pill o" id="o6a">⏱️ GLP-1 humano: some em <b>minutos</b></span><span class="pill" id="o6b">🔑 lagarto: mesma fechadura</span><span class="pill" id="o6c">⏳ e dura <b>HORAS</b></span></div>'),
hd('h7',47.3,51.4,'<div class="m"><span>Exenatida</span> 🧪</div><div class="s">a versão feita em laboratório</div>'),
hd('h8',51.4,66.2,'<div class="m">Status pelo <span>mundo</span> 🌎</div>'),
ov('o8',52.6,66.2,'<div class="chips"><span class="pill" id="o8a">🇺🇸 FDA <b>2005</b> · diabetes tipo 2</span><span class="pill v" id="o8b">🥇 o <b>primeiro</b> remédio da família</span><span class="pill" id="o8c">🇪🇺 Europa <b>2006</b></span><span class="pill" id="o8d">🇧🇷 Anvisa <b>aprovou</b></span></div>',1080),
hd('h9',66.2,77.2,'<div class="m">E o <span>Ozempic</span>? 🤔</div>'),
ov('o9',67.6,77.2,'<div class="chips"><span class="pill o" id="o9a">❌ não é feito do lagarto</span><span class="pill v" id="o9b">🧬 semaglutida = <b>GLP-1 humano</b> redesenhado</span><span class="pill" id="o9c">🦎 o lagarto <b>mostrou o caminho</b></span></div>',1080),
hd('h10',77.2,79.6,'<div class="s">Veredito ⚖️</div>'),
'<div id="st2" class="clip stamp" data-start="78.1" data-duration="1.5"><span style="font-size:96px">MEIA VERDADE</span></div>',
hd('h11',79.6,T,'<div class="m">Qual peptídeo<br>eu explico no <span>próximo</span>? 💬</div>'),
f'<div id="cta" class="clip" data-start="85.2" data-duration="{round(T-85.2,2)}"><span>Comenta aqui 👇</span></div>',
f'<div id="handle" class="clip" data-start="79.6" data-duration="{round(T-79.6,2)}"><span>@obolari_academy</span></div>',
])
slides=[('#o1',8.4),('#o2',14.8),('#o5a',35.6),('#o5b',37.3),('#o6a',40.6),('#o6b',43.4),('#o6c',45.8),('#o8a',52.6),('#o8b',58.8),('#o8c',61.4),('#o8d',63.6),('#o9a',67.6),('#o9b',69.6),('#o9c',73.8)]
js=''
for h,t in [('#h1',4.5),('#h2',11.4),('#h3',18.9),('#h4',24.3),('#h5',30.9),('#h6',39.4),('#h7',47.3),('#h8',51.4),('#h9',66.2),('#h10',77.2),('#h11',79.6)]:
    js+=f'tl.fromTo("{h}",{{y:30,opacity:0}},{{y:0,opacity:1,duration:0.3,ease:"power3.out"}},{t});\n'
js+='tl.fromTo("#h0 .m",{scale:1.6,opacity:0},{scale:1,opacity:1,duration:0.3,ease:"power4.out"},0.0);\n'
js+='''tl.fromTo("#st1 span",{scale:3,opacity:0},{scale:1,opacity:1,duration:0.25,ease:"power3.in"},20.6);
tl.fromTo("#flash",{opacity:0.8},{opacity:0,duration:0.3,immediateRender:false},20.6);
tl.to("#bg",{filter:"grayscale(1) brightness(0.6)",duration:0.15},20.6); tl.to("#bg",{filter:"grayscale(0) brightness(1)",duration:0.2},21.9);
tl.fromTo("#o3 .big",{scale:2.4,opacity:0},{scale:1,opacity:1,duration:0.35,ease:"power4.out"},22.0);
tl.fromTo("#flash",{opacity:0.6},{opacity:0,duration:0.3,immediateRender:false},22.0);
'''
for i in range(39): js+=f'tl.fromTo("#bd{i}",{{scale:0}},{{scale:1,duration:0.15,ease:"back.out(3)"}},{26.7+i*0.07:.2f});\n'
js+='''tl.fromTo("#n39",{textContent:0},{textContent:39,duration:2.7,ease:"none",snap:{textContent:1}},26.7);
tl.fromTo("#o6c",{scale:1},{scale:1.12,duration:0.25,yoyo:true,repeat:1},46.1);
tl.fromTo("#bg",{x:0},{x:-30,duration:0.05,yoyo:true,repeat:5,immediateRender:false},78.1);
tl.fromTo("#flash",{opacity:0.8},{opacity:0,duration:0.3,immediateRender:false},78.1);
tl.fromTo("#st2 span",{scale:2.8,opacity:0,rotation:-15},{scale:1,opacity:1,rotation:-4,duration:0.3,ease:"power3.in"},78.1);
tl.fromTo("#cta span",{scale:0.6,opacity:0},{scale:1,opacity:1,duration:0.4,ease:"back.out(2.2)"},85.2);
tl.to("#cta span",{scale:1.06,duration:0.45,yoyo:true,repeat:3,ease:"sine.inOut"},85.7);
tl.fromTo("#handle span",{y:30,opacity:0},{y:0,opacity:1,duration:0.4},80.0);
'''
build('.',T,'PEPTÍDEOS · EXENATIDA',fixes,merges,KEY,body,slides,js)
