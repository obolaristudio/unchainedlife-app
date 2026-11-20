const {chromium}=require('playwright');
(async()=>{const d=process.argv[2];const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for(const n of ['capa1','capa2','capa3']){await p.goto('file://'+d+'/'+n+'.html');await p.waitForTimeout(300);await p.screenshot({path:d+'/'+n+'.png'});}
await b.close();})();
