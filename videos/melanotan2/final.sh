#!/bin/bash
# usage: final.sh dir
cd $1
ffmpeg -loglevel error -y -i video.mp4 -c:v libx264 -b:v 1380k -maxrate 2500k -bufsize 3000k -preset slow -pass 1 -passlogfile p2 -an -f null /dev/null
ffmpeg -loglevel error -y -i video.mp4 -i mix.wav -map 0:v -map 1:a -c:v libx264 -b:v 1380k -maxrate 2500k -bufsize 3000k -preset slow -pass 2 -passlogfile p2 -pix_fmt yuv420p -r 30 -c:a aac -b:a 160k -shortest -movflags +faststart reel.mp4
ls -la reel.mp4
