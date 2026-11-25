T=77.11; TAG="PEPTÍDEOS · GLUCAGON"
REP={'dispensa':'despensa','dispensa.':'despensa.','hagem':'agem','Obolary':'Obolari','nasal,':'nasal.','conteúdo':'Conteúdo'}
SEQ=[(['agem','três'],['agem','em','três']),(['reta','trutida,'],['retatrutida,']),(['dele','e'],['dele!','E'])]
KEY=['1922,','estranha.','subir,','descer.','culpado','1923,','glucagon.','29','colar.','contrário','fígado','despensa','guarda','abre','horas','gangorra.','surpresa.','GLP-1','Ozempic?','parecido','retatrutida,','três','fechaduras','FDA','Anvisa,','emergência','spray','nasal,','peptídeo']
cols=['#E53935','#F4C430','#CBEF4B','#4FC3F7','#B388FF']
beads=''.join(f'<i style="background:{cols[i%5]}"></i>' for i in range(29))
HEADERS=[('h0',0,10.8,'<div class="m">Um <span>mistério</span><br>no pâncreas 🧪</div>'),
('h1',10.8,24.7,'<div class="m"><span>Glucagon</span> 🧬</div><div class="s">o "irmão oposto" da insulina</div>'),
('h2',24.7,38.6,'<div class="m">Como ele <span>age</span>? ⚖️</div>'),
('h3',38.6,56.5,'<div class="m">A <span>surpresa</span> 😮</div>'),
('h4',56.5,72.5,'<div class="m">Status pelo <span>mundo</span> 🌎</div>'),
('h5',72.5,T,'<div class="m">Um peptídeo<br>por <span>vídeo</span></div>')]
OVERLAYS=[('o0',0.8,5.6,'top:1120px','<div class="big"><span id="yr">1900</span><small>a insulina tinha acabado de ser descoberta</small></div>'),
('o0b',5.7,10.7,'top:1150px','<span class="pill" id="o0c" style="font-size:52px">🩸 o açúcar <b>subia</b> em vez de descer?!</span>'),
('o1',14.6,18.1,'top:1100px','<div class="big" id="gname" style="color:#CBEF4B;font-size:150px">GLUCAGON<small style="color:#fff">batizado em 1923</small></div>'),
('o1b',18.2,22.5,'top:1100px',f'<div class="beads">{beads}</div><div style="margin-top:16px"><span class="pill"><b id="n29">0</b> aminoácidos</span></div>'),
('o1c',22.6,24.6,'top:1150px','<span class="pill v" id="o1d" style="font-size:52px">🔄 faz o <b>contrário</b> da insulina</span>'),
('o2',24.7,36.0,'top:1110px','<div class="chips"><span class="pill" id="o2a">🏠 fígado = <b>despensa de açúcar</b></span><span class="pill" id="o2b">🔑 insulina <b>guarda</b> o açúcar</span><span class="pill" id="o2c">🚪 glucagon <b>abre</b> a despensa</span><span class="pill" id="o2d">⏰ ex.: muitas horas <b>sem comer</b></span></div>'),
('o2s',36.1,38.5,'top:1100px','<div class="big" id="seesaw" style="font-size:220px">⚖️</div>'),
('o3w',38.6,40.2,'top:880px','<div class="stamp"><span id="esp">ESPERA…</span></div>'),
('o3',40.3,47.5,'','<div class="chips"><span class="pill" id="o3a">💊 GLP-1 = família do <b>Ozempic</b></span><span class="pill" id="o3b" style="font-size:50px">GLP = <b>peptídeo parecido com o glucagon</b> 🤯</span></div>'),
('o3c',47.6,56.4,'','<div class="chips"><span class="pill" id="o3d">🆕 remédios novos, ex.: <b>retatrutida</b></span><span class="pill" id="o3e">🔐🔐🔐 <b>3 fechaduras</b> ao mesmo tempo</span><span class="pill" id="o3f">1 delas = a do <b>glucagon</b></span></div>'),
('o4',57.0,72.4,'top:1100px','<div class="chips"><span class="pill" id="o4a">🇺🇸 FDA: <b>aprovado</b></span><span class="pill" id="o4b">🇧🇷 Anvisa: <b>aprovado</b></span><span class="pill" id="o4c">🚨 remédio de <b>emergência</b> (açúcar muito baixo)</span><span class="pill" id="o4d">👃 EUA: versão em <b>spray nasal</b></span></div>'),
('o5',74.1,T,'top:1220px','<div class="cta"><span id="cta">Qual peptídeo eu explico? 💬</span></div>')]
SLIDES=[('#o2a',24.7),('#o2b',27.2),('#o2c',29.4),('#o2d',33.2),('#o3a',40.3),('#o3d',47.6),('#o3e',50.5),('#o4a',57.3),('#o4b',59.8),('#o4c',62.0),('#o4d',66.2)]
POPS=[('#o0c',5.7),('#o1d',22.6),('#o3f',54.3),('#cta',74.1)]
PUNCH=[10.8,14.6,22.6,43.4,54.3]
STAMPS=[38.6,43.4]; DINGS=[18.4,14.6,57.3]
JS='''tl.fromTo("#flash",{opacity:0.6},{opacity:0,duration:0.25},0);
tl.fromTo("#yr",{textContent:1900},{textContent:1922,duration:1.5,ease:"power2.out",snap:{textContent:1}},0.9);
tl.fromTo("#gname",{scale:2.4,opacity:0},{scale:1,opacity:1,duration:0.3,ease:"power4.out"},14.6);
tl.fromTo("#flash",{opacity:0.6},{opacity:0,duration:0.3},14.6);
tl.fromTo("#n29",{textContent:0},{textContent:29,duration:1.4,ease:"power1.out",snap:{textContent:1}},18.4);
tl.fromTo("#o1b .beads i",{scale:0},{scale:1,duration:0.12,stagger:0.045,ease:"back.out(3)"},18.3);
tl.fromTo("#seesaw",{rotation:-18,scale:0.5,opacity:0},{rotation:18,scale:1,opacity:1,duration:0.6,ease:"back.out(2)"},36.1);
tl.to("#seesaw",{rotation:-18,duration:0.6,yoyo:true,repeat:2,ease:"sine.inOut"},36.7);
tl.fromTo("#flash",{opacity:0.8},{opacity:0,duration:0.3},38.6);
tl.fromTo("#esp",{scale:3,opacity:0},{scale:1,opacity:1,duration:0.25,ease:"power3.in"},38.62);
tl.fromTo("#bg",{filter:"grayscale(0) brightness(1)"},{filter:"grayscale(1) brightness(0.55)",duration:0.12},38.6);
tl.to("#bg",{filter:"grayscale(0) brightness(1)",duration:0.2},40.0);
tl.fromTo("#o3b",{opacity:0,scale:3},{opacity:1,scale:1,duration:0.3,ease:"power4.out"},43.4);
tl.fromTo("#flash",{opacity:0.7},{opacity:0,duration:0.3},43.4);
tl.fromTo("#bg",{x:0},{x:-26,duration:0.05,yoyo:true,repeat:5},43.45);
tl.to("#cta",{scale:1.06,duration:0.45,yoyo:true,repeat:2,ease:"sine.inOut"},74.6);'''
