import json,re,html
W=json.load(open('vwords.json')); T=61.5
rep={'Lili':'Lilly','biológico':'biologic','biológico,':'biologic,','biológico.':'biologic.'}
words=[{'w':rep.get(w['w'],w['w']),'s':w['s']} for w in W]
groups=[];cur=[]
for w in words:
    cur.append(w)
    if len(cur)==3 or re.search(r'[,.?!:]$',w['w']): groups.append(cur);cur=[]
if cur: groups.append(cur)
KEY={'reta.','aprovado.','aminoácidos,','40','41','biologic','biologic,','biologic.','FDA','FDA,','aprovado,','vender.','processando','aprovação.','permissão','dela.','consumidor','meio.'}
caps=[];js=[]
for gi,g in enumerate(groups):
    a=g[0]['s']; b=groups[gi+1][0]['s'] if gi+1<len(groups) else T-0.1
    spans=''.join(f'<span class="{"k" if w["w"] in KEY else ""}" id="c{gi}_{j}">{html.escape(w["w"])}</span> ' for j,w in enumerate(g))
    caps.append(f'<div id="cg{gi}" class="clip cap" data-start="{a:.2f}" data-duration="{b-a:.2f}">{spans}</div>')
    for j,w in enumerate(g): js.append(f'tl.fromTo("#c{gi}_{j}",{{opacity:0.25,y:8}},{{opacity:1,y:0,duration:0.12}},{w["s"]:.2f});')
