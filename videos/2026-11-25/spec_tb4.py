T=85.39; TAG="PEPTÍDEOS · TIMOSINA β4"
REP={'peptídio':'peptídeo','Timosina':'timosina','Beta':'beta-','beta- 4':'beta-4','Timo,':'timo,','TB500':'TB-500','desses esqueletos':'desse esqueleto'}
KEY=['1981,','bezerros','polêmica','timosina','43','colar.','timo,','todas','esqueleto','actina.','mestre','obras','machucado.','2004,','Nature,','coração','camundongos','colírio','mistos.','TB-500?','TB-500','sintética','cavalo.','anti-doping','proíbe','FDA.','outubro','2026,','manipulação','receita,','Anvisa','registro.','peptídeo']
cols=['#E53935','#F4C430','#CBEF4B','#4FC3F7','#B388FF']
beads=''.join(f'<i style="background:{cols[i%5]}"></i>' for i in range(43))
HEADERS=[('h0',0,9.4,'<div class="m">Uma glândula de<br><span>bezerro</span> 🐄</div><div class="s">EUA · 1981</div>'),
('h1',9.4,22.2,'<div class="m">Timosina <span>beta-4</span> 🧬</div>'),
('h2',22.2,39.6,'<div class="m">Como ela <span>age</span>? 🏗️</div>'),
('h3',39.6,51.9,'<div class="m">O que os <span>estudos</span><br>mostraram 🔬</div>'),
('h4',51.9,62.2,'<div class="m">E o tal do<br><span>TB-500</span>? 🐎</div>'),
('h5',62.2,78.5,'<div class="m">Status pelo <span>mundo</span> 🌎</div>'),
('h6',78.5,T,'<div class="m">Um peptídeo<br>por <span>vídeo</span></div>')]
OVERLAYS=[('o0',1.2,9.3,'top:1120px','<div class="big"><span id="yr">1950</span><small>um peptídeo no centro de uma polêmica</small></div>'),
('o1',11.9,15.85,'top:1090px',f'<div class="beads">{beads}</div><div style="margin-top:16px"><span class="pill"><b id="n43">0</b> aminoácidos</span></div>'),
('o1b',15.9,22.1,'','<div class="chips"><span class="pill" id="o1c">📍 achado no <b>timo</b>, glândula do peito</span><span class="pill" id="o1d">😮 está em <b>quase todas as células</b></span></div>'),
('o2',23.1,35.8,'','<div class="chips"><span class="pill" id="o2a">🦴 a célula tem um <b>esqueleto</b></span><span class="pill" id="o2b">🧱 as peças = <b>actina</b></span><span class="pill" id="o2c">👷 timosina β4 = <b>mestre de obras</b></span></div>'),
('o2d',35.9,39.5,'','<span class="pill" id="o2e">🩹 a célula se move → <b>fecha o machucado</b></span>'),
('o3',41.2,47.1,'','<div class="chips"><span class="pill" id="o3a">📰 Nature, 2004</span><span class="pill" id="o3b">🐭❤️ coração de <b>camundongos</b> se recuperou</span></div>'),
('o3c',47.2,51.8,'','<span class="pill v" id="o3d">👁️ em pessoas: colírio · <b>resultados mistos</b></span>'),
('o4w',51.9,53.05,'top:880px','<div class="stamp"><span id="esp">ESPERA…</span></div>'),
('o4',53.1,58.75,'','<div class="chips"><span class="pill" id="o4a">🧪 TB-500 = versão <b>sintética</b></span><span class="pill" id="o4b">🏇 famosa nas <b>corridas de cavalo</b></span></div>'),
('o4s',58.8,62.15,'top:880px','<div class="stamp r"><span id="st2">🚫 <b>PROIBIDO</b> no esporte</span></div><div style="margin-top:40px"><span class="pill" id="o4p">Agência Mundial <b>Antidoping</b></span></div>'),
('o5',63.1,78.45,'top:1100px','<div class="chips"><span class="pill" id="o5a">🇺🇸 FDA: <b>não aprovada</b> como remédio</span><span class="pill" id="o5b">🏛️ out/2026: <b>manipulação tolerada</b>, com receita</span><span class="pill" id="o5c">⏳ a regra final <b>ainda não saiu</b></span><span class="pill" id="o5d">🇧🇷 Anvisa: <b>sem registro</b></span></div>'),
('o6',82.3,T,'top:1220px','<div class="cta"><span id="cta">Qual peptídeo eu explico? 💬</span></div>')]
SLIDES=[('#o1c',15.9),('#o1d',18.8),('#o2a',23.1),('#o2b',27.6),('#o2c',30.7),('#o3b',42.6),('#o4a',53.1),('#o4b',55.3),('#o5a',63.1),('#o5b',66.9),('#o5c',72.6),('#o5d',76.2)]
POPS=[('#o2e',35.9),('#o3a',41.2),('#o3d',47.2),('#o4p',59.6),('#cta',82.3)]
PUNCH=[9.4,22.2,30.7,41.2,62.2]
JS='''tl.fromTo("#flash",{opacity:0.6},{opacity:0,duration:0.25},0);
tl.fromTo("#yr",{textContent:1950},{textContent:1981,duration:1.6,ease:"power2.out",snap:{textContent:1}},1.3);
tl.fromTo("#n43",{textContent:0},{textContent:43,duration:1.5,ease:"power1.out",snap:{textContent:1}},12.1);
tl.fromTo("#o1 .beads i",{scale:0},{scale:1,duration:0.12,stagger:0.035,ease:"back.out(3)"},12.0);
tl.fromTo("#flash",{opacity:0.8},{opacity:0,duration:0.3},51.9);
tl.fromTo("#esp",{scale:3,opacity:0},{scale:1,opacity:1,duration:0.25,ease:"power3.in"},51.92);
tl.fromTo("#bg",{filter:"grayscale(0) brightness(1)"},{filter:"grayscale(1) brightness(0.55)",duration:0.12},51.9);
tl.to("#bg",{filter:"grayscale(0) brightness(1)",duration:0.2},52.9);
tl.fromTo("#flash",{opacity:0.7},{opacity:0,duration:0.3},58.8);
tl.fromTo("#st2",{scale:3,opacity:0,rotation:-25},{scale:1,opacity:1,rotation:-6,duration:0.28,ease:"power3.in"},58.82);
tl.fromTo("#bg",{x:0},{x:-28,duration:0.05,yoyo:true,repeat:5},58.85);
tl.to("#cta",{scale:1.06,duration:0.45,yoyo:true,repeat:4,ease:"sine.inOut"},82.9);'''
STAMPS=[51.9,58.8]; DINGS=[12.1,41.2]
