import sys;sys.path.insert(0,'../_lib')
from mix import mix
T=59.0
cues=[(0.0,'impact',0.6)]+[(t,'whoosh',0.35) for t in [5.2,8.1,16.9,23.2,29.9,33.3,37.2,45.6,48.5,55.1]]
cues+=[(t,'pop',0.5) for t in [3.4,12.6,15.0,19.6,22.0,24.7,28.7,31.4,34.2,42.3,45.75,46.9,48.8,51.9,56.1]]
cues+=[(29.95,'impact',0.6),(14.2,'impact',0.55),(40.4,'ding',0.4),(37.2,'ding',0.25)]
mix('silent.mp4','/tmp/claude-0/aud/v2.mp3','/tmp/claude-0/aud/music.mp3',T,cues,'reel.mp4')
