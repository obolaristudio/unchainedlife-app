T=83.7
TAG='· PEPTÍDEOS · AFAMELANOTIDA'
REP={}
KEY=['80,','bronzeado,','sol.','remédio','coisa.','Arizona,','mensageiro','melanina,','pigmento','forte','durável.','Melanotan-1,','afamelanotida.','guarda-sol','chave','fechadura','rara','protoporfiria','eritropoiética.','queimadura,','minutos','sem','dor','placebo.','2014,','Europa','2019,','FDA,','Anvisa.','irmão','Melanotan-2,','PT-141.','próximo?','Comenta']
HEADS=[(0,'O peptídeo do <span>bronzeado sem sol</span> ☀️'),(8.34,'A <span>história</span> 🇺🇸'),(27.28,'Como ele <span>age</span>? 🔑'),(36.08,'Onde virou <span>remédio</span> 💊'),(47.34,'O que os <span>estudos</span> mostraram 📊'),(53.48,'Status pelo <span>mundo</span> 🌎'),(66.16,'Curiosidade 🤓'),(75.64,'Conteúdo <span>educativo</span> 🎓')]
OVS=[
 dict(k='chips',t=0.32,end=5.22,items=[(0.32,'📅 <b>anos 80</b>'),(3.42,'☀️ bronzeado <b>sem sol</b>?')]),
 dict(k='stamp',t=5.3,dur=1.6,h='VIROU REMÉDIO…'),
 dict(k='chips',t=6.9,end=8.34,items=[(6.9,'…para <b>outra coisa</b> 🤔')]),
 dict(k='chips',t=8.4,end=19.9,items=[(8.4,'🎓 <b>Universidade do Arizona</b>'),(12.54,'📨 copiaram um <b>mensageiro natural</b>'),(15.1,'🧴 ele avisa a pele: <b>fabrique melanina</b>'),(18.3,'🎨 melanina = <b>o pigmento que escurece a pele</b>')]),
 dict(k='chips',t=20.06,end=25.3,items=[(20.06,'💪 cópia <b>mais forte</b>'),(22.28,'⏳ e <b>mais durável</b>')]),
 dict(k='big',t=23.3,end=27.28,top=1400,h='Melanotan 1 = <span style="color:#CBEF4B">afamelanotida</span>',st='font-size:62px'),
 dict(k='chips',t=28.56,items=[(28.56,'⛱️ melanina = <b>guarda-sol</b> das células'),(31.92,'🔑 peptídeo = <b>a chave</b>'),(33.9,'🏭 abre a fechadura da <b>fábrica de melanina</b>')]),
 dict(k='big',t=37.52,end=41.6,top=1150,h='protoporfiria<br><span style="color:#CBEF4B">eritropoiética</span>',st='font-size:70px'),
 dict(k='chips',t=41.6,end=47.34,items=[(41.6,'🔥 dor forte, <b>como queimadura</b>'),(45.28,'⏱️ <b>poucos minutos</b> depois de pegar sol','v')]),
 dict(k='chips',t=48.36,end=53.48,items=[(48.36,'☀️ <b>mais tempo no sol sem dor</b>'),(52.4,'📉 do que quem recebeu <b>placebo</b>','v')]),
 dict(k='chips',t=53.48,top=1080,items=[(53.48,'🇪🇺 Europa: <b>aprovada em 2014</b>'),(57.54,'🇺🇸 FDA: <b>aprovada em 2019</b>'),(61.9,'🎯 só para <b>essa doença rara</b>'),(63.36,'🇧🇷 Anvisa: <b>ainda sem registro</b>','v')]),
 dict(k='chips',t=67.04,items=[(67.04,'👬 o <b>irmão</b>: Melanotan 2'),(69.32,'🛤️ seguiu <b>outro caminho</b>')]),
 dict(k='big',t=73.76,end=75.64,h='PT-141',st='font-size:170px;color:#CBEF4B'),
 dict(k='chips',t=75.8,end=80.9,items=[(76.2,'não é recomendação médica','v'),(78.3,'nem sugestão de uso','v')]),
 dict(k='cta',t=80.9,h='Qual peptídeo no próximo? 💬'),
]
SECS=[(0,[31793,3133]),(8.34,[2092,23537,4773,34643,33934]),(27.28,[26128,14971]),(36.08,[25163,1086,16399]),(47.34,[25158,32285]),(53.48,[5491,17497,15064]),(66.16,[34371,4508]),(75.64,[18240,33472])]
CUTS=[];CLIPS=[]
b=[s[0] for s in SECS]+[T]
for i,(t,cl) in enumerate(SECS):
    n=len(cl); L=(b[i+1]-t)/n
    for j,c in enumerate(cl): CUTS.append(round(t+j*L,2)); CLIPS.append(c)
PUNCH=[5.3,23.3,37.52,73.76]
