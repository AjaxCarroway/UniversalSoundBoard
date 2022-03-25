from tkinter import *
from tkinter import filedialog
import soundboard_helper
#from playsound import playsound
from pygame import mixer
import multiprocessing
import soundboard_errors
import os
import pathlib
#import time


class Key:
    def __init__(self, keyname: str, window):
        self._keyname = keyname
        self._button = None
        self._soundfile = None
        self._photo = soundboard_helper.get_image()
        self._channel = None
        self._window = window
        self._label = None

    def create_button(self, window):
        button = Button(
            window, text=self._keyname,
            width=54, height=75,
            bg = "#09265C", highlightbackground= "#09265C",
            image=self._photo, borderwidth=0,
            compound='center',
            font=('Ubuntu', 20))
        if self._soundfile is None:
            soundLabel = Label(window, text='test')
        else:
            print("making label")
            soundLabel = Label(window, text=os.path.basename(self._soundfile), font=('Ubuntu', 20) )
        button.bind('<Enter>', self._hover)
        button.bind('<Leave>', self._leave)
        button.bind('<Button-1>', self.play_sound)
        button.bind('<Button-2>', self._select_sound)
        button.bind('<Button-3>', self._select_sound)
        self._button = button
        self._label = soundLabel

    def get_button(self):
        return self._button

    def get_label(self):
        return self._label

    def set_label(self, label):
        self._label = label
    def set_soundfile(self, file):
        self._soundfile = file

    def get_soundfile(self):
        return self._soundfile

    def _select_sound(self, event):
        try:
            tempfile = filedialog.askopenfilename(initialdir="",
                                                         title="Select A WAV or MP3 Sound File",
                                                         filetypes=(("MP3", "*.mp3"),
                                                                    ("WAV", "*.wav"),))
            try:
                p = multiprocessing.Process(target=soundboard_helper.zero_music(tempfile))
                p.start()
                self._soundfile = tempfile
            except:
                soundboard_errors.error_sound_unplayable(self._window)
            soundboard_helper.update_save_file(self._keyname, self._soundfile)
        except:
            soundboard_errors.error_sound_not_added(self._window)

    def play_sound(self, event=None):
        print(self._soundfile)
        if self._soundfile:
            p = multiprocessing.Process(target=soundboard_helper.music(self._soundfile, self._window))
            p.start()

    def _hover(self, event):
        self._button.config(background="#09265C")

    def _leave(self, event):
        self._button.config(background="#09265C")


