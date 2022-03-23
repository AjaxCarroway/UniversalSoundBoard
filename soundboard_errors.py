from tkinter import *
import time
import multiprocessing as mp
import threading

def hide_after_delay(label):
    time.sleep(3)
    label.place_forget()

def error_sound_not_played(window):
    label = Label(window, text="Error: Sound could not be played", font=("Ubuntu", 15), bg="#09265C", fg='red')
    label.place(x=380 ,y=10)
    threading.Thread(target=lambda: hide_after_delay(label)).start()

def error_sound_unplayable(window):
    label = Label(window, text="Error: Sound unplayable", font=("Ubuntu", 15), bg="#09265C", fg='red')
    label.place(x=380 ,y=10)
    threading.Thread(target=lambda: hide_after_delay(label)).start()

def error_sound_not_added(window):
    label = Label(window, text="Error: Sound not added - file cannot be run", font=("Ubuntu", 15), bg="#09265C", fg='red')
    label.place(x=380 ,y=10)
    threading.Thread(target=lambda: hide_after_delay(label)).start()