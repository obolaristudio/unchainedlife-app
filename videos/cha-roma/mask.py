import numpy as np,sys
from PIL import Image,ImageFilter
Y0,Y1=640,1130
def mask(rgb):
    a=rgb[Y0:Y1].astype(np.float32)/255
    mx=a.max(2); mn=a.min(2); sat=(mx-mn)/(mx+1e-4)
    fg=((sat>0.52)|(mx<0.16)).astype(np.uint8)*255
    m=Image.fromarray(fg).filter(ImageFilter.MedianFilter(9)).filter(ImageFilter.MinFilter(5)).filter(ImageFilter.MaxFilter(7)).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(2.2))
    full=np.zeros(rgb.shape[:2],np.uint8); full[Y0:Y1]=np.array(m)
    # fade band edges
    full[Y0:Y0+30]=(full[Y0:Y0+30]*np.linspace(0,1,30)[:,None]).astype(np.uint8)
    full[Y1-30:Y1]=(full[Y1-30:Y1]*np.linspace(1,0,30)[:,None]).astype(np.uint8)
    return full
if __name__=='__main__':
    im=np.array(Image.open(sys.argv[1]).convert('RGB')); m=mask(im)
    red=np.zeros_like(im); red[:]=(229,57,53)
    out=(im*(m[...,None]/255)+red*(1-m[...,None]/255)).astype(np.uint8)
    Image.fromarray(out[560:1200]).resize((540,320)).save(sys.argv[2])
