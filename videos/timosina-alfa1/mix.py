import sys;sys.path.insert(0,'../_lib')
from mix import mix
T=57.6
cues=[(0.0,'impact',0.6)]+[(t,'whoosh',0.35) for t in [5.4,8.9,13.8,20.8,26.1,30.7,37.9,43.5,47.0,53.3]]
cues+=[(t,'pop',0.5) for t in [9.6,11.0,12.3,14.7,16.7,18.7,20.95,22.8,24.8,26.25,27.9,31.2,32.2,35.4,38.05,40.7,42.4,43.65,44.8,47.3,50.0,54.1]]
cues+=[(33.7,'impact',0.6),(14.6,'whoosh',0.5),(16.0,'ding',0.4)]
mix('silent.mp4','/tmp/claude-0/aud/v1.mp3','/tmp/claude-0/aud/music.mp3',T,cues,'reel.mp4')
