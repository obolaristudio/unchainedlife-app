import sys
from PIL import Image, ImageDraw, ImageFont
name, frame, l1, l2, pill = sys.argv[1:6]
FB='/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf'
im=Image.open(f'out_{name}/base.png').convert('RGB'); d=ImageDraw.Draw(im)
d.rectangle([40,1830,1080,1880],fill='#F2EFE6')
fr=Image.open(frame).convert('RGB').resize((1000,1080))
m=Image.open(f'out_{name}/mask.png'); im.paste(fr,(40,430),m)
f=ImageFont.truetype(FB,92); fp=ImageFont.truetype(FB,70)
for i,t in enumerate([l1,l2]):
    w=d.textlength(t,font=f); d.text(((1080-w)/2,150+i*105),t,font=f,fill='#141414')
w=d.textlength(pill,font=fp); x=(1080-w)/2; y=1240
d.rounded_rectangle([x-36+10,y-20+10,x+w+36+10,y+96+10],16,fill='#141414')
d.rounded_rectangle([x-36,y-20,x+w+36,y+96],16,fill='#CBEF4B',outline='#141414',width=5)
d.text((x,y),pill,font=fp,fill='#141414')
im.save(f'capa_{name}.jpg',quality=92)
