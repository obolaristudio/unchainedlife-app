import math
T=41.0
# (id, text lines, start, end, pill left/top, align, target x,y)
L=[('c',['PAU DE CANELA'],4.2,9.2,60,1680,'l',(430,1520)),
   ('s',['SEMENTES','DE ROMÃ'],9.6,15.2,640,1440,'l',(830,1330)),
   ('m',['FOLHAS','DE MENTA'],15.6,21.6,560,1470,'l',(420,1300)),
   ('t',['CHÁ DA CASCA','DE ROMÃ'],22.2,31.0,50,1500,'l',(470,1420))]
els=[];js=[]
for k,lines,a,b,px,py,al,(tx,ty) in L:
    d=round(b-a,2)
    txt='<br>'.join(lines)
    els.append(f'<div id="p{k}" class="clip pill" data-start="{a}" data-duration="{d}" style="left:{px}px;top:{py}px">{txt}</div>')
    # line from pill anchor (top-left corner area) to target
    ax,ay=px+40,py  # anchor on pill top edge
    if k=='m': ax,ay=px,py+40
    dx,dy=tx-ax,ty-ay; ln=math.hypot(dx,dy); ang=math.degrees(math.atan2(dy,dx))
    els.append(f'<div id="l{k}" class="clip ln" data-start="{a}" data-duration="{d}" style="left:{ax}px;top:{ay-2}px;width:{ln:.0f}px;transform:rotate({ang:.1f}deg)"></div>')
    els.append(f'<div id="d{k}" class="clip dot" data-start="{a}" data-duration="{d}" style="left:{tx-14}px;top:{ty-14}px"></div>')
    js+= [f'tl.fromTo("#d{k}",{{scale:0}},{{scale:1,duration:0.3,ease:"back.out(3)"}},{a});',
          f'tl.fromTo("#l{k}",{{scaleX:0}},{{scaleX:1,duration:0.35,ease:"power2.out"}},{a+0.1});',
          f'tl.fromTo("#p{k}",{{opacity:0,y:20}},{{opacity:1,y:0,duration:0.35,ease:"power3.out"}},{a+0.3});',
          f'tl.to("#p{k},#l{k},#d{k}",{{opacity:0,duration:0.3}},{b-0.3:.2f});']
html=f'''<!doctype html><html lang="pt-BR"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script><style>
@font-face{{font-family:"Bric";src:url("assets/fonts/Bricolage-800.ttf");font-weight:800}}
@font-face{{font-family:"Bric";src:url("assets/fonts/Bricolage-700.ttf");font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}html,body{{width:1080px;height:1920px;overflow:hidden;background:#0E0E0E}}
#root{{position:relative;width:1080px;height:1920px;font-family:"Bric",sans-serif;color:#fff;overflow:hidden}}
#v{{position:absolute;left:0;top:0;width:1080px;height:1920px;object-fit:cover;z-index:1}}
.pill{{position:absolute;z-index:5;background:#CBEF4B;color:#141414;font-weight:800;font-size:46px;line-height:1.05;letter-spacing:-.5px;padding:14px 26px;border-radius:18px;box-shadow:0 8px 28px rgba(0,0,0,.45);white-space:nowrap}}
.ln{{position:absolute;z-index:4;height:4px;background:#F7F4EC;transform-origin:0 50%;box-shadow:0 0 8px rgba(0,0,0,.5)}}
.dot{{position:absolute;z-index:4;width:28px;height:28px;border-radius:50%;background:#CBEF4B;border:4px solid #F7F4EC;box-shadow:0 0 14px rgba(0,0,0,.5)}}
#shade{{position:absolute;inset:0;z-index:2;background:linear-gradient(rgba(0,0,0,.45) 0%,rgba(0,0,0,0) 15%,rgba(0,0,0,0) 85%,rgba(0,0,0,.45) 100%)}}
#frame{{position:absolute;inset:26px;z-index:7;border:4px solid #CBEF4B;border-radius:34px;box-shadow:0 0 0 40px #0E0E0E}}
#tag{{position:absolute;z-index:8;top:80px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:16px;font-weight:700;font-size:26px;letter-spacing:8px}}
#tag .dot2{{width:18px;height:18px;border-radius:50%;background:#CBEF4B;box-shadow:0 0 14px #CBEF4B}}#tag .c{{color:#CBEF4B}}
#hook{{position:absolute;z-index:5;left:60px;right:60px;top:200px;text-align:center}}
#hook .a{{font-weight:800;font-size:104px;line-height:.98;letter-spacing:-3px;text-shadow:0 8px 30px rgba(0,0,0,.75)}}
#hook .a span{{color:#CBEF4B}}
#hook .b{{font-weight:700;font-size:44px;margin-top:20px;text-shadow:0 4px 20px rgba(0,0,0,.8)}}
#end{{position:absolute;z-index:5;left:60px;right:60px;top:200px;text-align:center}}
#end .a{{font-weight:800;font-size:92px;line-height:1;letter-spacing:-2px;text-shadow:0 8px 30px rgba(0,0,0,.75)}}
#end .p{{display:inline-block;margin-top:28px;background:#CBEF4B;color:#141414;font-weight:800;font-size:62px;padding:16px 44px;border-radius:60px;box-shadow:0 0 40px rgba(203,239,75,.55)}}
#foot{{position:absolute;z-index:8;top:1800px;left:0;right:0;text-align:center;font-weight:700;font-size:20px;letter-spacing:2px;color:rgba(255,255,255,.75)}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{T}" data-width="1080" data-height="1920">
<video id="v" class="clip" data-start="0" data-duration="{T}" src="assets/orig.mp4" muted></video>
<div id="shade" class="clip" data-start="0" data-duration="{T}"></div>
{chr(10).join(els)}
<div id="hook" class="clip" data-start="0" data-duration="3.8"><div class="a">Você joga fora<br>a <span>melhor parte</span><br>da romã?</div><div class="b">O chá da casca 👇</div></div>
<div id="end" class="clip" data-start="34.8" data-duration="6.2"><div class="a">Salva essa<br>receita 💾</div><div class="p">Comenta GUIA 📩</div></div>
<div id="frame" class="clip" data-start="0" data-duration="{T}"></div>
<div id="tag" class="clip" data-start="0" data-duration="{T}"><span class="dot2"></span>OBOLARI ACADEMY<span class="c">· BEM-ESTAR</span></div>
<div id="foot" class="clip" data-start="0" data-duration="{T}">@OBOLARI_ACADEMY · CONTEÚDO EDUCATIVO · NÃO É RECOMENDAÇÃO MÉDICA</div>
</div><script>
const tl=gsap.timeline({{paused:true}});
tl.fromTo("#hook .a",{{y:30,opacity:0}},{{y:0,opacity:1,duration:0.4,ease:"power3.out"}},0.1);
tl.fromTo("#hook .b",{{opacity:0}},{{opacity:1,duration:0.3}},0.6);
tl.to("#hook",{{opacity:0,duration:0.3}},3.5);
tl.fromTo("#end .a",{{y:30,opacity:0}},{{y:0,opacity:1,duration:0.4,ease:"power3.out"}},35.0);
tl.fromTo("#end .p",{{scale:0.7,opacity:0}},{{scale:1,opacity:1,duration:0.4,ease:"back.out(2)"}},35.6);
tl.to("#end .p",{{scale:1.06,duration:0.5,yoyo:true,repeat:5,ease:"sine.inOut"}},36.2);
{chr(10).join(js)}
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
open('hf2/index.html','w').write(html)
