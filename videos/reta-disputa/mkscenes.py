import subprocess,json
S=json.load(open('scenes.json')); PW,PH=1080,1100
for i,(a,b,c,off,cx) in enumerate(S):
    d=round(b-a,3); src=f'stock/{c}.mp4'
    w,h=map(int,subprocess.run(['ffprobe','-v','error','-select_streams','v','-show_entries','stream=width,height','-of','csv=p=0',src],capture_output=True,text=True).stdout.strip().split(','))
    if cx is None or h>w: panel=f'scale={PW}:-2,crop={PW}:{PH}'
    else:
        cw=round(h*PW/PH); x=int(max(0,min(w-cw,w*cx-cw/2)))
        panel=f'crop={cw}:{h}:{x}:0,scale={PW}:{PH}:flags=lanczos,unsharp=5:5:0.5'
    fc=(f"[0:v]setpts=PTS-STARTPTS,fps=30,split[a][b];[a]{panel},setsar=1[p];"
        f"[b]scale=-2:1920,crop=1080:1920,boxblur=30:3,eq=brightness=-0.2:saturation=0.8,setsar=1[bg];[bg][p]overlay=0:420,format=yuv420p")
    subprocess.run(['ffmpeg','-loglevel','error','-y','-ss',str(off),'-t',str(d),'-i',src,'-filter_complex',fc,'-an','-c:v','libx264','-crf','16','-preset','veryfast',f'sc_{i:02d}.mp4'],check=True)
open('list.txt','w').write(''.join(f"file 'sc_{i:02d}.mp4'\n" for i in range(len(S))))
subprocess.run(['ffmpeg','-loglevel','error','-y','-f','concat','-i','list.txt','-c','copy','bg.mp4'],check=True)
print('ok')
