# Biblioteca comum dos Reels da rotina da madrugada (Obolari Academy).
# Uso: from common import *  (veja videos/timosina-alfa1/gen.py)
import subprocess,json,re,html,os,shutil
CSS='''
@font-face{font-family:"Bric";src:url("assets/fonts/Bric-700.ttf");font-weight:700}
@font-face{font-family:"Bric";src:url("assets/fonts/Bric-700.ttf");font-weight:800}
*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1920px;overflow:hidden;background:#0E0E0E}
#root{position:relative;width:1080px;height:1920px;font-family:"Bric","Noto Color Emoji",sans-serif;color:#fff;overflow:hidden}
#bg{position:absolute;inset:0;width:1080px;height:1920px;object-fit:cover;z-index:1}
#frame{position:absolute;inset:26px;z-index:9;border:4px solid #CBEF4B;border-radius:34px;box-shadow:0 0 0 40px #0E0E0E}
#tag{position:absolute;z-index:9;top:80px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:16px;font-weight:700;font-size:26px;letter-spacing:8px}
#tag .d{width:18px;height:18px;border-radius:50%;background:#CBEF4B;box-shadow:0 0 14px #CBEF4B}#tag .c{color:#CBEF4B}
.hd{position:absolute;z-index:6;left:40px;right:40px;top:150px;height:260px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.hd .s{font-weight:700;font-size:42px;color:#F2EFE6}
.hd .m{font-weight:800;font-size:76px;line-height:1.02;letter-spacing:-2px}
.hd .m span,.hd .s span{color:#CBEF4B}
.cap{position:absolute;z-index:6;left:60px;right:60px;top:1555px;text-align:center;font-weight:800;font-size:60px;line-height:1.1;letter-spacing:-1px;text-shadow:0 4px 18px rgba(0,0,0,.8)}
.cap .k{color:#CBEF4B}
.ov{position:absolute;z-index:5;left:50px;right:50px;top:1190px;text-align:center}
.pill{display:inline-block;background:rgba(14,14,14,.88);border:3px solid #CBEF4B;font-weight:800;font-size:44px;padding:12px 28px;border-radius:18px;margin:6px 0}
.pill b{color:#CBEF4B}.pill.v{border-color:#B388FF}.pill.v b{color:#B388FF}.pill.o{border-color:#FF8A3D}.pill.o b{color:#FF8A3D}
.big{font-weight:800;font-size:150px;line-height:1;text-shadow:0 10px 40px rgba(0,0,0,.6)}
.flag{font-size:170px;line-height:1}
.chip{display:inline-block;background:rgba(14,14,14,.9);border:3px solid #CBEF4B;font-weight:800;font-size:46px;padding:10px 26px;border-radius:16px;margin:6px 0}
.fall{position:absolute;top:0;z-index:7;line-height:1}
#stamp{position:absolute;z-index:7;left:0;right:0;top:800px;text-align:center}
#stamp span{display:inline-block;background:#CBEF4B;color:#141414;font-weight:800;font-size:150px;padding:6px 40px;border-radius:24px;transform:rotate(-4deg);box-shadow:0 20px 60px rgba(0,0,0,.6)}
#flash{position:absolute;inset:0;z-index:8;background:#fff;opacity:0}
#cta{position:absolute;z-index:6;left:0;right:0;top:1180px;text-align:center}
#cta span{display:inline-block;background:#CBEF4B;color:#141414;font-weight:800;font-size:64px;padding:18px 46px;border-radius:60px;box-shadow:0 0 50px rgba(203,239,75,.6)}
#foot{position:absolute;z-index:9;top:1800px;left:0;right:0;text-align:center;font-weight:700;font-size:20px;letter-spacing:2px;color:rgba(255,255,255,.75)}
.bead{display:inline-block;width:44px;height:44px;border-radius:50%;background:#CBEF4B;border:3px solid #141414;margin:0 3px}
'''
def build_bg(S,stock='/tmp/claude-0/stock',out='.'):
    PW,PH=1080,1100
    for i,(a,b,c,off,cx) in enumerate(S):
        d=round(b-a,3); src=f'{stock}/{c}.mp4'
        cw=round(720*PW/PH); x=int(max(0,min(1280-cw,1280*(cx or .5)-cw/2)))
        panel=f'crop={cw}:720:{x}:0,scale={PW}:{PH}:flags=lanczos,unsharp=5:5:0.6'
        fc=(f"[0:v]setpts=PTS-STARTPTS,fps=30,split[a][b];[a]{panel},setsar=1[p];"
            f"[b]scale=-2:1920,crop=1080:1920,boxblur=30:3,eq=brightness=-0.18:saturation=0.8,setsar=1[bg];"
            f"[bg][p]overlay=0:420,format=yuv420p")
        subprocess.run(['ffmpeg','-loglevel','error','-y','-stream_loop','-1','-ss',str(off),'-t',str(d),'-i',src,'-filter_complex',fc,'-an','-c:v','libx264','-crf','17','-preset','veryfast',f'{out}/sc_{i:02d}.mp4'],check=True)
    open(f'{out}/list.txt','w').write(''.join(f"file 'sc_{i:02d}.mp4'\n" for i in range(len(S))))
    subprocess.run(['ffmpeg','-loglevel','error','-y','-f','concat','-i',f'{out}/list.txt','-c','copy',f'{out}/bg.mp4'],check=True)
def captions(W,T,KEY):
    groups=[];cur=[]
    for w in W:
        cur.append(w)
        if len(cur)==3 or re.search(r'[,.?!:]$',w['w']): groups.append(cur);cur=[]
    if cur: groups.append(cur)
    caps=[];js=[]
    for gi,g in enumerate(groups):
        a=g[0]['s']; b=groups[gi+1][0]['s'] if gi+1<len(groups) else T-0.1
        spans=''.join(f'<span class="{"k" if w["w"].strip(".,?!:").lower() in KEY else ""}" id="c{gi}_{j}">{html.escape(w["w"])}</span> ' for j,w in enumerate(g))
        caps.append(f'<div id="cg{gi}" class="clip cap" data-start="{a:.2f}" data-duration="{b-a:.2f}">{spans}</div>')
        for j,w in enumerate(g): js.append(f'tl.fromTo("#c{gi}_{j}",{{opacity:0.25,y:8}},{{opacity:1,y:0,duration:0.12}},{w["s"]:.2f});')
    return caps,js
def hd(id,a,b,inner): return f'<div id="{id}" class="clip hd" data-start="{a}" data-duration="{round(b-a,2)}">{inner}</div>'
def page(T,body,js,series):
    return f'''<!doctype html><html lang="pt-BR"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script><style>{CSS}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{T}" data-width="1080" data-height="1920">
<video id="bg" class="clip" data-start="0" data-duration="{T}" src="assets/bg.mp4" muted></video>
{body}
<div id="flash" class="clip" data-start="0" data-duration="{T}"></div>
<div id="frame" class="clip" data-start="0" data-duration="{T}"></div>
<div id="tag" class="clip" data-start="0" data-duration="{T}"><span class="d"></span>OBOLARI ACADEMY<span class="c">· {series}</span></div>
<div id="foot" class="clip" data-start="0" data-duration="{T}">@OBOLARI_ACADEMY · CONTEÚDO EDUCATIVO · NÃO É RECOMENDAÇÃO MÉDICA</div>
</div><script>
const tl=gsap.timeline({{paused:true}});
{js}
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
