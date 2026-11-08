import json
P=json.load(open('plan.json')); TOP=790; T=round(P[-1]['start']+P[-1]['dur'],3)
N={'canela':('01 · PAU DE','','CANELA',190),'sementes':('02 · SEMENTES DE','','ROMÃ',190),'menta':('03 · FOLHAS DE','','MENTA',250),'cha':('04 · O CHÁ DA','','CASCA DE ROMÃ',190)}
from PIL import ImageFont
def width(t,sz):
    fnt=ImageFont.truetype('hf/assets/fonts/Bricolage-800.ttf',sz); return fnt.getlength(t)+(len(t)-1)*(-0.035*sz)
v=[];names=[];js=[]
for p in P:
    i,k,s,d=p['i'],p['k'],p['start'],p['dur']
    v.append(f'<video id="v{i}" class="clip bg" data-start="{s}" data-duration="{d}" src="assets/{p["file"]}" muted></video>')
    sel=f'#v{i}'
    if k in N:
        n,l1,l2,sz=N[k]; sz=int(min(260,960/(width(l2,100)/100))); w=width(l2,sz); x0=round((1080-w)/2+45); x1=x0-90
        v.append(f'<video id="f{i}" class="clip fg" data-start="{s}" data-duration="{d}" src="assets/{p["file"][:-4]}_fg.webm" muted></video>')
        big=f' style="font-size:{sz}px"'
        names.append(f'<div id="n{i}" class="clip nm" data-start="{s}" data-duration="{d}">'+(f'<div class="l1">{l1}</div>' if l1 else '')+f'<div class="l2"{big}>{l2}</div></div>')
        names.append(f'<div id="p{i}" class="clip pill" data-start="{s}" data-duration="{d}"><span>{n}</span></div>')
        sel=f'#v{i},#f{i}'
        # name: whip in from right, drift, whip out left
        js.append(f'tl.fromTo("#n{i}",{{x:1100,opacity:0,filter:"blur(18px)"}},{{x:{x0},opacity:1,filter:"blur(0px)",duration:0.45,ease:"power4.out"}},{s+0.15});')
        js.append(f'tl.to("#n{i}",{{x:{x1:.0f},duration:{d-0.95:.3f},ease:"none"}},{s+0.6});')
        js.append(f'tl.to("#n{i}",{{x:{x1-700:.0f},opacity:0,filter:"blur(18px)",duration:0.3,ease:"power3.in"}},{s+d-0.35:.3f});')
        js.append(f'tl.fromTo("#p{i}",{{scale:0,opacity:0}},{{scale:1,opacity:1,duration:0.35,ease:"back.out(2.5)"}},{s+0.35});')
        js.append(f'tl.to("#p{i}",{{opacity:0,duration:0.2}},{s+d-0.3:.3f});')
        js.append(f'tl.fromTo("{sel}",{{scale:1.0}},{{scale:1.07,duration:{d},ease:"none"}},{s});')
    else:
        js.append(f'tl.fromTo("{sel}",{{scale:1.08}},{{scale:1.0,duration:{d},ease:"none"}},{s});')
    # zoom-through transitions
    if i>0:
        js.append(f'tl.fromTo("{sel}",{{filter:"blur(14px) brightness(1.4)"}},{{filter:"blur(0px) brightness(1)",duration:0.3,ease:"power2.out"}},{s});')
        js.append(f'tl.fromTo("#flash",{{opacity:0.75}},{{opacity:0,duration:0.28,ease:"power2.out"}},{s});')
    if i<len(P)-1:
        js.append(f'tl.to("{sel}",{{filter:"blur(14px) brightness(1.4)",duration:0.22,ease:"power2.in"}},{s+d-0.22:.3f});')
