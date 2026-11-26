D='/tmp/claude-0/-home-user-unchainedlife-app/7a97ed93-910e-5bcd-a596-7dedfde0b525/scratchpad/octr'
SERIE='OCTREOTIDA'
REP={'peptídio':'peptídeo','Albolária':'Obolari','Obolári':'Obolari'}
SCENES=[(0,3.4,'30255',1),(3.4,7.0,'25327',1),(7.0,11.5,'4786',1),(11.5,13.8,'5634',1),(13.8,18.1,'5661',1),(18.1,21.5,'15959',0),
(21.5,27.4,'26784',0),(27.4,30.5,'3679',0),(30.5,35.0,'28897',1),(35.0,37.6,'33268',1),(37.6,43.5,'14776',1),(43.5,47.5,'5579',1),
(47.5,51.5,'17625',1),(51.5,55.3,'5491',1),(55.3,59.9,'40938',1),(59.9,62.6,'40892',1),(62.6,67.5,'1776',1),(67.5,71.7,'5407',1),
(71.7,76.0,'29933',1),(76.0,83.3,'46749',1),(83.3,None,'6472',1)]
HEADS=[(0,6.9,'<div class="s">1973 · CALIFÓRNIA 🇺🇸</div><div class="m">Um <span>freio</span> para o<br>crescimento 🛑</div>'),
(6.9,21.5,'<div class="s">O ORIGINAL</div><div class="m">A <span>somatostatina</span></div>'),
(21.5,27.4,'<div class="s">PRÊMIO NOBEL · 1977</div><div class="m">Roger <span>Guillemin</span> 🏅</div>'),
(27.4,35.0,'<div class="s">O PROBLEMA</div><div class="m">Some em menos de<br><span>3 minutos</span> ⏱️</div>'),
(35.0,47.5,'<div class="s">A SOLUÇÃO</div><div class="m">Nasce a<br><span>octreotida</span> ✂️</div>'),
(47.5,62.6,'<div class="s">POR QUE IMPORTA</div><div class="m">A <span>acromegalia</span></div>'),
(62.6,76.0,'<div class="s">STATUS PELO MUNDO</div><div class="m">Remédio <span>aprovado</span> 💊</div>'),
(76.0,83.3,'<div class="s">CURIOSIDADE</div><div class="m">A receita de<br><span>encolher</span> 🧬</div>'),
(83.3,None,'<div class="s">OBOLARI ACADEMY</div><div class="m">Conteúdo<br><span>educativo</span></div>')]
b14=''.join(f'<i id="ba{i}" style="background:{c}"></i>' for i,c in enumerate((['#CBEF4B','#7B5CFF']*7)))
b8=''.join(f'<i id="bb{i}" style="background:{c}"></i>' for i,c in enumerate(['#CBEF4B','#FF8A3D','#CBEF4B','#CBEF4B','#FF8A3D','#CBEF4B','#CBEF4B','#CBEF4B']))
OVS=[(3.6,6.9,1200,'<span class="pill">🐑 achado no <b>cérebro de ovelhas</b></span>'),
(7.6,11.5,1100,f'<div class="beads" style="max-width:600px">{b14}</div>'),
(14.0,18.1,1120,'<span class="pill">🧠 cérebro + <b>pâncreas</b></span><br><span class="pill">🛑 funciona como <b>placa de pare</b></span>'),
(18.2,21.5,1200,'<span class="pill">⬇️ segura o <b>hormônio do crescimento</b></span>'),
(28.4,32.7,1080,'<div class="big"><span id="cnt" data-to="3">0</span> min</div>'),
(32.8,35.0,1200,'<span class="pill r">rápido demais para <b>virar remédio</b></span>'),
(37.6,43.5,1050,f'<div class="beads" style="max-width:600px">{b8}</div><span class="pill">14 → <b>8 aminoácidos</b></span><br><span class="pill">🔄 peças <b>viradas ao contrário</b></span>'),
(43.6,47.5,1200,'<span class="pill">⏳ dura <b>horas</b>, não minutos</span>'),
(51.6,55.3,1150,'<span class="pill">🧠 hipófise: <b>excesso</b> de hormônio do crescimento</span>'),
(55.4,59.9,1100,'<span class="pill" id="hx1">✋ mãos</span> <span class="pill" id="hx2">🦶 pés</span> <span class="pill" id="hx3">🙂 rosto</span>'),
(60.0,62.6,1200,'<span class="pill">🛑 a octreotida <b>pisa no freio</b></span>'),
(62.8,76.0,1040,'<div class="flags"><div><small>🇺🇸 EUA · FDA</small>Aprovada em 1988</div><div><small>🇧🇷 BRASIL · ANVISA</small>Registrada · no SUS para acromegalia</div></div>'),
(77.2,83.3,1150,'<span class="pill">✂️ encolher o peptídeo</span><br><span class="pill">🔑 guardar só a <b>parte que funciona</b></span>')]
STAMP=(27.4,1.0,'PROBLEMA!')
CTA=88.9
ANIMS=[(f'#ba{i}',7.7+i*0.12,'pop') for i in range(14)]+[(f'#bb{i}',37.7+i*0.1,'pop') for i in range(8)]+[('#cnt',28.5,'count'),('#hx1',55.5,'drop'),('#hx2',56.6,'drop'),('#hx3',57.4,'drop')]
DINGS=[7.7,28.5,62.8]
KEY=['1973,','ovelhas','freio','crescimento.','14','somatostatina.','pâncreas,','pare.','Nobel','1977.','3','minutos.','8','encolhida.','octreotida,','horas','acromegalia.','hipófise','mãos,','pés','rosto','FDA','1988.','Anvisa','SUS','receita','Obolari','educativo','próximo?']
