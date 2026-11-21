T = 88.0
SERIE = 'KISSPEPTINA'
MUSIC = 'm127.mp3'
VS_END = 1.1
CTA = 84.0
REP = {'Peptina': 'peptina', 'Peptina.': 'peptina.', 'Obolary': 'Obolari'}
KEY = {'beijo','interruptor','puberdade','kiss','peptina','kisspeptina','hershey','chocolate','kisses','melanoma','1','surpresa','2003','fechadura','central','chave','liga','ovários','testículos','ideia','fertilização','vitro','2014','londres','60','95','%','fda','anvisa','europa','pesquisa','pequenos','educativo','próximo','comenta'}
SCENES = [
 (0,2.7,'4664',0.5),(2.7,6.5,'4624',1),(6.5,8.8,'5485',1),(8.8,12.3,'4206',1),(12.3,17.1,'41117',1),
 (17.1,21.5,'4773',1),(21.5,25.0,'3955',1),(25.0,30.3,'5661',1),(30.3,36.6,'46749',1),(36.6,42.0,'5636',1),
 (42.0,48.2,'17497',1),(48.2,53.0,'6294',1),(53.0,60.3,'24876',1),(60.3,66.0,'4042',1),(66.0,72.0,'46749',12),
 (72.0,78.4,'17497',8),(78.4,88.0,'26597',2)]
HEADS = [
 (1.1,6.5,'Um peptídeo com<br>nome de <span>beijo</span> 💋',''),
 (6.5,8.8,'O nome dele é…',''),
 (8.8,17.1,'Onde tudo <span>começou</span> 📍',''),
 (17.1,25.0,'Um gene contra o<br><span>câncer de pele</span> 🧬',''),
 (25.0,36.6,'A <span>surpresa</span> de 2003 😮',''),
 (36.6,48.2,'Como ela <span>age</span> 🔑',''),
 (48.2,66.0,'O que os estudos<br><span>mostraram</span> 🧪',''),
 (66.0,78.4,'Status pelo <span>mundo</span> 🌎',''),
 (78.4,84.0,'Obolari <span>Academy</span>','conteúdo educativo'),
 (84.0,88.0,'Comenta <span>aqui</span> 👇',''),
]
OVER = [
 (3.6,6.5,[('🔌 o <b>interruptor da puberdade</b>',3.7)]),
 (9.6,17.1,[('📍 Hershey, EUA · <b>1996</b>',9.8),('🍫 a cidade do chocolate <b>Kisses</b>',14.8)]),
 (18.4,25.0,[('🧬 um gene que <b>freava o melanoma</b>',18.5),('nome do gene: <b>KiSS-1</b>',22.9)]),
 (27.9,36.6,[('🔒 sem a <b>fechadura</b> da kisspeptina…',31.6),('…a pessoa <b>não entrava na puberdade</b>',34.4)]),
 (37.8,48.2,[('🧠 o cérebro tem uma <b>central dos hormônios</b>',37.9),('🔑 a kisspeptina é a <b>chave</b> que liga',41.0),('⚡ acorda <b>ovários e testículos</b>',44.2)]),
 (50.4,60.2,[('🧪 ideia: usar na <b>fertilização in vitro</b>',50.4),('🇬🇧 Londres · 2014: ajudou os <b>óvulos a amadurecer</b>',53.2)]),
 (67.6,78.4,[('🇺🇸 FDA: <b>ainda em estudo</b>',67.7),('🇧🇷 Anvisa: <b>sem registro</b>',71.5),('🇪🇺 Europa: <b>em pesquisa</b>',73.7),('👥 em pessoas, os estudos <b>ainda são pequenos</b>',75.8)]),
]
BIGS = [
 (7.2,8.8,'<b>KISSPEPTINA</b>',None),
 (60.3,66.0,'<b><span id="g1_n">0</span>%</b>',(95,62.4)),
]
STAMPS = [(26.7,27.8,'SURPRESA!')]
CSS = '#g0 span{font-size:132px}#g1 span{font-size:230px}#g1sub{position:absolute;z-index:6;left:0;right:0;top:1060px;text-align:center}#g1sub span{display:inline-block;background:rgba(14,14,14,.88);border:3px solid #CBEF4B;font-size:44px;padding:12px 28px;border-radius:18px}'
HTML_EXTRA = '<div id="g1sub" class="clip" data-start="61.0" data-duration="5.0"><span>60 mulheres: óvulos amadureceram em <b style="color:#CBEF4B">95%</b></span></div>'
EXTRA_JS = ['tl.fromTo("#g1sub span",{opacity:0,y:30},{opacity:1,y:0,duration:0.3},61.0);']
