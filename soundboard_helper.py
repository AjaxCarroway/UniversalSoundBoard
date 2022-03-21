from tkinter import *
#import keyboard
# import pygame.event
from PIL import ImageTk, Image
from pygame import mixer, K_SPACE


def get_image():
    img = Image.open("venv/src/key_unpressed.png")
    img = img.resize((70, 70), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)


def on_press_space(sound):
    if sound:
        sound.stop()


def music(file):
    mixer.init()
    sound = mixer.Sound(file)
    channel = sound.play()
