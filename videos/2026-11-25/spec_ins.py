T=91.52; TAG="PEPTÍDEOS · INSULINA"
REP={'peptídio':'peptídeo','Ubolari':'Obolari','ANVISA':'Anvisa','100':'Cem'}
KEY=['1922','menino','14','insulina.','peptídeo.','51','colar','chave','porta','células','energia.','tipo','Toronto,','Banting,','Best','Collip','pâncreas','Thompson,','primeiro','dólar.','simbólico','Nobel.','1978,','bactérias','genética.','FDA','Anvisa','essenciais','milhões','peptídeo?']
cols=['#E53935','#F4C430','#CBEF4B','#4FC3F7','#B388FF']
beads=''.join(f'<i id="bd{i}" style="background:{cols[i%5]}"></i>' for i in range(51))
HEADERS=[('h0',0,8.5,'<div class="m">1922 · Toronto 🇨🇦</div><div class="s">um menino de <span>14 anos</span> no hospital</div>'),
('h1',8.5,18.8,'<div class="m">A insulina é um<br><span>peptídeo</span> 🧬</div>'),
('h2',18.8,31.5,'<div class="m">Como ela <span>age</span>? 🔑</div>'),
('h3',31.5,49.2,'<div class="m">A <span>descoberta</span> 🔬</div><div class="s">Toronto, 1921–1922</div>'),
('h4',49.2,56.9,'<div class="m">A parte mais<br><span>bonita</span> 💛</div>'),
('h5',56.9,68.9,'<div class="m">O que veio<br><span>depois</span> 🏅</div>'),
('h6',68.9,80.3,'<div class="m">Status pelo <span>mundo</span> 🌎</div>'),
('h7',80.3,T,'<div class="m"><span>100 anos</span> depois</div><div class="s">milhões de vidas 🫶</div>')]
OVERLAYS=[('o0',1.0,8.4,'top:1120px','<div class="big"><span id="yr">1900</span><small>uma molécula minúscula salvou a vida dele</small></div>'),
('o1',14.0,18.7,'top:1080px',f'<div class="beads">{beads}</div><div style="margin-top:16px"><span class="pill"><b id="n51">0</b> aminoácidos · 2 correntes</span></div>'),
('o2',19.7,27.6,'','<div class="chips"><span class="pill" id="o2a">🍽️ você come → <b>açúcar no sangue</b></span><span class="pill" id="o2b">🔑 insulina = <b>a chave</b></span><span class="pill" id="o2c">🚪 abre as <b>células</b> → energia ⚡</span></div>'),
('o2d',27.7,31.4,'','<span class="pill v">🔒 diabetes tipo 1: <b>o corpo para de fabricar a chave</b></span>'),
('o3',36.4,42.8,'','<div class="chips"><span class="pill" id="o3a">👨‍🔬 Frederick <b>Banting</b></span><span class="pill" id="o3b">🎓 Charles <b>Best</b></span><span class="pill" id="o3c">⚗️ James <b>Collip</b></span></div>'),
('o3d',42.9,49.1,'','<div class="chips"><span class="pill" id="o3e">🧒 Leonard Thompson · <b>14 anos</b></span><span class="pill" id="o3f">✅ melhorou em <b>poucos dias</b></span></div>'),
('o4',51.3,53.15,'top:1150px','<span class="pill" style="font-size:52px">A patente foi vendida por… 🤔</span>'),
('o4s',53.2,56.85,'top:900px','<div class="stamp"><span id="st1">US$ 1</span></div><div style="margin-top:40px"><span class="pill" id="o4p">um valor <b>simbólico</b> 💛</span></div>'),
('o5',56.9,60.85,'top:1150px','<span class="pill" id="o5a" style="font-size:54px">🏅 <b>Prêmio Nobel</b> · 1923</span>'),
('o5b',60.9,68.85,'','<div class="chips"><span class="pill" id="o5c">🦠 1978: <b>bactérias</b> fabricam insulina humana</span><span class="pill" id="o5d">🧪 um dos primeiros remédios da <b>engenharia genética</b></span></div>'),
('o6',69.5,80.2,'top:1110px','<div class="chips"><span class="pill" id="o6a">🇺🇸 FDA: <b>aprovada</b></span><span class="pill" id="o6b">🇧🇷 Anvisa: <b>aprovada</b></span><span class="pill" id="o6c">🌎 OMS: <b>remédio essencial</b></span><span class="pill v" id="o6d">🩺 sempre com <b>acompanhamento médico</b></span></div>'),
('o7',84.6,T,'top:1220px','<div class="cta"><span id="cta">Qual peptídeo eu explico? 💬</span></div>')]
SLIDES=[('#o2a',19.7),('#o2b',22.4),('#o2c',24.6),('#o3e',42.9),('#o3f',46.1),('#o5c',60.9),('#o5d',66.3),('#o6a',69.5),('#o6b',71.6),('#o6c',73.6),('#o6d',77.8)]
POPS=[('#o2d .pill',27.7),('#o3a',37.6),('#o3b',38.8),('#o3c',39.8),('#o4 .pill',51.3),('#o5a',56.9),('#o4p',54.1),('#cta',84.6)]
PUNCH=[8.5,10.6,22.4,53.2,56.9,80.3]
JS='''tl.fromTo("#flash",{opacity:0.6},{opacity:0,duration:0.25},0);
tl.fromTo("#yr",{textContent:1900},{textContent:1922,duration:1.6,ease:"power2.out",snap:{textContent:1}},1.0);
tl.fromTo("#n51",{textContent:0},{textContent:51,duration:1.6,ease:"power1.out",snap:{textContent:1}},14.3);
tl.fromTo("#o1 .beads i",{scale:0},{scale:1,duration:0.12,stagger:0.03,ease:"back.out(3)"},14.1);
tl.fromTo("#flash",{opacity:0.85},{opacity:0,duration:0.35},53.2);
tl.fromTo("#st1",{scale:3.2,opacity:0,rotation:-20},{scale:1,opacity:1,rotation:-4,duration:0.28,ease:"power3.in"},53.22);
tl.fromTo("#bg",{x:0},{x:-28,duration:0.05,yoyo:true,repeat:5},53.25);
tl.fromTo("#bg",{filter:"grayscale(0) brightness(1)"},{filter:"grayscale(1) brightness(0.55)",duration:0.15},53.2);
tl.to("#bg",{filter:"grayscale(0) brightness(1)",duration:0.25},56.6);
tl.to("#cta",{scale:1.06,duration:0.45,yoyo:true,repeat:5,ease:"sine.inOut"},85.2);'''
STAMPS=[53.2]; DINGS=[14.3,56.9,69.5]
