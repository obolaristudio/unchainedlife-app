import sys; sys.path.insert(0,'..')
from common import *
T=92.7
fixes={'Diexa.':'Dihexa.','Diexa':'Dihexa','Anjotensina,':'angiotensina,','abirinto':'labirinto','Obolary':'Obolari','LL37,':'LL-37,','notícia.':'notícia:'}
merges={('GHK,','CU'):'GHK-Cu'}
KEY={'memória','FDA.','Dihexa.','Universidade','Washington,','mensageiro','angiotensina,','pressão','cérebro.','árvores.','galhos','conexões','sinapses.','laboratório,','HGF.','chave','obra.','2013,','idosos','labirinto','água.','pessoas,','notícia:','FDA','fevereiro','2027,','GHK-Cu','LL-37,','estudo,','Anvisa','registro.','próximo?'}
body='\n'.join([
hd('h0',0,6.4,'<div class="s">Um peptídeo para…</div><div class="m">consertar a<br><span>memória</span>? 🧠</div>'),
ov('o0',3.8,6.4,'<span class="pill o">📋 entrou na <b>pauta da FDA</b></span>'),
'<div id="o0b" class="clip ov" data-start="6.4" data-duration="2.1" style="top:1120px"><div class="big" style="font-size:180px">DI<span style="color:#CBEF4B">HEXA</span></div></div>',
hd('h1',8.5,12.4,'<div class="m">Nasceu numa<br><span>universidade</span> 🎓</div>'),
ov('o1',9.3,12.4,'<span class="pill">🇺🇸 Universidade Estadual de <b>Washington</b></span>'),
hd('h2',12.4,19.6,'<div class="m">De onde <span>veio</span>? 🧬</div>'),
ov('o2',13.8,19.6,'<div class="chips"><span class="pill" id="o2a">📨 um <b>mensageiro natural</b> do corpo</span><span class="pill v" id="o2b">🩺 família da <b>angiotensina</b> (pressão)</span></div>'),
hd('h3',19.6,26.6,'<div class="m">Remodelado no <span>laboratório</span></div>'),
ov('o3',19.8,26.6,'<div class="chips"><span class="pill" id="o3a">✂️ cortaram</span><span class="pill" id="o3b">🔧 ajustaram</span><span class="pill" id="o3c">🧠 pequeno e resistente para <b>chegar ao cérebro</b></span></div>'),
hd('h4',26.6,34.5,'<div class="m">Neurônios = <span>árvores</span> 🌳</div>'),
ov('o4',30.8,34.5,'<span class="pill">🌿 galhos = conexões (<b>sinapses</b>)</span>'),
hd('h5',34.5,40.8,'<div class="m">No <span>laboratório</span> 🧪</div>'),
ov('o5',36.6,40.8,'<div class="chips"><span class="pill" id="o5a">🌿 <b>mais galhos</b></span><span class="pill" id="o5b">🔗 <b>mais conexões</b></span></div>'),
hd('h6',40.8,49.2,'<div class="m">Liga o <span>modo obra</span> 🏗️</div>'),
ov('o6',44.4,49.2,'<div class="chips"><span class="pill v" id="o6a">🔑 chave do sistema <b>HGF</b></span><span class="pill" id="o6b">🛠️ construção do próprio corpo</span></div>'),
hd('h7',49.2,58.8,'<div class="m">E nos <span>animais</span>? 🐀</div>'),
'<div id="o7" class="clip ov" data-start="50.6" data-duration="8.2" style="top:1060px"><div class="big"><span id="n2013">0</span></div><div class="chips" style="margin-top:14px"><span class="pill" id="o7a">🐀 ratos idosos</span><span class="pill" id="o7b">🌊 acharam o caminho no <b>labirinto de água</b></span></div></div>',
hd('h8',58.8,62.1,'<div class="m">E em <span>pessoas</span>? 👥</div>'),
ov('o8',59.0,62.1,'<span class="pill o">📚 ainda <b>sem estudos publicados</b></span>'),
'<div id="st1" class="clip stamp" data-start="62.1" data-duration="1.7"><span>📰 NOTÍCIA</span></div>',
hd('h9',63.8,75.9,'<div class="m">Pauta da <span>FDA</span> 📋</div>'),
ov('o9',64.0,75.9,'<div class="chips"><span class="pill o" id="o9a">📅 comitê da FDA: <b>até fev/2027</b></span><span class="pill" id="o9b">🧠 Dihexa · <b>GHK-Cu</b> · <b>LL-37</b></span><span class="pill v" id="o9c">✅ GHK-Cu e LL-37: já expliquei aqui</span></div>',1060),
hd('h10',75.9,83.0,'<div class="m">Status <span>hoje</span> 🌎</div>'),
ov('o10',76.0,83.0,'<div class="chips"><span class="pill o" id="o10a">🇺🇸 EUA: <b>em estudo</b>, sem aprovação</span><span class="pill" id="o10b">🇧🇷 Anvisa: <b>sem registro</b></span></div>'),
hd('h11',83.0,T,'<div class="m">Qual peptídeo<br>eu explico no <span>próximo</span>? 💬</div>'),
f'<div id="cta" class="clip" data-start="89.4" data-duration="{round(T-89.4,2)}"><span>Comenta aqui 👇</span></div>',
f'<div id="handle" class="clip" data-start="83.0" data-duration="{round(T-83.0,2)}"><span>@obolari_academy</span></div>',
])
slides=[('#o0',3.8),('#o1',9.3),('#o2a',13.8),('#o2b',15.8),('#o3a',19.8),('#o3b',20.8),('#o3c',22.3),('#o4',30.8),('#o5a',38.6),('#o5b',39.5),('#o6a',44.4),('#o6b',41.5+4.0),('#o7a',51.8),('#o7b',55.2),('#o8',59.0),('#o9a',64.0),('#o9b',68.9),('#o9c',73.4),('#o10a',76.0),('#o10b',80.4)]
js=''
for h,t in [('#h1',8.5),('#h2',12.4),('#h3',19.6),('#h4',26.6),('#h5',34.5),('#h6',40.8),('#h7',49.2),('#h8',58.8),('#h9',63.8),('#h10',75.9),('#h11',83.0)]:
    js+=f'tl.fromTo("{h}",{{y:30,opacity:0}},{{y:0,opacity:1,duration:0.3,ease:"power3.out"}},{t});\n'
