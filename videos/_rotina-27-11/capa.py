import sys,subprocess
from PIL import Image,ImageDraw,ImageFont
v,t,l1,l2,l3,tag=sys.argv[1:7]
subprocess.run(['ffmpeg','-loglevel','error','-y','-ss',t,'-i',f'{v}/hf/assets/bg.mp4','-frames:v','1',f'{v}/bgf.png'],check=True)
im=Image.open(f'{v}/bgf.png').convert('RGB'); d=ImageDraw.Draw(im,'RGBA')
d.rectangle([0,0,1080,1920],fill=(0,0,0,95))
F=lambda s,f='Bric-800.ttf': ImageFont.truetype(f'fonts/{f}',s)
def ctext(y,txt,font,fill,box=None):
    w=d.textlength(txt,font=font); x=(1080-w)/2
    if box: d.rounded_rectangle([x-28,y-8,x+w+28,y+font.size+22],18,fill=box,outline=(20,20,20),width=6)
    d.text((x,y),txt,font=font,fill=fill)
ctext(470,tag,F(34,'Mono.ttf'),(203,239,75))
ctext(640,l1,F(110),(255,255,255))
sz=120
while d.textlength(l2,font=F(sz))>900: sz-=4
ctext(790+(120-sz)//2,l2,F(sz),(20,20,20),box=(203,239,75))
ctext(990,l3,F(54),(255,255,255))
d.rounded_rectangle([26,26,1054,1894],34,outline=(203,239,75),width=5)
ctext(1480,'@obolari_academy',F(36,'Mono.ttf'),(203,239,75))
im.save(f'{v}/capa.jpg',quality=92); print('capa',v)
