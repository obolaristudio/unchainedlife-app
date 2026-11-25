const {chromium}=require('playwright');const fs=require('fs');
const css=`@font-face{font-family:B;src:url(Bricolage-800.ttf);font-weight:800}@font-face{font-family:B;src:url(Bricolage-700.ttf);font-weight:700}
*{margin:0;padding:0;box-sizing:border-box}body{width:1080px;height:1920px;position:relative;overflow:hidden;font-family:B,"Noto Color Emoji";background:#0E0E0E}
.ph{position:absolute;inset:0;width:1080px;height:1920px;object-fit:cover}
.sh{position:absolute;inset:0;background:linear-gradient(rgba(0,0,0,.4),rgba(0,0,0,.1) 30%,rgba(0,0,0,.1) 55%,rgba(0,0,0,.65))}
.chip{display:inline-block;background:#CBEF4B;color:#141414;font-weight:800;font-size:60px;padding:10px 34px;border-radius:22px;transform:rotate(-3deg);box-shadow:0 14px 40px rgba(0,0,0,.5)}
.box{display:inline-block;background:#fff;color:#111;font-weight:800;font-size:74px;line-height:1.08;white-space:nowrap;padding:26px 36px;border-radius:18px;box-shadow:0 20px 60px rgba(0,0,0,.45);letter-spacing:-1px}
.box em{font-style:normal;background:#CBEF4B;padding:0 10px;border-radius:8px}.box u{text-decoration:none;color:#D93025}
.sub{display:inline-block;margin-top:18px;background:rgba(14,14,14,.85);color:#fff;font-weight:700;font-size:44px;padding:12px 26px;border-radius:14px;border:3px solid #CBEF4B}
.w{position:absolute;left:60px;right:60px;text-align:center}
.fr{position:absolute;inset:26px;border:4px solid #CBEF4B;border-radius:34px;box-shadow:0 0 0 40px #0E0E0E}
.tag{position:absolute;top:80px;left:0;right:0;text-align:center;color:#fff;font-weight:700;font-size:26px;letter-spacing:8px;text-shadow:0 2px 10px #000}.tag b{color:#CBEF4B}`;
const C={glu:{tag:'PEPTÍDEOS · GLUCAGON',h:`<div class="w" style="top:700px"><span class="chip">1922 · UM MISTÉRIO 🧪</span></div>
<div class="w" style="top:850px"><span class="box">O peptídeo que deu<br>nome ao <em>GLP-1</em>…<br>e faz o <u>contrário</u><br>da insulina</span></div>
<div class="w" style="top:1320px"><span class="sub">o nome do GLP-1 veio daqui 🤯</span></div>`},
cic:{tag:'PEPTÍDEOS · CICLOSPORINA',h:`<div class="w" style="top:700px"><span class="chip">1969 · NORUEGA 🇳🇴</span></div>
<div class="w" style="top:850px"><span class="box">Um punhado de terra<br>trazido das <em>férias</em><br>mudou a história<br>dos <u>transplantes</u></span></div>
<div class="w" style="top:1320px"><span class="sub">o peptídeo que veio de um fungo 🍄</span></div>`}};
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for(const d of ['glu','cic']){fs.writeFileSync('t.html',`<html><head><meta charset="utf-8"><style>${css}</style></head><body><img class="ph" src="${d}/ph.jpg"><div class="sh"></div><div class="tag">● OBOLARI ACADEMY <b>· ${C[d].tag}</b></div>${C[d].h}<div class="fr"></div></body></html>`);
await p.goto('file://'+process.cwd()+'/t.html');await p.waitForTimeout(600);await p.screenshot({path:`${d}/capa.jpg`,type:'jpeg',quality:92});}
await b.close()})();