js+='''tl.fromTo("#h0 .m",{scale:1.6,opacity:0},{scale:1,opacity:1,duration:0.3,ease:"power4.out"},0.0);
tl.fromTo("#o0b .big",{scale:2.4,opacity:0},{scale:1,opacity:1,duration:0.35,ease:"power4.out"},6.45);
tl.fromTo("#flash",{opacity:0.7},{opacity:0,duration:0.3,immediateRender:false},6.45);
tl.fromTo("#o5",{opacity:0},{opacity:1,duration:0.01},36.6);
tl.fromTo("#n2013",{textContent:1990},{textContent:2013,duration:1.0,ease:"power2.out",snap:{textContent:1}},50.6);
tl.to("#bg",{filter:"grayscale(1) brightness(0.55)",duration:0.12},62.1); tl.to("#bg",{filter:"grayscale(0) brightness(1)",duration:0.2},63.7);
tl.fromTo("#bg",{x:0},{x:-30,duration:0.05,yoyo:true,repeat:5,immediateRender:false},62.1);
tl.fromTo("#flash",{opacity:0.85},{opacity:0,duration:0.3,immediateRender:false},62.1);
tl.fromTo("#st1 span",{scale:3,opacity:0,rotation:-15},{scale:1,opacity:1,rotation:-4,duration:0.28,ease:"power3.in"},62.12);
tl.fromTo("#cta span",{scale:0.6,opacity:0},{scale:1,opacity:1,duration:0.4,ease:"back.out(2.2)"},89.4);
tl.to("#cta span",{scale:1.06,duration:0.45,yoyo:true,repeat:2,ease:"sine.inOut"},89.9);
tl.fromTo("#handle span",{y:30,opacity:0},{y:0,opacity:1,duration:0.4},83.4);
'''
build('.',T,'PEPTÍDEOS · DIHEXA',fixes,merges,KEY,body,slides,js,noflash=(62.1,))
