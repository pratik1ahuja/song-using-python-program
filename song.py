#!/usr/bin/python2

#to import all funtion of pygame
from  pygame import *

#to intilize mixer
mixer.init()

#to load yoor song
#first converet your .mp3 song into .ogg
#you can covert your song mp3 to ogg from this site https://audio.online-convert.com/convert-to-ogg
mixer.music.load('a.ogg')

#to play song
mixer.music.play()

#for no termination untill song is running
while mixer.music.get_busy():
	time.Clock().tick(10)
