# pywinmm:
this python library can help you to control your audio files where it support a lot of file formats.\
video files will be supported through updates\
this library is using the winmulty media dll (winmm.dll) that comes with windows.\
am trying to make it simple as i can\
so please support with ideas or you can help on github project\
https://github.com/baaziznasser/pywinmm

## install pywinmm
you can install pywinmm through the pypi by using\
	pip install pywinmm\
## avalable functions
here is the list of avalable functions\
* load (load the file)
* loop (set or disable loop, the play function must recall after this function)
* reverce (enable or disable reverce, the play function must call after this one)
* loadrec (load the audio recorder)
* play (play the audio)
* record (start recording)
* pause (pause the player or recorder)
* resume (resume the player or the recorder)
* getlength (get the length of file or the recorded time)
* get position (get the current position)
* setposition (change the current position)
* get volume (get the current volume)
* setvolume (get the current volume)
* status (get the current status)
* stop (stop the player or the recorder)
* unload (unload the player or the recorder)


an other functions will be aded soon.

## example of usage:
	import pywinmm\
	import time\
	clip = pywinmm.load(r'snd.mp3')\
	print(clip.getvolume())\
	clip.setvolume(200)\
	print(clip.getvolume())\
	clip.loop(True)\
	clip.reverse(False)\
	clip.play()\
	print(clip.getlength())\
	time.sleep(1)\
	print(clip.getposition())\
	clip.setposition(2000)\
	print(clip.getposition())\
	clip.play()\
	print(clip.status())\


## notes:
this library can works only with windows