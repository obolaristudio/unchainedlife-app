import subprocess,json,sys,os
d=sys.argv[1]; S=json.load(open(f'{d}/scenes.json')); PW,PH=1080,1100; ST='stock'
os.makedirs(f'{d}/sc',exist_ok=True)
for i,(a,b,c,off,cx) in enumerate(S):
    dur=round(b-a,3)
    if c.startswith('gila'):
        src=f'{ST}/{c}.jpg'; n=int(dur*30)+2
        inp=['-loop','1','-t',str(dur),'-i',src]
        panel=f"scale=2400:-2,crop='min(iw,ih*{PW}/{PH})':ih,scale={PW*2}:{PH*2},zoompan=z='1.0+0.12*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={PW}x{PH}:fps=30"
    else:
        src=f'{ST}/{c}.mp4'
        L=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',src],capture_output=True,text=True).stdout)
        w,h=map(int,subprocess.run(['ffprobe','-v','error','-select_streams','v','-show_entries','stream=width,height','-of','csv=p=0',src],capture_output=True,text=True).stdout.strip().split(','))
        slow=''
        if L-off<dur: off=0; 
        if L<dur: slow=f'setpts={dur/L+0.01:.3f}*PTS,'
        inp=['-ss',str(off),'-i',src]
        if cx is None or h>w: panel=f'{slow}scale={PW}:-2,crop={PW}:{PH}'
        else:
            cw=round(h*PW/PH); x=int(max(0,min(w-cw,w*cx-cw/2)))
            panel=f'{slow}crop={cw}:{h}:{x}:0,scale={PW}:{PH}:flags=lanczos,unsharp=5:5:0.5'
    fc=(f"[0:v]fps=30,{panel},setsar=1,split[p0][b0];[p0]null[p];"
        f"[b0]scale=-2:1920,crop=1080:1920,boxblur=30:3,eq=brightness=-0.2:saturation=0.8,setsar=1[bg];[bg][p]overlay=0:420,format=yuv420p")
    subprocess.run(['ffmpeg','-loglevel','error','-y',*inp,'-t',str(dur),'-filter_complex',fc,'-an','-r','30','-c:v','libx264','-crf','16','-preset','veryfast',f'{d}/sc/sc_{i:02d}.mp4'],check=True)
open(f'{d}/sc/list.txt','w').write(''.join(f"file 'sc_{i:02d}.mp4'\n" for i in range(len(S))))
subprocess.run(['ffmpeg','-loglevel','error','-y','-f','concat','-i',f'{d}/sc/list.txt','-c','copy',f'{d}/bg.mp4'],check=True)
print(d,'ok',subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'{d}/bg.mp4'],capture_output=True,text=True).stdout)
