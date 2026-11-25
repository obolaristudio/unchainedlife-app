import math
T=80.39; TAG="PEPTÍDEOS · CICLOSPORINA"
REP={'peptídio,':'peptídeo','peptídio':'peptídeo','Borrel,':'Borel,','Sandos':'Sandoz,'}
SEQ=[(['figa','do'],['fígado'])]
KEY=['1969,','suíço','Noruega','terra','transplantes.','fungo','ciclosporina,','anel','11','contas.','invasor','ataca.','calmante','soldados','linfócitos','T,','curioso,','antibiótico.','fraco','descartado.','Borel,','Sandoz,','insistiu','rim,','fígado','coração','salto.','1983,','FDA','Anvisa','SUS.','acompanhamento','punhado','férias.','peptídeo']
cols=['#E53935','#F4C430','#CBEF4B','#4FC3F7','#B388FF']
ring=''.join(f'<i style="position:absolute;left:{150+120*math.cos(2*math.pi*i/11-math.pi/2)-24:.0f}px;top:{150+120*math.sin(2*math.pi*i/11-math.pi/2)-24:.0f}px;width:48px;height:48px;border-radius:50%;background:{cols[i%5]};box-shadow:inset -5px -5px 0 rgba(0,0,0,.25)"></i>' for i in range(11))
HEADERS=[('h0',0,9.0,'<div class="m">Férias na<br><span>Noruega</span> 🇳🇴</div>'),
('h1',9.0,18.7,'<div class="m"><span>Ciclosporina</span> 🍄</div>'),
('h2',18.7,34.4,'<div class="m">Como ela <span>age</span>? 🛡️</div>'),
('h3',34.4,57.9,'<div class="m">A <span>virada</span> 😮</div>'),
('h4',57.9,70.7,'<div class="m">Status pelo <span>mundo</span> 🌎</div>'),
('h5',70.7,T,'<div class="m">Tudo começou com<br>um punhado de <span>terra</span> 🌱</div>')]
OVERLAYS=[('o0',0.8,5.4,'top:1120px','<div class="big"><span id="yr">1950</span><small>um cientista suíço 🇨🇭 sai de férias</small></div>'),
('o0b',5.5,8.95,'top:1150px','<span class="pill" id="o0c" style="font-size:52px">🧳 e volta com um <b>saquinho de terra</b></span>'),
('o1',9.0,13.9,'','<div class="chips"><span class="pill" id="o1a">🍄 na terra: um <b>fungo</b></span><span class="pill" id="o1b">🧪 que fabricava a <b>ciclosporina</b></span></div>'),
('o1c',14.0,18.6,'top:1050px',f'<div style="position:relative;width:300px;height:300px;margin:0 auto;background:rgba(14,14,14,.8);border-radius:50%" id="ring">{ring}</div><div style="margin-top:14px"><span class="pill"><b id="n11">0</b> aminoácidos em <b>anel</b> 💍</span></div>'),
('o2',19.7,25.3,'','<div class="chips"><span class="pill" id="o2a">🫀 órgão novo → a defesa acha que é <b>invasor</b></span><span class="pill v" id="o2b">⚔️ e <b>ataca</b></span></div>'),
('o2c',25.4,34.3,'','<div class="chips"><span class="pill" id="o2d">😌 ciclosporina = <b>calmante</b> das defesas</span><span class="pill" id="o2e">🪖 acalma os <b>linfócitos T</b></span><span class="pill" id="o2f">✅ o órgão novo é <b>poupado</b></span></div>'),
('o3',34.4,39.95,'top:1150px','<span class="pill" id="o3a" style="font-size:52px">🔎 procuravam um <b>antibiótico</b></span>'),
('o3s',40.0,43.55,'top:880px','<div class="stamp r"><span id="st3">🗑️ QUASE FOI <b>PRO LIXO</b></span></div>'),
('o3b',43.6,53.5,'','<div class="chips"><span class="pill" id="o3c">👨‍🔬 Jean-François <b>Borel</b> · Sandoz 🇨🇭</span><span class="pill" id="o3d">💡 descobriu o efeito <b>calmante das defesas</b></span></div>'),
('o3e',53.6,57.8,'top:1120px','<div class="chips" style="flex-direction:row;justify-content:center;gap:12px"><span class="pill" id="t1">🫘 rim</span><span class="pill" id="t2">🟤 fígado</span><span class="pill" id="t3">❤️ coração</span></div><div style="margin-top:16px"><span class="pill" id="t4">transplantes deram um <b>salto</b> 📈</span></div>'),
('o4',58.0,70.6,'top:1100px','<div class="chips"><span class="pill" id="o4a">🇺🇸 FDA: <b>aprovada</b> em 1983</span><span class="pill" id="o4b">🇧🇷 Anvisa: <b>aprovada</b></span><span class="pill" id="o4c">🏥 no <b>SUS</b>, para transplantados</span><span class="pill v" id="o4d">🩺 sempre com <b>acompanhamento médico</b></span></div>'),
('o5',77.4,T,'top:1220px','<div class="cta"><span id="cta">Qual peptídeo eu explico? 💬</span></div>')]
SLIDES=[('#o1a',9.0),('#o1b',11.4),('#o2a',19.7),('#o2d',25.4),('#o2e',28.9),('#o2f',31.6),('#o3c',43.6),('#o3d',49.0),('#o4a',58.0),('#o4b',62.9),('#o4c',65.5),('#o4d',68.3)]
POPS=[('#o0c',5.5),('#o2b',23.4),('#o3a',34.4),('#t1',54.0),('#t2',54.6),('#t3',55.2),('#t4',56.0),('#cta',77.4)]
PUNCH=[9.0,18.7,25.4,53.6,70.7]
STAMPS=[40.0]; DINGS=[14.2,58.0]
JS='''tl.fromTo("#flash",{opacity:0.6},{opacity:0,duration:0.25},0);
tl.fromTo("#yr",{textContent:1950},{textContent:1969,duration:1.5,ease:"power2.out",snap:{textContent:1}},0.9);
tl.fromTo("#ring i",{scale:0},{scale:1,duration:0.15,stagger:0.12,ease:"back.out(3)"},14.1);
tl.to("#ring",{rotation:360,duration:4.5,ease:"none"},14.0);
tl.fromTo("#n11",{textContent:0},{textContent:11,duration:1.3,ease:"power1.out",snap:{textContent:1}},14.1);
tl.fromTo("#flash",{opacity:0.8},{opacity:0,duration:0.3},40.0);
tl.fromTo("#st3",{scale:3,opacity:0,rotation:-25},{scale:1,opacity:1,rotation:-6,duration:0.28,ease:"power3.in"},40.02);
tl.fromTo("#bg",{x:0},{x:-28,duration:0.05,yoyo:true,repeat:5},40.05);
tl.fromTo("#bg",{filter:"grayscale(0) brightness(1)"},{filter:"grayscale(1) brightness(0.55)",duration:0.12},40.0);
tl.to("#bg",{filter:"grayscale(0) brightness(1)",duration:0.2},43.3);
tl.to("#cta",{scale:1.06,duration:0.45,yoyo:true,repeat:2,ease:"sine.inOut"},77.9);'''
