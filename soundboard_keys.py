from tkinter import * 
import soundboard_helper
from functools import partial
from tkinter import filedialog

class Key:
    def __init__(self, keyname: str):
        self._keyname = keyname
        self._button = None
        self._soundfile = None

        
    def create_button(self, window):
        button = Button(
            master=window, text=self._keyname,
            height=2, width=2,
            font=('Helvetica', 20))
        button.bind('<Button-1>', self._play_sound)
        button.bind('<Button-2>', self._select_sound)
        self._button = button

    def get_button(self):
        return self._button

    def set_soundfile(self):
        self._soundfile = file

    def _select_sound(self, event):
        self._soundfile = filedialog.askopenfilename(initialdir="",
                                                     title="Select A Sound",
                                                     filetypes=(("MP3", "*.mp3"),
                                                                ("WAV", "*.wav"),
                                                                ("OGG", "*.ogg")))
    
    def _play_sound(self, event):
        pass
