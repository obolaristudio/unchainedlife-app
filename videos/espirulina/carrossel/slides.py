# Carrossel espirulina no estilo editorial verde-escuro (referência visual @soverde.pt), texto original da Obolari.
import base64,pathlib
F=pathlib.Path('../hf/assets/fonts').resolve()
def b64(p): return base64.b64encode(open(p,'rb').read()).decode()
S=[
 (1,None,'Esse pó vem de um dos <b>seres vivos mais antigos da Terra</b>. Deixa a água <b>azul</b>, tem <b>mais da metade do peso em proteína</b> e a <b>NASA</b> estudou como comida para o espaço.'),
 (2,'O que <b>é</b>?','A espirulina <b>não é uma planta</b>. É uma <b>cianobactéria</b>: um micro-organismo em forma de <b>espiral</b> que faz fotossíntese, como as plantas.'),
 (3,None,'As cianobactérias existem há <b>mais de 3 bilhões de anos</b>. Foram elas que ajudaram a encher a atmosfera da Terra de <b>oxigênio</b>.'),
 (4,None,'O azul vem de um pigmento chamado <b>ficocianina</b>. É ele que pinta a água e muitos <b>doces azuis "naturais"</b>.'),
 (5,'A <b>proteína</b>','Mais da <b>metade do peso seco</b> da espirulina é proteína, com <b>todos os aminoácidos essenciais</b>. Mas uma porção tem poucos gramas: ela <b>não substitui</b> o prato.'),
 (6,None,'A <b>NASA</b> estudou a espirulina como comida para <b>missões longas no espaço</b>: ela cresce rápido e ainda <b>produz oxigênio</b>.'),
 (7,'E em <b>pessoas</b>?','Estudos pequenos mostraram <b>leve queda no colesterol e na pressão</b>. Já os estudos de <b>câncer</b> com a ficocianina são de <b>laboratório e em animais</b>.'),
 (8,'A <b>surpresa</b> 🤔','Muita gente acha que a espirulina é fonte de <b>vitamina B12</b>. Mas a maior parte é uma <b>pseudovitamina</b>: uma B12 "falsa", que o corpo <b>não consegue usar</b>.'),
 (9,'<b>Resumindo</b>','Antiga, rica em proteína, <b>mas não é fonte de B12</b>.'),
]
CSS=f'''@font-face{{font-family:B;src:url(data:font/ttf;base64,{b64(F/"Bricolage-700.ttf")});font-weight:700}}
@font-face{{font-family:B;src:url(data:font/ttf;base64,{b64(F/"Bricolage-800.ttf")});font-weight:800}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;background:#1D3324;font-family:B,sans-serif;color:#fff;overflow:hidden;position:relative}}
.img{{position:absolute;left:0;top:0;width:1080px;height:860px;object-fit:cover}}
.fade{{position:absolute;left:0;top:560px;width:1080px;height:310px;background:linear-gradient(rgba(29,51,36,0),#1D3324)}}
.bar{{position:absolute;left:0;top:0;width:1080px;height:130px;background:rgba(18,32,22,.78);display:flex;align-items:center;justify-content:center;font-weight:800;font-size:44px;letter-spacing:-.5px}}
.bar i{{display:inline-block;width:16px;height:16px;border-radius:50%;background:#CBEF4B;margin-right:14px;box-shadow:0 0 12px #CBEF4B}}
.n{{position:absolute;right:40px;top:38px;background:rgba(0,0,0,.35);border-radius:30px;padding:8px 20px;font-weight:700;font-size:34px}}
.txt{{position:absolute;left:70px;right:70px;bottom:110px;text-align:center}}
h2{{font-weight:800;font-size:76px;margin-bottom:30px;letter-spacing:-1px}} p{{font-weight:700;font-size:50px;line-height:1.28;letter-spacing:-.5px}}
b{{color:#CBEF4B;font-weight:800}}
.foot{{position:absolute;left:0;right:0;bottom:36px;text-align:center;font-weight:700;font-size:22px;letter-spacing:2px;color:rgba(255,255,255,.55)}}
.cta{{display:inline-block;margin-top:40px;background:#CBEF4B;color:#141414;font-weight:800;font-size:52px;padding:16px 40px;border-radius:60px}}
.src{{margin-top:34px;font-weight:700;font-size:24px;line-height:1.4;color:rgba(255,255,255,.65)}}'''
for n,t,p in S:
    extra=''
    if n==9: extra='<div class="cta">Você já provou? Comenta aqui 💬</div><div class="src">Fontes: Watanabe et al., J Agric Food Chem 1999 · Serban et al., Clin Nutr 2016 · Machowiec et al., Nutrients 2021 · Braune et al., Life 2021</div>'
    h=f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><img class="img" src="data:image/png;base64,{b64(f"../ia/img{n}.png")}"><div class="fade"></div><div class="bar"><i></i>obolari_academy</div><div class="n">{n}/9</div><div class="txt">{f"<h2>{t}</h2>" if t else ""}<p>{p}</p>{extra}</div><div class="foot">CONTEÚDO EDUCATIVO · NÃO É RECOMENDAÇÃO MÉDICA NEM SUGESTÃO DE USO</div></body></html>'
    open(f's{n}.html','w').write(h)
print('ok')
