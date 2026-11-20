const {chromium}=require('playwright');const fs=require('fs');const d=process.argv[2];const C=JSON.parse(fs.readFileSync(d+'/capa.json'));
const css=`@font-face{font-family:B;src:url(../Bricolage-800.ttf);font-weight:800}@font-face{font-family:B;src:url(../Bricolage-700.ttf);font-weight:700}
*{margin:0;padding:0;box-sizing:border-box}body{width:1080px;height:1920px;position:relative;overflow:hidden;font-family:B;background:#0E0E0E}
.ph{position:absolute;inset:0;width:1080px;height:1920px;object-fit:cover;filter:brightness(.8)}
.sh{position:absolute;inset:0;background:linear-gradient(rgba(0,0,0,.35),rgba(0,0,0,0) 25%,rgba(0,0,0,0) 50%,rgba(0,0,0,.65))}
.chip{display:inline-block;background:#CBEF4B;color:#141414;font-weight:800;font-size:60px;padding:10px 34px;border-radius:22px;transform:rotate(-3deg);box-shadow:0 14px 40px rgba(0,0,0,.5)}
.box{display:inline-block;background:#fff;color:#111;font-weight:800;font-size:72px;line-height:1.08;white-space:nowrap;padding:26px 36px;border-radius:18px;box-shadow:0 20px 60px rgba(0,0,0,.45);letter-spacing:-1px}
.box em{font-style:normal;background:#CBEF4B;padding:0 10px;border-radius:8px}.box u{text-decoration:none;color:#D9503F}
.sub{display:inline-block;margin-top:18px;background:rgba(14,14,14,.85);color:#fff;font-weight:700;font-size:44px;padding:12px 26px;border-radius:14px;border:3px solid #CBEF4B}
.w{position:absolute;left:60px;right:60px;text-align:center}
.fr{position:absolute;inset:26px;border:4px solid #CBEF4B;border-radius:34px;box-shadow:0 0 0 40px #0E0E0E}
.tag{position:absolute;top:80px;left:0;right:0;text-align:center;color:#fff;font-weight:700;font-size:26px;letter-spacing:8px;text-shadow:0 2px 10px #000}.tag b{color:#CBEF4B}`;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
fs.writeFileSync(d+'/t.html',`<html><head><meta charset="utf-8"><style>${css}</style></head><body><img class="ph" src="ph.jpg"><div class="sh"></div><div class="tag">● OBOLARI ACADEMY <b>${C.tag}</b></div><div class="w" style="top:880px"><span class="chip">${C.chip}</span></div><div class="w" style="top:1020px"><span class="box">${C.box}</span></div><div class="w" style="top:1390px"><span class="sub">${C.sub}</span></div><div class="fr"></div></body></html>`);
await p.goto('file://'+process.cwd()+'/'+d+'/t.html');await p.waitForTimeout(500);await p.screenshot({path:d+'/capa.jpg',type:'jpeg',quality:92});await b.close()})();
