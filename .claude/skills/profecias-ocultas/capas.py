import sys, base64
import os
S=sys.argv[1]
def b64(p): return "data:image/png;base64,"+base64.b64encode(open(p,"rb").read()).decode()
CSS="""*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1920px;overflow:hidden;font-family:'Inter';background:#000;position:relative}
.bg{position:absolute;inset:0;background-size:cover;background-position:center;filter:brightness(1.18) contrast(1.12) saturate(1.1)}
.sh{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.15) 0%,rgba(0,0,0,.25) 35%,rgba(0,0,0,.85) 62%,rgba(0,0,0,.95) 100%)}
.vig{position:absolute;inset:0;box-shadow:inset 0 0 260px 60px rgba(0,0,0,.9)}
.wrap{position:absolute;left:70px;right:70px;top:1000px;text-align:center}
.tag{display:inline-block;background:#E53935;color:#fff;font-weight:900;font-size:40px;letter-spacing:4px;padding:12px 26px;border-radius:6px;margin-bottom:34px;text-transform:uppercase}
h1{color:#fff;font-weight:900;font-size:118px;line-height:1.0;letter-spacing:-3px;text-transform:uppercase;text-shadow:0 6px 30px rgba(0,0,0,.9)}
h1 .r{color:#FF2D2D;text-shadow:0 0 40px rgba(255,30,30,.65),0 6px 30px rgba(0,0,0,.9)}
.sub{color:#eee;font-weight:800;font-size:44px;margin-top:34px;text-transform:uppercase;letter-spacing:1px}
.sub b{color:#FF2D2D}
.ring{position:absolute;border:10px solid #FF2D2D;border-radius:50%;box-shadow:0 0 40px rgba(255,40,40,.8)}
.arrow{position:absolute;color:#FF2D2D;font-size:150px;font-weight:900;text-shadow:0 0 30px rgba(255,0,0,.7)}
"""
caps=[
 ("capa1","00.png",'<div class="tag">Apocalipse 13</div><h1>Você vai<br><span class="r">implorar</span><br>por esse chip</h1><div class="sub">e nem vai perceber <b>como</b></div>',
  '<div class="ring" style="left:610px;top:535px;width:220px;height:220px"></div>'),
 ("capa2","10.png",'<div class="tag">Ninguém está vendo</div><h1>Você vai<br><span class="r">implorar</span><br>pela marca</h1><div class="sub">a Bíblia avisou há <b>2.000 anos</b></div>',
  '<div class="ring" style="left:330px;top:500px;width:420px;height:420px"></div>'),
 ("capa3","11.png",'<div class="tag">Abra os olhos</div><h1>Não vão te<br>obrigar.<br><span class="r">Você vai pedir.</span></h1><div class="sub">a tecnologia da <b>marca</b> já existe</div>',
  '<div class="ring" style="left:395px;top:725px;width:200px;height:200px"></div>'),
]
for name,img,txt,extra in caps:
    html=f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="bg" style="background-image:url({b64(S+"/img/"+img)})"></div><div class="sh"></div><div class="vig"></div>{extra}<div class="wrap">{txt}</div></body></html>'
    open(f"{S}/capas/{name}.html","w").write(html)
