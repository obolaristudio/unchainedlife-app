const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const [dir,chip,l1,l2,sub]=process.argv.slice(2);
const css=`@font-face{font-family:B;src:url(${path.resolve(__dirname,'Bric.ttf')})}
*{margin:0;padding:0;box-sizing:border-box}body{width:1080px;height:1920px;position:relative;overflow:hidden;font-family:B;font-weight:800;background:#0E0E0E}
.ph{position:absolute;inset:0;width:1080px;height:1920px;object-fit:cover}
.sh{position:absolute;inset:0;background:linear-gradient(rgba(0,0,0,.35),rgba(0,0,0,0) 25%,rgba(0,0,0,.1) 50%,rgba(0,0,0,.65))}
.chip{display:inline-block;background:#CBEF4B;color:#141414;font-size:64px;padding:10px 34px;border-radius:22px;transform:rotate(-3deg);box-shadow:0 14px 40px rgba(0,0,0,.5)}
.box{display:inline-block;background:#F2EFE6;color:#111;font-size:76px;line-height:1.08;padding:26px 36px;border-radius:18px;border:5px solid #141414;box-shadow:12px 12px 0 #141414;letter-spacing:-1px}
.box em{font-style:normal;background:#CBEF4B;padding:0 10px;border-radius:8px}
.sub{display:inline-block;margin-top:18px;background:rgba(14,14,14,.88);color:#fff;font-size:44px;padding:12px 26px;border-radius:14px;border:3px solid #CBEF4B}
.w{position:absolute;left:70px;right:70px;text-align:center}
.fr{position:absolute;inset:26px;border:4px solid #CBEF4B;border-radius:34px;box-shadow:0 0 0 40px #0E0E0E}
.tag{position:absolute;top:80px;left:0;right:0;text-align:center;color:#fff;font-family:"DejaVu Sans Mono",monospace;font-weight:700;font-size:26px;letter-spacing:6px;text-shadow:0 2px 10px #000}.tag b{color:#CBEF4B}`;
const h=`<div class="w" style="top:620px"><span class="chip">${chip}</span></div>
<div class="w" style="top:760px"><span class="box">${l1}<br>${l2}</span></div>
<div class="w" style="top:1120px"><span class="sub">${sub}</span></div>`;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
const f=path.resolve(dir,'capa.html');
fs.writeFileSync(f,`<html><head><style>${css}</style></head><body><img class="ph" src="ph.jpg"><div class="sh"></div><div class="tag">● OBOLARI ACADEMY <b>· PEPTÍDEOS</b></div>${h}<div class="fr"></div></body></html>`);
await p.goto('file://'+f);await p.waitForTimeout(600);await p.screenshot({path:path.resolve(dir,'capa.jpg'),type:'jpeg',quality:92});await b.close()})();