html=f'''<!doctype html><html lang="pt-BR"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script><style>
@font-face{{font-family:"Bric";src:url("assets/fonts/Bricolage-800.ttf");font-weight:800}}
@font-face{{font-family:"Bric";src:url("assets/fonts/Bricolage-700.ttf");font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}html,body{{width:1080px;height:1920px;overflow:hidden;background:#0E0E0E}}
#root{{position:relative;width:1080px;height:1920px;font-family:"Bric",sans-serif;color:#fff;overflow:hidden}}
.bg,.fg{{position:absolute;left:0;top:0;width:1080px;height:1920px;object-fit:cover;transform-origin:50% 55%}}
.bg{{z-index:1}}.nm{{z-index:2}}.fg{{z-index:3}}
.nm{{position:absolute;left:0;top:{TOP}px;line-height:1;white-space:nowrap;width:max-content}}
.nm .l1{{font-weight:800;font-size:120px;letter-spacing:-3px;color:#CBEF4B;text-shadow:0 8px 30px rgba(0,0,0,.35)}}
.nm .l2{{font-weight:800;letter-spacing:-0.035em;color:#F7F4EC;text-shadow:0 10px 40px rgba(0,0,0,.4)}}
.pill{{position:absolute;z-index:5;left:0;right:0;top:640px;text-align:center}}
.pill span{{display:inline-block;font-weight:800;font-size:32px;letter-spacing:6px;color:#141414;background:#CBEF4B;padding:8px 22px;border-radius:12px}}
#flash{{position:absolute;inset:0;z-index:6;background:#FFF6E8;opacity:0}}
#vig{{position:absolute;inset:0;z-index:4;background:radial-gradient(ellipse at 50% 50%,rgba(0,0,0,0) 55%,rgba(0,0,0,.35) 100%),linear-gradient(rgba(0,0,0,.45) 0%,rgba(0,0,0,0) 16%,rgba(0,0,0,0) 82%,rgba(0,0,0,.5) 100%)}}
#frame{{position:absolute;inset:26px;z-index:7;border:4px solid #CBEF4B;border-radius:34px;box-shadow:0 0 0 40px #0E0E0E}}
#tag{{position:absolute;z-index:8;top:80px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:16px;font-weight:700;font-size:26px;letter-spacing:8px}}
#tag .dot{{width:18px;height:18px;border-radius:50%;background:#CBEF4B;box-shadow:0 0 14px #CBEF4B}}#tag .c{{color:#CBEF4B}}
#hook{{position:absolute;z-index:5;left:60px;right:60px;top:230px;text-align:center}}
#hook .a{{font-weight:800;font-size:112px;line-height:.98;letter-spacing:-3px;text-shadow:0 8px 30px rgba(0,0,0,.7)}}
#hook .a span{{color:#CBEF4B}}
#hook .b{{font-weight:700;font-size:44px;margin-top:20px;text-shadow:0 4px 20px rgba(0,0,0,.8)}}
#mid{{position:absolute;z-index:5;left:60px;right:60px;top:240px;text-align:center;font-weight:800;font-size:80px;line-height:1;letter-spacing:-2px;text-shadow:0 8px 30px rgba(0,0,0,.7)}}
#mid span{{color:#CBEF4B}}
#end{{position:absolute;z-index:5;left:60px;right:60px;top:230px;text-align:center}}
#end .a{{font-weight:800;font-size:96px;line-height:1;letter-spacing:-2px;text-shadow:0 8px 30px rgba(0,0,0,.7)}}
#end .p{{display:inline-block;margin-top:30px;background:#CBEF4B;color:#141414;font-weight:800;font-size:64px;padding:16px 44px;border-radius:60px;box-shadow:0 0 40px rgba(203,239,75,.55)}}
#foot{{position:absolute;z-index:8;top:1800px;left:0;right:0;text-align:center;font-weight:700;font-size:20px;letter-spacing:2px;color:rgba(255,255,255,.75)}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{T}" data-width="1080" data-height="1920">
{chr(10).join(v)}
{chr(10).join(names)}
<div id="vig" class="clip" data-start="0" data-duration="{T}"></div>
<div id="hook" class="clip" data-start="0" data-duration="{P[0]['dur']}"><div class="a">Você joga fora<br>a <span>melhor parte</span><br>da romã?</div><div class="b">O chá da casca 👇</div></div>
<div id="mid" class="clip" data-start="{P[5]['start']}" data-duration="{P[5]['dur']}">Tampa, canudo<br>e <span>pronto.</span></div>
<div id="end" class="clip" data-start="{P[6]['start']}" data-duration="{P[6]['dur']}"><div class="a">Salva essa<br>receita 💾</div><div class="p">Comenta GUIA 📩</div></div>
<div id="flash" class="clip" data-start="0" data-duration="{T}"></div>
<div id="frame" class="clip" data-start="0" data-duration="{T}"></div>
<div id="tag" class="clip" data-start="0" data-duration="{T}"><span class="dot"></span>OBOLARI ACADEMY<span class="c">· BEM-ESTAR</span></div>
<div id="foot" class="clip" data-start="0" data-duration="{T}">@OBOLARI_ACADEMY · CONTEÚDO EDUCATIVO · NÃO É RECOMENDAÇÃO MÉDICA</div>
</div><script>
const tl=gsap.timeline({{paused:true}});
tl.set("#flash",{{opacity:0}},0);
tl.fromTo("#hook .a",{{scale:1.5,opacity:0}},{{scale:1,opacity:1,duration:0.35,ease:"power4.out"}},0.05);
tl.fromTo("#hook .b",{{y:30,opacity:0}},{{y:0,opacity:1,duration:0.3}},0.5);
tl.fromTo("#hook .a span",{{color:"#ffffff"}},{{color:"#CBEF4B",duration:0.2}},0.7);
tl.fromTo("#mid",{{scale:0.6,opacity:0}},{{scale:1,opacity:1,duration:0.35,ease:"back.out(2)"}},{P[5]['start']+0.2});
tl.fromTo("#end .a",{{y:40,opacity:0}},{{y:0,opacity:1,duration:0.4,ease:"power3.out"}},{P[6]['start']+0.25});
tl.fromTo("#end .p",{{scale:0.6,opacity:0}},{{scale:1,opacity:1,duration:0.45,ease:"back.out(2.2)"}},{P[6]['start']+0.8});
tl.to("#end .p",{{scale:1.07,duration:0.45,yoyo:true,repeat:5,ease:"sine.inOut"}},{P[6]['start']+1.4});
{chr(10).join(js)}
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
open('hf/index.html','w').write(html);print(T)
