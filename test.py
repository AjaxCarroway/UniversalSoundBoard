import multiprocessing
from playsound import playsound
import winsound


winsound.PlaySound("/home/moosestuff/PycharmProjects/soundboard/TestSounds/why-are_yIJ3kw3.mp3", winsound.SND_FILENAME)
input("press ENTER to stop playback")
winsound.PlaySound(None, winsound.SND_PURGE)
