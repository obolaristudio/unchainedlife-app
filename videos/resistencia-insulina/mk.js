const {chromium}=require('playwright');const fs=require('fs');
const css=`@font-face{font-family:B;src:url(Bricolage-800.ttf);font-weight:800}@font-face{font-family:B;src:url(Bricolage-700.ttf);font-weight:700}
*{margin:0;padding:0;box-sizing:border-box}body{width:1080px;height:1920px;position:relative;overflow:hidden;font-family:B;background:#0E0E0E}
.ph{position:absolute;inset:0;width:1080px;height:1920px;object-fit:cover}
.sh{position:absolute;inset:0;background:linear-gradient(rgba(0,0,0,.35),rgba(0,0,0,0) 30%,rgba(0,0,0,0) 60%,rgba(0,0,0,.55))}
.chip{display:inline-block;background:#CBEF4B;color:#141414;font-weight:800;font-size:64px;padding:10px 34px;border-radius:22px;transform:rotate(-3deg);box-shadow:0 14px 40px rgba(0,0,0,.5)}
.box{display:inline-block;background:#fff;color:#111;font-weight:800;font-size:76px;line-height:1.05;padding:26px 36px;border-radius:18px;box-shadow:0 20px 60px rgba(0,0,0,.45);letter-spacing:-1px}
.box em{font-style:normal;background:#CBEF4B;padding:0 10px;border-radius:8px}.box u{text-decoration:none;color:#D93025}
.sub{display:inline-block;margin-top:18px;background:rgba(14,14,14,.85);color:#fff;font-weight:700;font-size:44px;padding:12px 26px;border-radius:14px;border:3px solid #CBEF4B}
.w{position:absolute;left:70px;right:70px;text-align:center}
.fr{position:absolute;inset:26px;border:4px solid #CBEF4B;border-radius:34px;box-shadow:0 0 0 40px #0E0E0E}
.tag{position:absolute;top:80px;left:0;right:0;text-align:center;color:#fff;font-weight:700;font-size:26px;letter-spacing:8px;text-shadow:0 2px 10px #000}.tag b{color:#CBEF4B}
.split{display:flex;flex-direction:column;gap:22px;align-items:center}
.row{background:rgba(14,14,14,.9);color:#fff;font-weight:800;font-size:66px;white-space:nowrap;padding:18px 36px;border-radius:22px;border:5px solid #CBEF4B}
.row.r{border-color:#E53935}.row .g{color:#CBEF4B}.row .rd{color:#FF6B5E}`;
const V={
A:{img:'p46085.jpg',h:`<div class="w" style="top:330px"><span class="chip">VOCÊ SABIA? 🤔</span></div>
<div class="w" style="top:500px"><span class="box">Seu exame pode vir <em>NORMAL</em>…<br>e você ter <u>resistência<br>à insulina</u></span></div>
<div class="w" style="top:1420px"><span class="sub">o problema que fica 10+ anos escondido</span></div>`},
B:{img:'p40831.jpg',h:`<div class="w" style="top:330px"><span class="chip">VOCÊ SABIA? 🤔</span></div>
<div class="w" style="top:1000px"><span class="box"><u>4 sinais</u> de resistência<br>à insulina que<br><em>quase ninguém percebe</em></span></div>
<div class="w" style="top:1440px"><span class="sub">o 2º acontece depois do almoço 😴</span></div>`},
C:{img:'p17456.jpg',h:`<div class="w" style="top:330px"><span class="chip">VOCÊ SABIA? 🤔</span></div>
<div class="w" style="top:520px"><div class="split"><div class="row">Glicose: <span class="g">normal ✅</span></div><div class="row r">Insulina: <span class="rd">lá em cima ⚠️</span></div></div></div>
<div class="w" style="top:1420px"><span class="sub">o que o seu exame <b style="color:#CBEF4B">não mostra</b></span></div>`}};
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for(const [k,v] of Object.entries(V)){fs.writeFileSync(`t_${k}.html`,`<html><head><style>${css}</style></head><body><img class="ph" src="${v.img}"><div class="sh"></div><div class="tag">● OBOLARI ACADEMY <b>· METABOLISMO</b></div>${v.h}<div class="fr"></div></body></html>`);
await p.goto('file://'+process.cwd()+`/t_${k}.html`);await p.waitForTimeout(500);await p.screenshot({path:`capa_${k}.jpg`,type:'jpeg',quality:92});}
await b.close()})();
