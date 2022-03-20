from tkinter import *
from tkinter import filedialog
import soundboard_helper
from playsound import playsound
import multiprocessing


class Key:
    def __init__(self, keyname: str):
        self._keyname = keyname
        self._button = None
        self._soundfile = None
        self._photo = soundboard_helper.get_image()

    def create_button(self, window):
        button = Button(
            window, text=self._keyname,
            width=60, height=60,
            image=self._photo, borderwidth=0,
            compound='center',
            font=('Helvetica', 20))
        button.bind('<Enter>', self._hover)
        button.bind('<Leave>', self._leave)
        button.bind('<Button-1>', self._play_sound)
        button.bind('<Button-2>', self._select_sound)
        button.bind('<Button-3>', self._select_sound)
        self._button = button

    def get_button(self):
        return self._button

    def set_soundfile(self):
        pass

    def _select_sound(self, event):
        self._soundfile = filedialog.askopenfilename(initialdir="",
                                                     title="Select A WAV or MP3 Sound File",
                                                     filetypes=(("MP3", "*.mp3"),
                                                                ("WAV", "*.wav"),))

    def _play_sound(self, event):
        if self._soundfile:
            interrupt = multiprocessing.Process(target=playsound, args=self._soundfile)
            interrupt.start()

    def _hover(self, event):
        self._button.config(background=self._button.cget('background'))

    def _leave(self, event):
        self._button.config(background=self._button.cget('background'))
