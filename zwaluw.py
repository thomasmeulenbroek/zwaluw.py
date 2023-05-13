import os,time, pathlib
from pygame import mixer
from mutagen.mp3 import MP3

path = pathlib.Path(__file__).parent.absolute()

playing = 1
mixer.init()
dir = str(path) + '/sounds/'
songs = os.listdir(dir)
index = 0
while 1 :
	print(songs)
	for song in songs :
		print('index ', index, songs[index])
		f = dir + songs[index]
		mixer.music.load(f)
		mixer.music.play(1,0)
		s = MP3(f)
		t = s.info.length
		print('play duration: ', t)
		time.sleep(t)
		index+=1