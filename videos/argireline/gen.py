# Reel Argireline (botox em pote? mito) — uso: python3 gen.py <pasta_de_trabalho> <pasta_stock>
import sys, json; sys.path.insert(0, '/home/user/unchainedlife-app/videos')
from lib_reel import build_bg, build_html, caption_groups, beads
WD, STOCK = sys.argv[1], sys.argv[2]
S = json.load(open('/home/user/unchainedlife-app/videos/argireline/scenes.json'))
W = json.load(open(f'{WD}/vwords.json')); T = 90.0
rep = {'peptídio': 'peptídeo', 'Acetil': 'acetil', 'Exapeptidio': 'hexapeptídeo', 'tedacinho': 'pedacinho',
       'Snap': 'SNAP', 'anvisa': 'Anvisa', 'acetil': 'acetyl', 'exapeptide': 'hexapeptide', 'Então,': 'Então'}
groups = caption_groups(W, rep, merges=[('SNAP', '25', 'SNAP-25')])
KEY = {'botox', 'pote', 'argireline', 'argireline.', '6', 'espanha', 'cosméticos', 'universidade', 'músculo', 'nervo',
       'zíper', 'snap-25', 'dente', 'falso', 'fraco', '2002', '10', '30', '30%', '2013', 'china', '60', 'metade', 'ninguém',
       'mito', 'meses', 'pele', 'suave', 'cosmético', 'remédio', 'fda', 'anvisa', 'banheiro', 'rótulo', 'próximo', 'hexapeptídeo', 'hexapeptide'}
heads = [
 ('h0', 0, 4.1, '<div class="s">Existe mesmo um</div><div class="m">“botox em <span>pote</span>”? 🤔</div>'),
 ('h1', 4.1, 13.4, '<div class="m"><span>Argireline</span></div><div class="s">acetil hexapeptídeo-8</div>'),
 ('h2', 13.4, 18.9, '<div class="m">Nasceu na <span>Espanha</span> 🇪🇸</div><div class="s">começo dos anos 2000</div>'),
 ('h3', 18.9, 35.9, '<div class="m">Como ele <span>age</span>? ⚙️</div>'),
 ('h4', 35.9, 55.1, '<div class="m">O que os <span>estudos</span><br>mostraram 🔬</div>'),
 ('h5', 55.1, 66.9, '<div class="m">Botox em pote?</div>'),
 ('h6', 66.9, 78.0, '<div class="m">Status pelo <span>mundo</span> 🌎</div>'),
 ('h7', 78.0, 84.3, '<div class="m"><span>Curiosidade</span> 🧴</div>'),
 ('h8', 84.3, T, '<div class="m">Qual é o <span>próximo</span>? 💬</div>'),
]
ovs = [
 ('o1', 7.2, 10.2, beads(6) + '<div style="margin-top:14px"><span class="pill"><b>6</b> aminoácidos = colar de 6 contas</span></div>', 1150, [('6', 7.3, 'beads')]),
 ('o2', 15.9, 18.9, '<div class="chips"><span class="pill" id="o2a">🧴 empresa de <b>cosméticos</b></span><span class="pill" id="o2b">🎓 + <b>universidade</b></span></div>', 1200, [('#o2a', 16.8, 'slide'), ('#o2b', 18.0, 'slide')]),
 ('o3', 19.6, 24.6, '<div class="chips"><span class="pill" id="o3a">💪 músculo do rosto <b>contrai</b></span><span class="pill" id="o3b">🧠 o nervo manda o <b>recado</b></span></div>', 1200, [('#o3a', 19.8, 'slide'), ('#o3b', 21.5, 'slide')]),
 ('o4', 24.6, 28.6, '<span class="pill" id="o4a"><b>SNAP-25</b> = um zíper 🤐</span>', 1250, [('#o4a', 24.7, 'slam')]),
 ('o5', 28.6, 35.9, '<div class="chips"><span class="pill" id="o5a">🎭 Argireline <b>imita</b> a peça</span><span class="pill" id="o5b">🦷 dente <b>falso</b> no zíper</span><span class="pill v" id="o5c">📉 recado <b>mais fraco</b></span></div>', 1150, [('#o5a', 28.8, 'slide'), ('#o5b', 31.4, 'slide'), ('#o5c', 34.5, 'slide')]),
 ('o6', 37.1, 43.1, '<span class="pill">📅 2002 · <b>10 mulheres</b> · 30 dias · ao redor dos olhos</span>', 1220, []),
 ('o7', 43.1, 45.8, '<div class="s" style="font-weight:800;font-size:46px">rugas: até</div><div class="big">-<span id="n30">0</span>%</div>', 1120, [('#n30', 43.3, 'count:30'), ('#o7 .big', 43.1, 'slam')]),
 ('o8', 45.8, 50.8, '<span class="pill">🇨🇳 2013 · <b>60 pessoas</b> · contra um creme falso</span>', 1220, []),
 ('o9', 50.8, 55.1, '<div class="chips"><span class="pill" id="o9a">✅ quase <b>metade</b> melhorou</span><span class="pill v" id="o9b">🧪 creme falso: <b>ninguém</b></span></div>', 1200, [('#o9a', 50.9, 'slide'), ('#o9b', 53.4, 'slide')]),
 ('o10', 58.0, 61.3, '<div class="chips"><span class="pill" id="o10a">🩺 toxina: aplicada pelo <b>médico</b></span><span class="pill" id="o10b">⏳ dura <b>meses</b></span></div>', 1200, [('#o10a', 58.1, 'slide'), ('#o10b', 60.3, 'slide')]),
 ('o11', 61.3, 66.9, '<div class="chips"><span class="pill" id="o11a">🧴 Argireline: fica na <b>pele</b></span><span class="pill v" id="o11b">🌊 efeito <b>mais suave</b></span></div>', 1200, [('#o11a', 61.4, 'slide'), ('#o11b', 65.5, 'slide')]),
 ('o12', 67.6, 72.2, '<div class="chips"><span class="pill" id="o12a">🇺🇸 EUA: <b>cosmético</b></span><span class="pill" id="o12b">🇧🇷 Brasil: <b>cosmético</b></span><span class="pill" id="o12c">🇪🇺 Europa: <b>cosmético</b></span></div>', 1130, [('#o12a', 67.7, 'slide'), ('#o12b', 68.7, 'slide'), ('#o12c', 69.3, 'slide')]),
 ('o13', 72.2, 78.0, '<div class="chips"><span class="pill v" id="o13a">FDA: cosmético <b>sem aprovação prévia</b></span><span class="pill" id="o13b">Anvisa: regras de <b>cosméticos</b></span></div>', 1200, [('#o13a', 72.3, 'slide'), ('#o13b', 75.1, 'slide')]),
 ('o14', 80.8, 84.3, '<span class="pill" id="o14a">🏷️ no rótulo: <b>acetyl hexapeptide-8</b></span>', 1240, [('#o14a', 81.4, 'slam')]),
]
stamps = [('st1', 56.8, 58.0, 'MITO ❌', True)]
build_bg(S, STOCK, WD)
build_html(dict(T=T, groups=groups, key=KEY, heads=heads, ovs=ovs, stamps=stamps, scenes=S, punch=[0.9, 44.8],
                cta_at=86.9, cta='Comenta o próximo 👇', serie='PEPTÍDEOS · ARGIRELINE'), f'{WD}/hf/index.html')
print('ok', len(groups))
