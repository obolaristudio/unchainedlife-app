T = 88.4
SERIES = 'PEPTÍDEOS · MAZDUTIDA'
MUSIC = '/tmp/hfa/m1023.mp3'
REP = {'peptídio,': 'peptídeo:', 'ozenpik.': 'Ozempic.', 'Inovent,': 'Innovent,'}
PAIRS = {('Maz','Dutida'):'mazdutida', ('Maz','Dutida.'):'mazdutida.', ('Maz','Dutida,'):'mazdutida,', ('GLP','-1,'):'GLP-1,', ('GLP','-GON,'):'glucagon,', ('El','Lili,'):'Eli Lilly,'}
KEY = ['mazdutida', 'mazdutida.', 'China', 'peptídeo:', 'colar.', 'dois', 'GLP-1,', 'Ozempic.', 'satisfeito.', 'glucagon,', 'acelerador.', 'fígado.', 'chave', 'fechaduras.', 'Lilly,', 'Innovent,', '48', '15%', 'placebo,', 'virada.', '2025,', 'aprovou', 'primeira', 'FDA', 'estudo.', 'Anvisa.', 'chinesas.', 'educativo', 'próximo?']
SCENES = [
 (0, 3.5, '5433', 2), (3.5, 6.0, '31010', 0.5), (6.0, 8.64, '13312', 1), (8.64, 12.0, '4786', 1), (12.0, 16.82, '5485', 1),
 (16.82, 20.8, '26096', 0.5), (20.8, 24.5, '5665', 1), (24.5, 28.04, '26085', 1), (28.04, 32.46, '722', 3), (32.46, 36.44, '32809', 1),
 (36.44, 39.34, '5563', 1), (39.34, 42.6, '28389', 1), (42.6, 45.88, '31042', 0.5), (45.88, 49.5, '22999', 1), (49.5, 52.6, '5850', 1),
 (52.6, 55.06, '4773', 1), (55.06, 57.26, '5767', 1), (57.26, 59.12, '30095', 1), (59.12, 62.6, '42111', 0.5), (62.6, 66.72, '20806', 0.5),
 (66.72, 71.1, '42117', 0.5), (71.1, 74.12, '42080', 1), (74.12, 77.24, '28611', 0.5), (77.24, 79.5, '23032', 2), (79.5, 83.4, '4629', 1), (83.4, 88.4, '1086', 1)]
HEADS = [
 (1.1, 8.64, '<div class="m">Já é remédio de farmácia<br>na <span>China</span> 🇨🇳</div>'),
 (8.64, 16.82, '<div class="m">O que é a<br><span>mazdutida</span>? 🧬</div>'),
 (16.82, 36.44, '<div class="m"><span>2 mensageiros</span><br>ao mesmo tempo</div><div class="s">os dois vêm do intestino</div>'),
 (36.44, 45.88, '<div class="m">🔑 1 chave,<br><span>2 fechaduras</span></div>'),
 (45.88, 57.26, '<div class="m">O que o <span>estudo</span><br>mostrou 📊</div><div class="s">48 semanas · adultos com obesidade</div>'),
 (57.26, 66.72, '<div class="m">A <span>virada</span> 🌏</div>'),
 (66.72, 79.5, '<div class="m">Status pelo <span>mundo</span> 🌎</div>'),
 (79.5, 88.4, '<div class="m">Qual peptídeo<br><span>eu explico</span> no próximo? 💬</div>')]
OVS = [
 ([20.8, 28.04, [(20.9, '🧠 <b>GLP-1</b>: avisa que você está satisfeito'), (25.3, 'mesmo caminho do <b>Ozempic</b>')], 1180]),
 ([28.04, 36.44, [(28.1, '⚡ <b>glucagon</b>: o acelerador'), (32.5, '🔥 mais gasto de energia'), (34.2, 'menos <b>gordura no fígado</b>')], 1140]),
 ([39.34, 45.88, [(39.5, '🇺🇸 nasceu na <b>Eli Lilly</b>'), (42.7, '🇨🇳 licenciada para a <b>Innovent</b>')], 1180]),
 ([66.72, 79.5, [(66.8, '🇨🇳 China: <b>aprovada</b> (jun/2025)'), (66.9 + 0.8, '🇺🇸 FDA: <b>em estudo</b>'), (71.2, '🇧🇷 Anvisa: <b>sem registro</b>'), (74.2, '!🔬 estudos grandes: <b>pessoas chinesas</b>')], 1080]),
]
OVS = [tuple(o) for o in OVS]
BIGS = [
 (47.6, 55.0, '−<span id="n15">0</span>%<div style="font-size:44px;font-weight:700;margin-top:10px">do peso, em média (até quase 15%)</div>', 1130, 160),
 (55.06, 57.26, '<b>−0,5%</b><div style="font-size:44px;font-weight:700;margin-top:10px">no grupo placebo</div>', 1130, 150),
 (60.6, 66.7, '<b>1ª</b> do mundo<div style="font-size:42px;font-weight:700;margin-top:10px">dupla GLP-1 + glucagon aprovada</div>', 1130, 130),
]
COUNTERS = [('#n15', 47.7, 1.6, 0, 15)]
BEADS = (12.4, 16.7, 18)
STAMP = (57.3, 'ESPERA…')
PUNCH = [8.64, 20.8, 28.04, 36.44, 47.7, 59.12, 64.44]
CTA = 85.2
CTA_TXT = 'Comenta aqui 👇'
