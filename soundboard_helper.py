from tkinter import *
import keyboard
import pygame.event
from PIL import ImageTk, Image
from pygame import mixer, K_SPACE
from pynput.keyboard import Key, Listener


def get_image():
    img = Image.open("key_unpressed.png")
    img = img.resize((70, 70), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)


def on_press_space():
    print("space")


def music(file):
    mixer.init()
    sound = mixer.Sound(file)
    channel = sound.play()