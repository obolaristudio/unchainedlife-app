const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for (const [d,k,t1,t2,sub] of [['calc','CALCITONINA','Um remédio de osso','que veio do <span>salmão</span> 🐟','PEPTÍDEOS · UM POR VÍDEO'],['octr','OCTREOTIDA','O <span>freio</span> do','crescimento 🛑','achado no cérebro de ovelhas 🐑']]){
const bg='data:image/jpeg;base64,'+require('fs').readFileSync(process.argv[2]+'/'+d+'/cbg.jpg').toString('base64');
await p.setContent(`<html><body style="margin:0;width:1080px;height:1920px;background:url(${bg}) center/cover;font-family:Inter,sans-serif">
<div style="position:absolute;inset:0;background:linear-gradient(rgba(0,0,0,.15),rgba(0,0,0,.55))"></div>
<div style="position:absolute;left:70px;right:70px;top:560px;text-align:center">
<div style="display:inline-block;font-family:'DejaVu Sans Mono',monospace;font-weight:700;font-size:34px;letter-spacing:5px;background:#CBEF4B;border:4px solid #141414;padding:8px 20px;box-shadow:6px 6px 0 #141414">${k}</div>
<div style="margin-top:36px;background:#FBFAF6;border:6px solid #141414;box-shadow:14px 14px 0 #141414;border-radius:22px;padding:34px 30px;font-weight:900;font-size:84px;line-height:1.05;letter-spacing:-2px;color:#141414">${t1}<br>${t2.replace('<span>','<span style="background:#CBEF4B;border:4px solid #141414;padding:0 12px">')}</div>
<div style="margin-top:34px;display:inline-block;background:#141414;color:#CBEF4B;font-weight:800;font-size:40px;padding:12px 30px;border-radius:40px">${sub}</div></div>
<div style="position:absolute;top:0;left:0;right:0;height:110px;background:#2B2B2B;color:#F2EFE6;font-family:'DejaVu Sans Mono',monospace;font-size:26px;letter-spacing:4px;display:flex;align-items:flex-end;padding:0 70px 26px"><span style="color:#CBEF4B">●</span>&nbsp;OBOLARI ACADEMY</div></body></html>`);
await p.waitForTimeout(400);await p.screenshot({path:process.argv[2]+'/'+d+'/capa.jpg',type:'jpeg',quality:90});}
await b.close();})();