cols=['#E53935','#F4C430','#CBEF4B','#4FC3F7','#B388FF','#FF8A65','#81C784','#F06292','#64B5F6','#FFD54F','#4DB6AC']
beads=''.join(f'<i id="bd{i}" style="background:{cols[i%len(cols)]}"></i>' for i in range(11))
for i in range(11): js.append(f'tl.fromTo("#bd{i}",{{scale:0}},{{scale:1,duration:0.2,ease:"back.out(3)"}},{8.5+i*0.18:.2f});')
beads2=''.join(f'<i class="{"x" if i==6 else ""}" style="background:{cols[i%len(cols)]}"></i>' for i in range(11))
def hd(id,a,b,inner): return f'<div id="{id}" class="clip hd" data-start="{a}" data-duration="{round(b-a,2)}">{inner}</div>'
H=f'''<!doctype html><html lang="pt-BR"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script><style>
@font-face{{font-family:"Bric";src:url("assets/fonts/Bricolage-800.ttf");font-weight:800}}
@font-face{{font-family:"Bric";src:url("assets/fonts/Bricolage-700.ttf");font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}html,body{{width:1080px;height:1920px;overflow:hidden;background:#0E0E0E}}
#root{{position:relative;width:1080px;height:1920px;font-family:"Bric",sans-serif;color:#fff;overflow:hidden}}
#bg{{position:absolute;inset:0;width:1080px;height:1920px;object-fit:cover;z-index:1}}
#shade{{position:absolute;left:0;top:420px;width:1080px;height:1100px;z-index:2;background:linear-gradient(rgba(0,0,0,0) 55%,rgba(0,0,0,.6) 100%)}}
#frame{{position:absolute;inset:26px;z-index:9;border:4px solid #CBEF4B;border-radius:34px;box-shadow:0 0 0 40px #0E0E0E}}
#tag{{position:absolute;z-index:9;top:80px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:16px;font-weight:700;font-size:26px;letter-spacing:8px}}
#tag .d{{width:18px;height:18px;border-radius:50%;background:#CBEF4B;box-shadow:0 0 14px #CBEF4B}}#tag .c{{color:#CBEF4B}}
.hd{{position:absolute;z-index:6;left:40px;right:40px;top:150px;height:260px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}}
.hd .s{{font-weight:700;font-size:42px;color:#F2EFE6}}
.hd .m{{font-weight:800;font-size:84px;line-height:1;letter-spacing:-2px}}
.hd .m span,.hd .s span{{color:#CBEF4B}} .r{{color:#E53935!important}}
.cap{{position:absolute;z-index:6;left:60px;right:60px;top:1555px;text-align:center;font-weight:800;font-size:60px;line-height:1.1;letter-spacing:-1px;text-shadow:0 4px 18px rgba(0,0,0,.8)}}
.cap .k{{color:#CBEF4B}}
.ov{{position:absolute;z-index:5;left:60px;right:60px;top:1180px;text-align:center}}
.pill{{display:inline-block;background:rgba(14,14,14,.86);border:3px solid #CBEF4B;font-weight:800;font-size:40px;padding:12px 26px;border-radius:16px}}
.pill.red{{border-color:#E53935;color:#fff}} .pill b{{color:#CBEF4B}} .pill.red b{{color:#E53935}}
.beads{{display:flex;justify-content:center;gap:12px;background:rgba(14,14,14,.8);padding:22px;border-radius:24px}}
.beads i{{display:block;width:58px;height:58px;border-radius:50%;box-shadow:inset -6px -6px 0 rgba(0,0,0,.18)}}
.beads i.x{{opacity:.25;outline:5px solid #E53935;outline-offset:3px}}
.cards{{display:flex;gap:22px;justify-content:center}}
.card{{flex:1;background:rgba(14,14,14,.88);border-radius:22px;padding:22px;text-align:left;border:3px solid #B388FF}}
.card.g{{border-color:#4DB6AC}} .card .t{{font-weight:800;font-size:28px;letter-spacing:3px;color:#B388FF}} .card.g .t{{color:#4DB6AC}}
.card .n{{font-weight:800;font-size:56px;line-height:1.05;margin:6px 0}} .card .d{{font-weight:700;font-size:28px;color:rgba(255,255,255,.85)}}
.count{{display:flex;justify-content:center;gap:60px}}
.cnt{{background:rgba(14,14,14,.88);border-radius:22px;padding:18px 40px;text-align:center;min-width:330px}}
.cnt .who{{font-weight:800;font-size:34px;letter-spacing:3px}} .cnt .num{{font-weight:800;font-size:150px;line-height:1}} .cnt .d{{font-weight:700;font-size:26px;color:rgba(255,255,255,.8)}}
.stamp span{{display:inline-block;border:8px solid #E53935;color:#E53935;background:rgba(14,14,14,.85);font-weight:800;font-size:76px;padding:6px 30px;border-radius:18px;transform:rotate(-5deg);line-height:1.05}}
.trio{{display:flex;justify-content:space-around;align-items:flex-end;background:rgba(14,14,14,.85);border-radius:22px;padding:20px}}
.trio div{{font-weight:800;font-size:40px}} .trio .cons{{color:#FFB74D;font-size:52px}}
#flash{{position:absolute;inset:0;z-index:8;background:#fff;opacity:0}}
#end{{position:absolute;z-index:7;left:60px;right:60px;top:1150px;text-align:center;background:rgba(14,14,14,.9);border-radius:22px;padding:24px;font-weight:700;font-size:28px;line-height:1.35;color:rgba(255,255,255,.9)}}
#end b{{color:#CBEF4B}}
#foot{{position:absolute;z-index:9;top:1800px;left:0;right:0;text-align:center;font-weight:700;font-size:20px;letter-spacing:2px;color:rgba(255,255,255,.75)}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{T}" data-width="1080" data-height="1920">
<video id="bg" class="clip" data-start="0" data-duration="{T}" src="assets/bg.mp4" muted></video>
<div id="shade" class="clip" data-start="0" data-duration="{T}"></div>
{hd('h0',0,2.0,'<div class="m">A disputa para<br>liberar a <span>reta</span></div><div class="s">Lilly × FDA</div>')}
{hd('h1',2.0,7.7,'<div class="m"><span>RETA</span></div><div class="s">remédio novo para emagrecer</div>')}
<div id="o1" class="clip ov" data-start="5.9" data-duration="1.8"><span class="pill red"><b>EM TESTE</b> · ainda não aprovado</span></div>
{hd('h2',7.7,12.9,'<div class="m">Correntinha de<br><span>aminoácidos</span></div>')}
<div id="o2" class="clip ov" data-start="8.3" data-duration="4.6"><div class="beads">{beads}</div></div>
{hd('h3',12.9,26.8,'<div class="m">A lei das <span>contas</span></div>')}
<div id="o3" class="clip ov" data-start="14.8" data-duration="12.0"><div class="cards"><div class="card"><div class="t">&gt; 40 CONTAS</div><div class="n">Biologic</div><div class="d">remédio especial<br>só a Lilly pode fazer</div></div><div class="card g" id="cg2"><div class="t">≤ 40 CONTAS</div><div class="n">Comum</div><div class="d">depois de aprovado,<br>outras podem copiar</div></div></div></div>
{hd('h4',26.8,40.2,'<div class="m">Quem conta<br>as <span>contas</span>?</div>')}
<div id="o4" class="clip ov" data-start="27.2" data-duration="10.2"><div class="count"><div class="cnt" id="cl"><div class="who" style="color:#B388FF">LILLY</div><div class="num" style="color:#B388FF">41</div><div class="d">"é biologic, é meu"</div></div><div class="cnt" id="cf"><div class="who" style="color:#4DB6AC">FDA</div><div class="num" style="color:#4DB6AC">40</div><div class="d">"uma não conta"</div></div></div></div>
<div id="o5" class="clip ov" data-start="37.4" data-duration="2.8"><div class="beads">{beads2}</div><div style="margin-top:14px"><span class="pill"><b>FDA:</b> não é biologic</span></div></div>
<div id="o6" class="clip ov stamp" data-start="40.4" data-duration="3.9"><span>SEM APROVAÇÃO<br><small style="font-size:40px">ninguém fabrica nem vende</small></span></div>
{hd('h5',44.3,53.7,'<div class="m">Processo nas<br><span>lojas online</span></div>')}
<div id="o7" class="clip ov" data-start="45.2" data-duration="8.5"><span class="pill red"><b>AÇÃO JUDICIAL</b> · remédio sem aprovação</span></div>
{hd('h6',53.7,T,'<div class="m">Quem controla<br>o <span>remédio</span>?</div>')}
<div id="o8" class="clip ov" data-start="54.0" data-duration="5.3"><div class="trio"><div style="color:#B388FF">LILLY</div><div class="cons">CONSUMIDOR</div><div style="color:#4DB6AC">FDA</div></div></div>
<div id="end" class="clip" data-start="59.3" data-duration="{round(T-59.3,2)}">Retatrutida: em fase 3 de testes, <b>sem aprovação</b> da FDA ou da Anvisa.<br>Fonte: processo Eli Lilly × FDA (7º Circuito, EUA, 2026).<br><b>Conteúdo educativo: não é recomendação médica nem sugestão de uso.</b></div>
{chr(10).join(caps)}
<div id="flash" class="clip" data-start="0" data-duration="{T}"></div>
<div id="frame" class="clip" data-start="0" data-duration="{T}"></div>
<div id="tag" class="clip" data-start="0" data-duration="{T}"><span class="d"></span>OBOLARI ACADEMY<span class="c">· NOTÍCIA</span></div>
<div id="foot" class="clip" data-start="0" data-duration="{T}">@OBOLARI_ACADEMY · CONTEÚDO EDUCATIVO · NÃO É RECOMENDAÇÃO MÉDICA</div>
</div><script>
const tl=gsap.timeline({{paused:true}});
tl.set("#flash",{{opacity:0}},0);
tl.fromTo("#h0 .m",{{scale:1.6,opacity:0}},{{scale:1,opacity:1,duration:0.35,ease:"power4.out"}},0.05);
'''
for h,t in [('#h1',2.0),('#h2',7.7),('#h3',12.9),('#h4',26.8),('#h5',44.3),('#h6',53.7)]:
    H+=f'tl.fromTo("{h}",{{y:30,opacity:0}},{{y:0,opacity:1,duration:0.3,ease:"power3.out"}},{t});\n'
