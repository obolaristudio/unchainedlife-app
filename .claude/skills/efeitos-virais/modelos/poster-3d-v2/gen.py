import os,shutil,json
V=[
 dict(k='zumbi',accent='#E53935',tag='LONGEVIDADE · CÉLULAS',t1='CÉLULAS',t2='ZUMBI',sub='Elas param de funcionar,<br>mas não morrem.',
      n=25,pre='+',suf='%',nl='de vida média em camundongos<br>quando foram removidas',src='Nature, 2016 · estudo em animais',
      an='Liberam inflamação que envelhece as células vizinhas.'),
 dict(k='sono',accent='#3DB7FF',tag='SONO · CÉREBRO',t1='SEU CÉREBRO',t2='SE LAVA',sub='e isso acontece só<br>enquanto você dorme.',
      n=60,pre='+',suf='%',nl='de espaço para o líquido de limpeza<br>circular durante o sono',src='Science, 2013 · estudo em camundongos',
      an='Um "rio" de líquido leva embora resíduos do dia.'),
 dict(k='glp1',accent='#2ED3B7',tag='PEPTÍDEOS · CÉREBRO',t1='GLP-1',t2='E O DESEJO',sub='o peptídeo do intestino<br>que conversa com o cérebro.',
      n=48,pre='',suf='',nl='adultos num estudo em que a semaglutida<br>reduziu a vontade de beber',src='JAMA Psychiatry, 2025 · estudo pequeno',
      an='O sinal sobe do intestino e acalma o centro de recompensa.'),
]
CSS='''@font-face{font-family:"Bric";src:url("assets/fonts/Bricolage-800.ttf");font-weight:800}
@font-face{font-family:"Bric";src:url("assets/fonts/Bricolage-700.ttf");font-weight:700}
:root{--lime:#CBEF4B;--acc:ACC}
*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1920px;overflow:hidden;background:#000}
#root{position:relative;width:1080px;height:1920px;font-family:"Bric",sans-serif;color:#fff;overflow:hidden}
#bg{position:absolute;left:0;top:0;width:1080px;height:1920px;object-fit:cover}
#shade{position:absolute;inset:0;background:linear-gradient(#000 0%,rgba(0,0,0,.6) 20%,rgba(0,0,0,0) 36%,rgba(0,0,0,0) 66%,rgba(0,0,0,.8) 80%,#000 100%)}
#tag{position:absolute;top:110px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:16px;font-weight:700;font-size:26px;letter-spacing:7px}
#tag .dot{width:16px;height:16px;border-radius:50%;background:var(--lime);box-shadow:0 0 14px var(--lime)}#tag .sep{width:2px;height:26px;background:rgba(255,255,255,.5)}#tag .cat{color:var(--acc)}
.lay{position:absolute;left:0;right:0;text-align:center}
#h1{top:175px}#h1 .a{font-weight:800;font-size:150px;letter-spacing:-5px;line-height:.95;text-shadow:0 0 50px rgba(255,255,255,.25)}
#h1 .b{font-weight:800;font-size:150px;letter-spacing:-5px;line-height:.95;color:var(--acc);text-shadow:0 0 40px var(--acc),0 0 90px var(--acc)}
#sub{top:500px;font-weight:700;font-size:50px;line-height:1.12}
#b2{top:1430px;padding:0 70px}
#num{font-weight:800;font-size:170px;line-height:1;color:var(--acc);text-shadow:0 0 40px var(--acc)}
#nl{font-weight:700;font-size:40px;line-height:1.15;margin-top:6px}
#src{font-weight:700;font-size:24px;letter-spacing:3px;color:rgba(255,255,255,.6);margin-top:12px;text-transform:uppercase}
#an{top:1500px;padding:0 90px;font-weight:700;font-size:44px;line-height:1.15}
#cta{top:1440px}
#cta .p{display:inline-block;background:var(--lime);color:#141414;font-weight:800;font-size:66px;padding:18px 46px;border-radius:60px;box-shadow:0 0 40px rgba(203,239,75,.6)}
#cta .s{font-weight:700;font-size:36px;margin-top:22px}
#foot{top:1785px;font-weight:700;font-size:22px;color:rgba(255,255,255,.55);letter-spacing:2px}'''
def build(v):
    p=v['k']; os.makedirs(p+'/assets/fonts',exist_ok=True)
    for f in ('Bricolage-800.ttf','Bricolage-700.ttf'): shutil.copy(os.path.expanduser('~/.fonts/'+f),p+'/assets/fonts/'+f)
    shutil.copy('../hftest/hyperframes.json',p+'/hyperframes.json')
    html=f'''<!doctype html><html lang="pt-BR"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script><style>{CSS.replace('ACC',v['accent'])}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="14" data-width="1080" data-height="1920">
<video id="bg" class="clip" data-start="0" data-duration="14" src="assets/anim.mp4" muted></video>
<div id="shade" class="clip" data-start="0" data-duration="14"></div>
<div id="tag" class="clip" data-start="0" data-duration="14"><span class="dot"></span>OBOLARI ACADEMY<span class="sep"></span><span class="cat">{v['tag']}</span></div>
<div id="h1" class="clip lay" data-start="0" data-duration="14"><div class="a">{v['t1']}</div><div class="b">{v['t2']}</div></div>
<div id="sub" class="clip lay" data-start="0" data-duration="14">{v['sub']}</div>
<div id="an" class="clip lay" data-start="0" data-duration="14">{v['an']}</div>
<div id="b2" class="clip lay" data-start="0" data-duration="14"><div id="num">{v['pre']}<span id="nv">0</span>{v['suf']}</div><div id="nl">{v['nl']}</div><div id="src">{v['src']}</div></div>
<div id="cta" class="clip lay" data-start="0" data-duration="14"><div class="p">Comenta GUIA 📩</div><div class="s">e entenda tudo na legenda 👇</div></div>
<div id="foot" class="clip lay" data-start="0" data-duration="14">@OBOLARI_ACADEMY · CONTEÚDO EDUCATIVO · NÃO É RECOMENDAÇÃO MÉDICA</div>
</div><script>
const tl=gsap.timeline({{paused:true}});
tl.fromTo("#h1 .a",{{opacity:0,y:-30,scale:1.1}},{{opacity:1,y:0,scale:1,duration:0.45,ease:"power3.out"}},0.05);
tl.fromTo("#h1 .b",{{opacity:0,scale:1.35}},{{opacity:1,scale:1,duration:0.4,ease:"back.out(2)"}},0.35);
tl.fromTo("#tag,#sub",{{opacity:0,y:20}},{{opacity:1,y:0,duration:0.45,stagger:0.12}},0.7);
tl.fromTo("#an",{{opacity:0,y:30}},{{opacity:1,y:0,duration:0.4}},1.3);
tl.to("#an",{{opacity:0,y:-20,duration:0.3}},4.0);
tl.fromTo("#b2",{{opacity:0,y:40}},{{opacity:1,y:0,duration:0.4,ease:"power3.out"}},4.3);
const c={{v:0}};tl.to(c,{{v:{v['n']},duration:1.6,ease:"power2.out",onUpdate:()=>{{document.getElementById("nv").textContent=Math.round(c.v)}}}},4.4);
tl.fromTo("#num",{{scale:1}},{{scale:1.15,duration:0.12,yoyo:true,repeat:1}},6.0);
tl.to("#b2",{{opacity:0,y:-20,duration:0.3}},9.4);
tl.fromTo("#cta",{{opacity:0,scale:0.7}},{{opacity:1,scale:1,duration:0.45,ease:"back.out(2.2)"}},9.7);
tl.to("#cta .p",{{scale:1.06,duration:0.5,yoyo:true,repeat:3,ease:"sine.inOut"}},10.3);
tl.to("#h1,#sub,#cta",{{opacity:0,duration:0.35}},13.5);
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
    open(p+'/index.html','w').write(html)
for v in V: build(v)
print('ok')
