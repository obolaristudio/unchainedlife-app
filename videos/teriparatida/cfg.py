T=84.6
TAG='· PEPTÍDEOS · TERIPARATIDA'
REP={}
KEY=['osso','novo,','hormônio.','teriparatida.','34','paratireoide,','pescoço.','casa','reforma','derruba,','constrói.','derruba.','diferente.','acorda','ritmo.','pulsos','2001,','1.637','14','5','100,','65%','2002,','FDA','2020,','Anvisa','SUS','contrário.','cálcio','próximo?','Comenta']
HEADS=[(0,'Um peptídeo que ajuda a <span>construir osso novo</span> 🦴'),(5.52,'O que <span>é</span>? 🧬'),(14.74,'Como ele <span>age</span>? 🏗️'),(28.62,'O segredo é o <span>ritmo</span> ⏱️'),(34.56,'O que o <span>estudo</span> mostrou 📊'),(50.08,'Status pelo <span>mundo</span> 🌎'),(67.78,'Curiosidade 🤓'),(76.48,'Conteúdo <span>educativo</span> 🎓')]
OVS=[
 dict(k='chips',t=3.54,end=5.52,items=[(3.54,'🧩 …e é um <b>pedaço de um hormônio</b>')]),
 dict(k='big',t=5.86,end=7.48,h='TERIPARATIDA',st='font-size:110px;color:#CBEF4B'),
 dict(k='chips',t=7.7,items=[(8.6,'🔢 os <b>primeiros 34 aminoácidos</b>'),(10.44,'🧬 do <b>hormônio da paratireoide</b>'),(12.2,'📍 glândulas pequeninas <b>no pescoço</b>')]),
 dict(k='chips',t=15.5,items=[(15.5,'🏠 osso = <b>casa em reforma constante</b>'),(17.9,'🔨 uma equipe <b>derruba</b>','v'),(19.12,'🧱 outra equipe <b>constrói</b>'),(20.5,'💊 a maioria dos remédios <b>segura quem derruba</b>','v')]),
 dict(k='stamp',t=24.42,dur=1.1,h='DIFERENTE!'),
 dict(k='chips',t=25.6,end=28.62,items=[(26.52,'⏰ ela <b>acorda a equipe que constrói</b>')]),
 dict(k='chips',t=30.56,end=34.56,items=[(30.56,'⚡ em <b>pulsos curtos</b>'),(32.0,'🦴 o sinal <b>estimula a construção</b> de osso')]),
 dict(k='count',t=37.72,end=41.5,top=1130,pre='mulheres no estudo (2001)',to=1637,suf=''),
 dict(k='bars',t=41.58,end=50.08,top=1040,title='FRATURAS NOVAS NA COLUNA · A CADA 100 · ≈65% A MENOS',bars=[(43.0,'placebo',14,'14','#7B5CFF'),(45.1,'teriparatida',5,'5','#CBEF4B')]),
 dict(k='chips',t=50.2,top=1080,items=[(50.2,'🇺🇸 FDA: <b>aprovada em 2002</b> para osteoporose'),(57.32,'📄 2020: alerta em destaque <b>sai da bula</b>'),(63.18,'🇧🇷 Anvisa: <b>registrada</b> · no SUS para casos graves')]),
 dict(k='chips',t=68.66,items=[(68.66,'🔁 o mesmo hormônio <b>alto o tempo todo</b>…'),(72.24,'↩️ faz o contrário: <b>tira cálcio do osso</b>','v')]),
 dict(k='big',t=74.72,end=76.48,h='tudo depende do <span style="color:#CBEF4B">ritmo</span>',st='font-size:88px'),
 dict(k='chips',t=76.6,end=81.88,items=[(77.0,'não é recomendação médica','v'),(79.1,'nem sugestão de uso','v')]),
 dict(k='cta',t=81.88,h='Qual peptídeo no próximo? 💬'),
]
SECS=[(0,[12345,48790]),(5.52,[23618,21454,33268]),(14.74,[1459,1458,20874,31450]),(28.62,[14729,4773]),(34.56,[16388,23300,12866,33371]),(50.08,[17625,5491,20031]),(67.78,[1440,32616]),(76.48,[32748,12533])]
CUTS=[];CLIPS=[]
b=[s[0] for s in SECS]+[T]
for i,(t,cl) in enumerate(SECS):
    n=len(cl); L=(b[i+1]-t)/n
    for j,c in enumerate(cl): CUTS.append(round(t+j*L,2)); CLIPS.append(c)
PUNCH=[5.86,24.42,45.1,74.72]
