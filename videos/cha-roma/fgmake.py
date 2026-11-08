import numpy as np,subprocess,sys
sys.path.insert(0,'.')
from mask import mask
W,H=1080,1920
for f in sys.argv[1:]:
    src=f'hf/assets/{f}.mp4'; out=f'hf/assets/{f}_fg.webm'
    dec=subprocess.Popen(['ffmpeg','-loglevel','error','-i',src,'-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
    enc=subprocess.Popen(['ffmpeg','-loglevel','error','-y','-f','rawvideo','-pix_fmt','rgba','-s',f'{W}x{H}','-r','30','-i','-','-c:v','libvpx-vp9','-pix_fmt','yuva420p','-b:v','6M','-deadline','realtime','-cpu-used','8','-auto-alt-ref','0',out],stdin=subprocess.PIPE)
    n=0
    while True:
        b=dec.stdout.read(W*H*3)
        if len(b)<W*H*3: break
        rgb=np.frombuffer(b,np.uint8).reshape(H,W,3)
        rgba=np.dstack([rgb,mask(rgb)]); enc.stdin.write(rgba.tobytes()); n+=1
    enc.stdin.close(); enc.wait(); print(f,n,flush=True)
