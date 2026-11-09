import subprocess,json
# (start,end,clip,src_offset,crop_center_x_frac)
S=[(0.0,3.9,'17456',2.0,0.55),(3.9,7.0,'42136',1.0,None),(7.0,9.4,'3768',2.0,0.5),(9.4,12.5,'3968',1.0,0.5),
   (12.5,15.0,'13194',3.0,0.45),(15.0,17.6,'12892',1.0,0.55),(17.6,19.6,'32060',4.0,0.5),(19.6,21.3,'46088',1.5,0.7),
   (21.3,23.8,'47584',3.0,0.4),(23.8,26.3,'4767',2.0,0.42),(26.3,29.0,'4745',2.0,0.5),(29.0,31.3,'42136',5.0,None),
   (31.3,33.6,'34273',2.0,0.5),(33.6,39.6,'46747',3.0,0.45)]
PW,PH=1080,1100
for i,(a,b,c,off,cx) in enumerate(S):
    d=round(b-a,3); src=f'stock/{c}.mp4'
    if cx is None:  # vertical clip 720x1280: fit panel
        panel=f'scale={PW}:-2,crop={PW}:{PH}'
    else:
        cw=round(720*PW/PH); x=int(max(0,min(1280-cw,1280*cx-cw/2)))
        panel=f'crop={cw}:720:{x}:0,scale={PW}:{PH}:flags=lanczos,unsharp=5:5:0.6'
    fc=(f"[0:v]setpts=PTS-STARTPTS,fps=30,split[a][b];[a]{panel},setsar=1[p];"
        f"[b]scale=-2:1920,crop=1080:1920,boxblur=30:3,eq=brightness=-0.18:saturation=0.8,setsar=1[bg];"
        f"[bg][p]overlay=0:420,format=yuv420p")
    subprocess.run(['ffmpeg','-loglevel','error','-y','-ss',str(off),'-t',str(d),'-i',src,'-filter_complex',fc,'-an','-c:v','libx264','-crf','17','-preset','veryfast',f'sc_{i:02d}.mp4'],check=True)
open('list.txt','w').write(''.join(f"file 'sc_{i:02d}.mp4'\n" for i in range(len(S))))
subprocess.run(['ffmpeg','-loglevel','error','-y','-f','concat','-i','list.txt','-c','copy','bg.mp4'],check=True)
json.dump(S,open('scenes.json','w'))
print('ok')
