T = 90.0
SERIE = 'ZICONOTIDA'
MUSIC = 'm184.mp3'
VS_END = 1.0
CTA = 86.3
REP = {'Recifes': 'recifes', 'Coral.': 'coral.', 'caloro': 'calouro', 'aides,': 'aids,'}
KEY = {'remédio','dor','veneno','caracol','mar','ziconotida','recifes','coral','lento','peixes','arpão','segundos','1970','utah','calouro','peptídeos','25','aminoácidos','colar','laboratório','nervos','cérebro','carro','estrada','portões','fecha','viagem','curioso','morfina','2004','111','53','%','18','placebo','fda','europa','2005','anvisa','graves','hospital','educativo','próximo','comenta'}
SCENES = [
 (0,2.5,'44869',0.5),(2.5,5.0,'47605',1),(5.0,7.2,'44868',1),(7.2,10.0,'44872',1),(10.0,13.0,'44973',1),
 (13.0,17.7,'44976',1),(17.7,23.5,'4733',1),(23.5,29.4,'23618',1),(29.4,33.4,'3957',1),(33.4,36.7,'17556',1),
 (36.7,41.9,'12866',1),(41.9,45.0,'5491',1),(45.0,49.8,'33747',1),(49.8,54.4,'4786',1),(54.4,60.3,'46367',1),
 (60.3,66.3,'4766',1),(66.3,73.0,'49010',1),(73.0,80.5,'7255',1),(80.5,90.0,'44868',12)]
HEADS = [
 (1.0,5.0,'Remédio para dor<br>que veio do <span>veneno</span> 🐚',''),
 (5.0,7.2,'O nome dele é…',''),
 (7.2,17.7,'O <span>caracol-cone</span> 🐌',''),
 (17.7,29.4,'A <span>descoberta</span> 🎓',''),
 (29.4,36.7,'<span>25</span> aminoácidos 📿',''),
 (36.7,49.8,'Como ela <span>age</span> 🚧',''),
 (49.8,54.4,'Detalhe <span>curioso</span> 🤓',''),
 (54.4,66.3,'O que o estudo<br><span>mostrou</span> 📊',''),
 (66.3,80.5,'Status pelo <span>mundo</span> 🌎',''),
 (80.5,86.3,'Obolari <span>Academy</span>','conteúdo educativo'),
 (86.3,90.0,'Comenta <span>aqui</span> 👇',''),
]
OVER = [
 (7.8,13.0,[('🪸 vive nos <b>recifes de coral</b>',8.1),('🐌 lento… mas <b>caça peixes</b>',10.1)]),
 (14.3,17.7,[('🎯 paralisa a presa <b>em segundos</b>',15.5)]),
 (18.3,29.4,[('🎓 Universidade de Utah · <b>fim dos anos 70</b>',18.3),('🧑‍🎓 um <b>calouro</b> ajudou a descobrir',22.5),('🧪 o veneno é cheio de <b>peptídeos</b>',24.6)]),
 (33.4,36.7,[('🏭 hoje: feita em <b>laboratório</b>',33.5)]),
 (37.8,49.8,[('🚗 a dor viaja como um <b>carro na estrada</b>',37.9),('🚧 no caminho há <b>portões</b>',42.0),('⛔ a ziconotida <b>fecha um portão</b>',45.1)]),
 (51.3,54.4,[('💊 <b>não</b> é da família da morfina',51.4)]),
 (54.8,60.3,[('📅 2004 · <b>111 pessoas</b> com dor forte',55.1),('por câncer ou aids',58.5)]),
 (67.7,80.5,[('🇺🇸 FDA: <b>aprovada em 2004</b> (dor crônica muito grave)',67.8),('🇪🇺 Europa: <b>aprovada em 2005</b>',73.0),('🇧🇷 Anvisa: <b>sem registro encontrado</b>',75.4),('🏥 só em <b>casos graves, no hospital</b>',78.1)]),
]
BIGS = [
 (5.6,7.2,'<b>ZICONOTIDA</b>',None),
 (60.3,66.3,'<b><span id="g1_n">0</span>%</b>',(53,60.5)),
]
STAMPS = [(13.0,14.2,'ARPÃO! 🎯')]
CSS = '#g0 span{font-size:140px}#g1 span{font-size:230px}#vs2{position:absolute;z-index:6;left:0;right:0;top:1080px;text-align:center}#vs2 span{display:inline-block;background:rgba(14,14,14,.88);border:3px solid #CBEF4B;font-size:46px;padding:12px 28px;border-radius:18px}#beads{position:absolute;z-index:6;left:90px;right:90px;top:880px;display:flex;flex-wrap:wrap;justify-content:center;gap:12px}#beads i{display:block;width:70px;height:70px;border-radius:50%;box-shadow:inset -7px -7px 0 rgba(0,0,0,.25)}'
cols = ['#CBEF4B','#F4C430','#4FC3F7','#B388FF','#FF8A65']
HTML_EXTRA = ('<div id="vs2" class="clip" data-start="63.8" data-duration="2.5"><span>placebo: só <b style="color:#CBEF4B">18%</b> · dor caiu em média</span></div>'
  '<div id="beads" class="clip" data-start="29.4" data-duration="4.0">' + ''.join(f'<i id="bd{i}" style="background:{cols[i%5]}"></i>' for i in range(25)) + '</div>')
EXTRA_JS = ['tl.fromTo("#vs2 span",{opacity:0,y:30},{opacity:1,y:0,duration:0.3},63.8);'] + [f'tl.fromTo("#bd{i}",{{scale:0}},{{scale:1,duration:0.15,ease:"back.out(3)"}},{31.4+i*0.06:.2f});' for i in range(25)] + ['tl.to("#beads i",{y:900,rotation:180,duration:0.6,stagger:0.01,ease:"power2.in"},33.0);']
