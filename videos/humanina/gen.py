# Reel Humanina — uso: python3 gen.py <pasta_de_trabalho> <pasta_stock>
import sys, json; sys.path.insert(0, '/home/user/unchainedlife-app/videos')
from lib_reel import build_bg, build_html, caption_groups, beads
WD, STOCK = sys.argv[1], sys.argv[2]
S = json.load(open('/home/user/unchainedlife-app/videos/humanina/scenes.json'))
W = json.load(open(f'{WD}/vwords.json')); T = 87.3
rep = {'MOTSC,': 'MOTS-c,', 'Pomenta': 'Comenta', 'seguem': 'segue', 'o': 'o', 'age,': 'age?', 'pessoas,': 'pessoas?'}
groups = caption_groups(W, rep, merges=[('guarda', '-costas', 'guarda-costas'), ('estudo.', '', 'estudo.')])
# corrige transcrição: "Os Estados Unidos e no Brasil, ela seguem o estudo." -> fala real: "Nos Estados Unidos e no Brasil, ela segue em estudo."
for g in groups:
    for w in g:
        if w['w'] == 'Os' and w['s'] > 71: w['w'] = 'Nos'
        if w['w'] == 'o' and 73.5 < w['s'] < 74: w['w'] = 'em'
        if w['w'] == 'a' and 68.5 < w['s'] < 68.8: w['w'] = '·'
        if w['w'] == 'e' and 45.4 < w['s'] < 45.6: w['w'] = 'que'
        if w['w'] == 'em' and 39.9 < w['s'] < 40.1: w['w'] = 'num'
for g in groups:
    g[:] = [w for w in g if w['w'] not in ('·', 'um') or not (40.1 < w['s'] < 40.3 or w['w'] == '·')]
groups = [g for g in groups if g]
KEY = {'cérebro', 'alzheimer', '100', 'humanina', 'humanina.', '2001', 'japoneses', 'neurônios', 'genes', 'trás', 'menos',
       '24', 'surpresa', 'dna', 'mitocôndria', 'usina', 'energia', 'mensagens', 'guarda-costas', 'estresse', 'receptores',
       'fechaduras', 'proteção', 'camundongos', 'memória', '2020', 'centenários', 'sangue', 'poucos', 'pequenos', 'nenhum',
       'país', 'mots-c', 'próximo'}
heads = [
 ('h0', 0, 6.6, '<div class="s">Descoberto no cérebro de um paciente com <span>Alzheimer</span>…</div><div class="m">e ligado a quem chega aos <span>100</span>? 🎂</div>'),
 ('h1', 6.6, 13.1, '<div class="m"><span>Humanina</span> 🧬</div><div class="s">um peptídeo da mitocôndria</div>'),
 ('h2', 13.1, 27.0, '<div class="m">A <span>descoberta</span> 🔎</div><div class="s">Japão, 2001</div>'),
 ('h3', 27.0, 38.9, '<div class="m">A <span>surpresa</span> ⚡</div>'),
 ('h4', 38.9, 48.8, '<div class="m">Como ela <span>age</span>? 🛡️</div>'),
 ('h5', 48.8, 67.0, '<div class="m">O que os <span>estudos</span><br>mostraram 🔬</div>'),
 ('h6', 67.0, 74.3, '<div class="m">Status pelo <span>mundo</span> 🌎</div>'),
 ('h7', 74.3, 81.2, '<div class="m"><span>Curiosidade</span> 👀</div>'),
 ('h8', 81.2, T, '<div class="m">Qual é o <span>próximo</span>? 💬</div>'),
]
ovs = [
 ('o1', 8.4, 13.1, '<div class="chips"><span class="pill" id="o1a">🇯🇵 cientistas <b>japoneses</b> · 2001</span><span class="pill" id="o1b">🧠 meta: proteger os <b>neurônios</b></span></div>', 1200, [('#o1a', 9.4, 'slide'), ('#o1b', 11.6, 'slide')]),
 ('o2', 13.1, 19.8, '<div class="chips"><span class="pill" id="o2a">🧬 vasculharam os <b>genes</b></span><span class="pill v" id="o2b">📍 região que a doença <b>atinge menos</b></span></div>', 1200, [('#o2a', 13.3, 'slide'), ('#o2b', 17.4, 'slide')]),
 ('o3', 19.8, 27.0, beads(24) + '<div style="margin-top:14px"><span class="pill"><b><span id="n24">0</span></b> aminoácidos</span></div>', 1060, [('24', 21.4, 'beads'), ('#n24', 21.4, 'count:24')]),
 ('o4', 28.1, 34.0, '<div class="chips"><span class="pill" id="o4a">📜 receita no <b>DNA da mitocôndria</b></span><span class="pill" id="o4b">🏭 mitocôndria = <b>usina</b> da célula</span></div>', 1200, [('#o4a', 30.4, 'slam'), ('#o4b', 32.4, 'slide')]),
 ('o5', 34.0, 38.9, '<div class="chips"><span class="pill" id="o5a">⚡ fabrica <b>energia</b></span><span class="pill" id="o5b">📨 e manda <b>mensagens</b></span></div>', 1200, [('#o5a', 35.8, 'slide'), ('#o5b', 37.5, 'slide')]),
 ('o6', 39.9, 44.6, '<span class="pill" id="o6a">🛡️ um <b>guarda-costas</b> da célula</span>', 1240, [('#o6a', 40.3, 'slam')]),
 ('o7', 44.6, 48.8, '<div class="chips"><span class="pill" id="o7a">🔐 receptor = <b>fechadura</b></span><span class="pill" id="o7b">✅ liga sinais de <b>proteção</b></span></div>', 1200, [('#o7a', 44.8, 'slide'), ('#o7b', 47.6, 'slide')]),
 ('o8', 50.3, 55.1, '<span class="pill" id="o8a">🐭 camundongos: <b>memória protegida</b></span>', 1240, [('#o8a', 53.9, 'slide')]),
 ('o9', 56.2, 60.8, '<span class="pill">👴 2020 · <b>filhos de centenários</b> vs. mesma idade</span>', 1220, []),
 ('o10', 60.8, 63.8, '<span class="pill" id="o10a">🩸 <b>mais humanina</b> no sangue</span>', 1240, [('#o10a', 62.3, 'slam')]),
 ('o11', 67.6, 74.3, '<div class="chips"><span class="pill v" id="o11a">🌍 aprovação como remédio: <b>nenhum país</b></span><span class="pill" id="o11b">🇺🇸 🇧🇷 em <b>estudo</b></span></div>', 1200, [('#o11a', 68.3, 'slide'), ('#o11b', 71.7, 'slide')]),
 ('o12', 75.4, 81.2, '<span class="pill" id="o12a">👯 prima do <b>MOTS-c</b> · as duas nascem na mitocôndria</span>', 1240, [('#o12a', 78.2, 'slam')]),
]
stamps = [('st1', 27.0, 28.1, 'ESPERA…', False)]
build_bg(S, STOCK, WD)
build_html(dict(T=T, groups=groups, key=KEY, heads=heads, ovs=ovs, stamps=stamps, scenes=S, punch=[2.7, 5.9, 31.3],
                cta_at=84.1, cta='Comenta o próximo 👇', serie='PEPTÍDEOS · HUMANINA'), f'{WD}/hf/index.html')
print('ok', len(groups))
