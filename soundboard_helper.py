from tkinter import *
#import keyboard
# import pygame.event
from PIL import ImageTk, Image
from pygame import mixer
import os.path
import time
import soundboard_errors


def get_image():
    img = Image.open("key_unpressed.png")
    img = img.resize((80, 80), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)


def music(file, window):
    if file != 'None' and not file.isspace():
        mixer.init()
        sound = mixer.Sound(file)
        channel = sound.play()
    else:
        assert isinstance(window, object)
        soundboard_errors.error_sound_not_added(window)
        return

def zero_music(file):
    if file != 'None' and not file.isspace():
        mixer.init()
        sound = mixer.Sound(file)
        sound.set_volume(0)
        channel = sound.play()
    else:
        return


def get_save_file():
    pass


def create_save_file(keyDict):
    exists = os.path.exists("KeyMap.txt")
    if not exists:
        file = open("KeyMap.txt", 'w')
        filetext = ''
        if keyDict is not None:
            keys = keyDict.keys()
            for key in keys:
                filetext += f"{key}: {keyDict[key].get_soundfile()}\n"
        file.write(filetext)
        file.close()
    else:
        file = open("KeyMap.txt", 'r')
        filetext = file.read()
        lines = filetext.split('\n')
        keyList = []
        print(lines)
        if keyDict is not None:
            keys = keyDict.keys()
            for key in keys:
                keyList.append(key)
        print(keyList)
        for i in range(len(lines)-1):
            keyDict[keyList[i]].set_soundfile(lines[i][3:])

def update_save_file(key, path):
    rfile = open("KeyMap.txt", 'r')
    text = rfile.read()
    textlines = text.split('\n')
    keyword = f"{key}:"
    for i in range(len(textlines)):
        if keyword in textlines[i][0:2]:
            textlines[i] = f"{key}: {path}"
    text = '\n'.join(textlines)
    rfile.close()
    wfile = open("KeyMap.txt", 'w')
    wfile.write(text)
    wfile.close()

def update_labels(window, keyDict):
    keys = keyDict.keys()
    soundLabel = ''
    for key in keys:
        print(f"{key} and {keyDict[key].get_soundfile()}")
        if keyDict[key].get_soundfile() is None:
            soundLabel = Label(window, text='test')
        else:
            soundLabel = Label(window, text=os.path.basename(keyDict[key].get_soundfile()), font=('Ubuntu', 20))
        keyDict[key].set_label(soundLabel)
    return keyDict