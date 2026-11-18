const {chromium}=require('playwright');
const V={
A:`<div class="k">ESCRITO HÁ 2 MIL ANOS</div><div class="t">ELA <span class="g">FALA.</span><br>E O MUNDO<br><span class="r">OBEDECE.</span></div><div class="s">Uma imagem feita pelo homem… 📜</div>`,
B:`<div class="k">UMA PASSAGEM ASSUSTADORA</div><div class="t">E SE O<br><span class="r">ANTICRISTO</span><br>FOR UMA <span class="g">IA?</span></div><div class="s">Apocalipse 13 descreve algo parecido 📖</div>`,
C:`<div class="k">POUCOS CONHECEM ESTE VERSÍCULO</div><div class="t">A BÍBLIA<br><span class="r">AVISOU</span><br>SOBRE A <span class="g">IA?</span></div><div class="s">Apocalipse 13:15 · “a imagem falasse”</div>`};
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for(const [k,h] of Object.entries(V)){
require('fs').writeFileSync(`t_${k}.html`,`<html><head><style>
@font-face{font-family:B;src:url(Bricolage-800.ttf);font-weight:800}
@font-face{font-family:B;src:url(Bricolage-700.ttf);font-weight:700}
*{margin:0;padding:0}body{width:1080px;height:1920px;position:relative;overflow:hidden;font-family:B;background:#000}
img{position:absolute;left:0;top:150px;width:1080px;height:1920px;object-fit:cover;filter:contrast(1.1) brightness(1.08)}
.sh{position:absolute;inset:0;background:linear-gradient(rgba(0,0,0,.9) 0%,rgba(0,0,0,.6) 28%,rgba(0,0,0,0) 40%,rgba(0,0,0,0) 80%,rgba(0,0,0,.5) 100%)}
.box{position:absolute;left:60px;right:60px;top:250px;text-align:center;color:#fff}
.k{display:inline-block;font-weight:700;font-size:34px;letter-spacing:6px;color:#E8B84A;border:2px solid #E8B84A;padding:8px 22px;border-radius:40px;background:rgba(0,0,0,.5)}
.t{font-weight:800;font-size:112px;line-height:.98;letter-spacing:-3px;margin-top:26px;text-shadow:0 8px 40px rgba(0,0,0,.95),0 0 4px #000}
.g{color:#E8B84A}.r{color:#ff3b30;text-shadow:0 0 40px rgba(255,59,48,.6),0 8px 30px #000}
.s{font-weight:700;font-size:44px;margin-top:26px;color:#EDE6D6;text-shadow:0 4px 20px #000}
.fr{position:absolute;inset:26px;border:4px solid #E8B84A;border-radius:34px;box-shadow:0 0 0 40px #0A0A0A}
</style></head><body><img src="bgA.png"><div class="sh"></div><div class="box">${h}</div><div class="fr"></div></body></html>`);await p.goto('file://'+process.cwd()+`/t_${k}.html`);
await p.waitForTimeout(400);await p.screenshot({path:`capa_${k}.jpg`,type:'jpeg',quality:92});}
await b.close()})();
