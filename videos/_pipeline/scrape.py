import re,subprocess,sys
used=set(re.findall(r'\b\d{3,6}\b',open('/home/user/unchainedlife-app/research/clipes-usados.md').read()))
for q in sys.argv[1:]:
  for page in ['','?page=2']:
    h=subprocess.run(['curl','-s',f'https://mixkit.co/free-stock-video/{q}/{page}'],capture_output=True,text=True).stdout
    for alt,i in re.findall(r'alt="([^"]{5,90})"\s*/?>?\s*.{0,400}?assets\.mixkit\.co/videos/(\d+)/\d+-360',h,re.S):
      if i not in used and 'Envato' not in alt: print(q,i,alt)
