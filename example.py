import pywinmm
import time
clip = pywinmm.load(r'snd.mp3')
print(clip.getvolume())
clip.setvolume(200)
print(clip.getvolume())
clip.loop(True)
clip.reverse(False)
clip.play()
print(clip.getlength())
time.sleep(1)
print(clip.getposition())
clip.setposition(2000)
print(clip.getposition())
clip.play()
print(clip.status())

time.sleep(50)