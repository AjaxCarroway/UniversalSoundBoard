from tkinter import filedialog

def select_sound(key, event):
    prompt = filedialog.askopenfilename(initialdir="",
                                                     title="Select A Sound",
                                                     filetypes=(("MP3", "*.mp3"),
                                                                ("WAV", "*.wav"),
                                                                ("OGG", "*.ogg")))
    key.set_soundfile(prompt)
    
def play_sound(key):
        pass
