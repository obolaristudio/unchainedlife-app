const {chromium}=require('playwright');
const [,,d,kick,title,sub]=process.argv;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
const html=`<html><head><style>@font-face{font-family:B;src:url(file://${process.cwd()}/BricolageGrotesque-Bold.ttf)}
body{margin:0;width:1080px;height:1920px;background:url(file://${process.cwd()}/${d}/cover_bg.jpg) center/cover;font-family:B;overflow:hidden}
.sh{position:absolute;inset:0;background:linear-gradient(rgba(0,0,0,.35),rgba(0,0,0,.55) 40%,rgba(0,0,0,.75))}
.fr{position:absolute;inset:26px;border:4px solid #CBEF4B;border-radius:34px}
.tag{position:absolute;top:80px;width:100%;text-align:center;color:#fff;font-size:26px;letter-spacing:8px}.tag b{color:#CBEF4B}
.box{position:absolute;left:70px;right:70px;top:640px;text-align:center;color:#fff}
.k{display:inline-block;background:#CBEF4B;color:#141414;font-size:44px;padding:8px 24px;border-radius:14px;border:3px solid #141414;box-shadow:6px 6px 0 #141414;letter-spacing:3px}
.t{font-size:118px;line-height:1.0;letter-spacing:-3px;margin-top:30px;text-shadow:0 8px 30px rgba(0,0,0,.7)} .t span{color:#CBEF4B}
.s{font-size:48px;margin-top:26px;color:#F2EFE6}</style></head><body><div class="sh"></div><div class="fr"></div>
<div class="tag">● OBOLARI ACADEMY <b>· PEPTÍDEOS</b></div>
<div class="box"><div class="k">${kick}</div><div class="t">${title}</div><div class="s">${sub}</div></div></body></html>`;
require("fs").writeFileSync(`${d}/cover.html`,html);await p.goto(`file://${process.cwd()}/${d}/cover.html`);await p.waitForTimeout(500);await p.screenshot({path:`${d}/capa.jpg`,type:'jpeg',quality:92});await b.close();})();
