from tkinter import *
from PIL import ImageTk, Image


def get_image():
    img = Image.open("key_unpressed.png")
    img = img.resize((70, 70), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)