S=json.load(open('scenes.json'))
for s in S[1:]: H+=f'tl.fromTo("#flash",{{opacity:0.3}},{{opacity:0,duration:0.18}},{s[0]});\n'
for o,t in [('#o1',5.9),('#o2',8.3),('#o5',37.4),('#o7',45.2),('#o8',54.0),('#end',59.3)]:
    H+=f'tl.fromTo("{o}",{{opacity:0,y:20}},{{opacity:1,y:0,duration:0.3}},{t});\n'
H+='''tl.fromTo("#o3 .card",{opacity:0,y:30},{opacity:1,y:0,duration:0.35},14.8);
tl.fromTo("#cg2",{opacity:0,y:30},{opacity:1,y:0,duration:0.35},20.6);
tl.fromTo("#cl",{opacity:0,scale:0.6},{opacity:1,scale:1,duration:0.35,ease:"back.out(2)"},27.3);
tl.fromTo("#cf",{opacity:0,scale:0.6},{opacity:1,scale:1,duration:0.35,ease:"back.out(2)"},32.3);
tl.fromTo("#o6 span",{scale:2.4,opacity:0},{scale:1,opacity:1,duration:0.25,ease:"power3.in"},40.4);
'''+'\n'.join(js)+'''
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
open('hf/index.html','w').write(H);print('ok',len(groups))
