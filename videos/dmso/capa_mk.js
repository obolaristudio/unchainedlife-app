const {chromium}=require('playwright');const fs=require('fs');
const css=`@font-face{font-family:B;src:url(Bricolage-800.ttf);font-weight:800}@font-face{font-family:B;src:url(Bricolage-700.ttf);font-weight:700}
*{margin:0;padding:0;box-sizing:border-box}body{width:1080px;height:1920px;position:relative;overflow:hidden;font-family:B;background:#0E0E0E}
.ph{position:absolute;inset:0;width:1080px;height:1920px;object-fit:cover}
.sh{position:absolute;inset:0;background:linear-gradient(rgba(0,0,0,.35),rgba(0,0,0,0) 25%,rgba(0,0,0,0) 55%,rgba(0,0,0,.6))}
.chip{display:inline-block;background:#CBEF4B;color:#141414;font-weight:800;font-size:64px;padding:10px 34px;border-radius:22px;transform:rotate(-3deg);box-shadow:0 14px 40px rgba(0,0,0,.5)}
.box{display:inline-block;background:#fff;color:#111;font-weight:800;font-size:70px;line-height:1.08;white-space:nowrap;padding:26px 36px;border-radius:18px;box-shadow:0 20px 60px rgba(0,0,0,.45);letter-spacing:-1px}
.box em{font-style:normal;background:#CBEF4B;padding:0 10px;border-radius:8px}.box u{text-decoration:none;color:#D93025}
.sub{display:inline-block;margin-top:18px;background:rgba(14,14,14,.85);color:#fff;font-weight:700;font-size:44px;padding:12px 26px;border-radius:14px;border:3px solid #CBEF4B}
.w{position:absolute;left:70px;right:70px;text-align:center}
.fr{position:absolute;inset:26px;border:4px solid #CBEF4B;border-radius:34px;box-shadow:0 0 0 40px #0E0E0E}
.tag{position:absolute;top:80px;left:0;right:0;text-align:center;color:#fff;font-weight:700;font-size:26px;letter-spacing:8px;text-shadow:0 2px 10px #000}.tag b{color:#CBEF4B}`;
const h=`<div class="w" style="top:930px"><span class="chip">VOCÊ SABIA? 🤔</span></div>
<div class="w" style="top:1080px"><span class="box">Ela atravessa a pele<br>em <em>30 segundos</em>…<br>e <u>leva outras junto</u></span></div>
<div class="w" style="top:1440px"><span class="sub">até gosto de alho na boca ela dá 🧄</span></div>`;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
fs.writeFileSync('t.html',`<html><head><style>${css}</style></head><body><img class="ph" src="ph.jpg"><div class="sh"></div><div class="tag">● OBOLARI ACADEMY <b>· MOLÉCULAS</b></div>${h}<div class="fr"></div></body></html>`);
await p.goto('file://'+process.cwd()+'/t.html');await p.waitForTimeout(500);await p.screenshot({path:'capa.jpg',type:'jpeg',quality:92});await b.close()})();
