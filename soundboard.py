from tkinter import *
from PIL import ImageTk, Image
from pygame import mixer
from pynput import keyboard
import soundboard_errors
import soundboard_helper
from pynput.keyboard import Key, Listener
import soundboard_keys
import multiprocessing as mp


def create_button(window, text: str, locations):
    button = Button(
        master=window, text=text,
        height=2, width=2,
        font=('Ubuntu', 20),
        command=play_sound)
    return button


def _get_offset(row: int, x_win, y_win):
    offset = 0
    row += 1
    if row == 1:
        offset = 40
    elif row == 2:
        offset = 60
    elif row == 3:
        offset = 100
    return offset


def create_board(window, x_win, y_win):
    offset = 0
    boardList = ["1234567890-=", "QWERTYUIOP[]", "ASDFGHJKL;'", "ZXCVBNM,./"]
    keyDict = {}
    keyButtonList = []
    rowCount = 0
    for row in boardList:
        colCount = 0
        for char in row:
            key = soundboard_keys.Key(char, window)
            key.create_button(window)
            button = key.get_button()
            label = key.get_label()
            x_coord = (colCount * 80 + x_win * 0.02 + offset)
            y_coord = (rowCount * 80 + y_win * 0.15)
            button.place(bordermode=OUTSIDE, x=(x_coord), y=(y_coord))
            label.place(x=(x_coord), y=(y_coord-10))
            keyButtonList.append(key)
            keyDict[char.lower()] = key
            colCount += 1
        offset = _get_offset(rowCount, x_win, y_win)
        rowCount += 1
    return keyButtonList, keyDict


def on_press(key, keyDict, window):
    acceptable_keys = "1234567890-=qwertyuiop[] asdfghjkl;zxcvbnm,./"
    letter = str(key)[1:2]
    if key == Key.space:
        try:
            mixer.stop()
        except:
            pass
    if len(str(key)) > 3:
        return
    if letter not in acceptable_keys:
        return
    try:
        keyDict[letter].play_sound()
    except:
        soundboard_errors.error_sound_not_played(window)

def start_window():
    root = Tk()
    root.configure(bg='#09265C')
    s_width = root.winfo_screenwidth()
    s_height = root.winfo_screenheight()
    x_win = 1020
    y_win = 400
    # root.bind("<space>", soundboard_helper.end_mixer())
    width_center = int((s_width / 2) - (x_win / 2))
    height_center = int((s_height / 2) - (y_win / 2))
    root.geometry(f"{x_win}x{y_win}+{width_center}+{height_center}")
    # root.resizable(False, False)
    keyButtonList, keyDict = create_board(root, x_win, y_win)
    soundboard_helper.create_save_file(keyDict)
    keyDict = soundboard_helper.update_labels(root, keyDict)
    print(keyDict['2'].get_soundfile())
    listener = keyboard.Listener(
        on_press=lambda event: on_press(event, keyDict, root))
    listener.start()
    root.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_window()
