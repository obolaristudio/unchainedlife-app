import subprocess,json,sys
d=sys.argv[1]; S=json.load(open(f'{d}/scenes.json')); PW,PH=1080,1100
for i,sc in enumerate(S):
    a,b,c,off=sc[:4]; gray=len(sc)>4 and sc[4]
    dd=round(b-a,3); src=f'stock/{c}.mp4'
    w,h=map(int,subprocess.run(['ffprobe','-v','error','-select_streams','v','-show_entries','stream=width,height','-of','csv=p=0',src],capture_output=True,text=True).stdout.strip().split(','))
    panel=f'scale={PW}:-2,crop={PW}:{PH}' if h>w else f'crop={round(h*PW/PH)}:{h},scale={PW}:{PH}:flags=lanczos,unsharp=5:5:0.5'
    g=',hue=s=0,eq=contrast=1.15' if gray else ''
    # slow zoom drift inside scene
    fc=(f"[0:v]setpts=PTS-STARTPTS,fps=30,split[a][b];[a]{panel}{g},zoompan=z='1.0+0.0007*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={PW}x{PH}:fps=30,setsar=1[p];"
        f"[b]scale=-2:1920,crop=1080:1920,boxblur=30:3,eq=brightness=-0.2:saturation=0.8{g},setsar=1[bg];[bg][p]overlay=0:420,format=yuv420p")
    subprocess.run(['ffmpeg','-loglevel','error','-y','-stream_loop','-1','-ss',str(off),'-t',str(dd),'-i',src,'-filter_complex',fc,'-an','-r','30','-c:v','libx264','-crf','16','-preset','veryfast',f'{d}/sc_{i:02d}.mp4'],check=True)
open(f'{d}/list.txt','w').write(''.join(f"file 'sc_{i:02d}.mp4'\n" for i in range(len(S))))
subprocess.run(['ffmpeg','-loglevel','error','-y','-f','concat','-i',f'{d}/list.txt','-c','copy',f'{d}/hf/assets/bg.mp4'],check=True)
print('bg ok',d)
