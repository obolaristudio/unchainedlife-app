D='/tmp/claude-0/-home-user-unchainedlife-app/7a97ed93-910e-5bcd-a596-7dedfde0b525/scratchpad/calc'
SERIE='CALCITONINA'
REP={'o':'o','peptídio':'peptídeo','Albolária':'Obolari','Obolári':'Obolari'}
SCENES=[(0,1.7,'45917',2),(1.7,3.1,'4291',1),(3.1,7.0,'18084',1),(7.0,10.9,'23618',1),(10.9,13.1,'4765',1),(13.1,18.0,'3769',0),
(18.0,21.3,'46056',1),(21.3,25.7,'14729',1),(25.7,28.7,'48655',2),(28.7,31.3,'25480',1),(31.3,35.0,'47995',1),(35.0,37.9,'46057',1),
(37.9,39.8,'44974',1),(39.8,45.9,'51600',1),(45.9,50.2,'17497',1),(50.2,54.0,'5769',1),(54.0,58.5,'5640',1),(58.5,61.7,'5433',2),
(61.7,65.2,'6562',1),(65.2,68.5,'48790',1),(68.5,73.0,'4291',8),(73.0,77.7,'47408',1),(77.7,None,'15919',1)]
HEADS=[(0,3.1,'<div class="s">PEPTÍDEOS · SÉRIE</div><div class="m">Um remédio de osso<br>que veio do <span>salmão</span> 🐟</div>'),
(3.1,13.1,'<div class="s">ANOS 60 · CANADÁ 🇨🇦</div><div class="m">A descoberta da<br><span>calcitonina</span></div>'),
(13.1,21.3,'<div class="s">O QUE É</div><div class="m">Um colar de<br><span>32 contas</span> 📿</div>'),
(21.3,37.9,'<div class="s">COMO AGE</div><div class="m">O osso é uma<br><span>obra sem fim</span> 🏗️</div>'),
(37.9,51.5,'<div class="s">A SURPRESA</div><div class="m">A do peixe é<br><span>mais forte</span> 💪</div>'),
(51.5,68.5,'<div class="s">STATUS PELO MUNDO</div><div class="m">Virou <span>remédio</span> 💊</div>'),
(68.5,77.7,'<div class="s">CURIOSIDADE</div><div class="m">A glândula que<br><span>se mudou</span> 🤯</div>'),
(77.7,None,'<div class="s">OBOLARI ACADEMY</div><div class="m">Conteúdo<br><span>educativo</span></div>')]
beads=''.join(f'<i id="bd{i}" style="background:{c}"></i>' for i,c in enumerate(['#CBEF4B','#3D7BFF','#FBFAF6','#CBEF4B']*8))
OVS=[(1.0,3.1,1150,'<span class="pill">🦴 osteoporose · 🐟 salmão</span>'),
(5.2,10.9,1180,'<span class="pill">👨‍🔬 <b>Harold Copp</b></span><br><span class="pill">⬇️ baixa o <b>cálcio do sangue</b></span>'),
(14.2,18.0,1060,f'<div class="beads">{beads}</div>'),
(18.3,21.3,1200,'<span class="pill">🦋 feita na <b>tireoide</b></span>'),
(25.7,28.7,1200,'<span class="pill r">🔨 células que <b>derrubam</b></span>'),
(28.7,31.3,1200,'<span class="pill">🧱 células que <b>constroem</b></span>'),
(31.3,37.9,1150,'<span class="pill">🛑 calcitonina = <b>freio</b></span><br><span class="pill">nas que <b>derrubam</b></span>'),
(39.8,45.9,1120,'<span class="pill">🐟 salmão &gt; 🧍 humano</span><br><span class="pill"><b>mais forte</b> e <b>dura mais</b></span>'),
(46.0,50.2,1200,'<span class="pill">🧪 copiada em <b>laboratório</b></span>'),
(51.6,61.7,1060,'<div class="flags"><div><small>🇺🇸 EUA · FDA</small>Aprovada desde os anos 70 (doenças dos ossos)</div><div><small>🇧🇷 BRASIL · ANVISA</small>Tem registro</div></div>'),
(62.0,68.5,1180,'<span class="pill">🩺 hoje: usos <b>mais específicos</b></span>'),
(70.0,77.7,1140,'<span class="pill">🐟 no salmão: <b>glândula separada</b></span><br><span class="pill">🤰 em nós: junta-se à <b>tireoide</b></span>')]
STAMP=(37.9,1.9,'ESPERA…')
CTA=83.4
ANIMS=[(f'#bd{i}',14.3+i*0.1,'pop') for i in range(32)]
DINGS=[14.3,51.6,70.0]
KEY=['ossos','salmão.','Canadá,','cálcio','calcitonina.','32','tireoide.','casa','derrubam','constroem','freio','surpresa.','forte','laboratório.','remédio.','FDA','Anvisa.','glândula','tireoide','Obolari','educativo','próximo?']
SKIP=[('virou','o','remédio.')]
