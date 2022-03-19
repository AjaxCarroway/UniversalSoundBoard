from tkinter import *
import soundboard_keys

def create_button(window, text: str, locations):
    button = Button(
        master=window, text=text,
        height=2, width=2,
        font=('Helvetica', 20),
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
    keyButtonList = []
    rowCount = 0
    for row in boardList:
        colCount = 0
        for char in row:
            key = soundboard_keys.Key(char)
            key.create_button(window)
            button = key.get_button()
            x_coord = (colCount * 80 + x_win * 0.02 + offset)
            y_coord = (rowCount * 70 + y_win * 0.15)
            button.place(bordermode=OUTSIDE, x=(x_coord), y=(y_coord))
            keyButtonList.append(key)
            colCount += 1
        offset = _get_offset(rowCount, x_win, y_win)
        rowCount += 1
    window.rowconfigure(0, weight=3)
    window.rowconfigure(1, weight=1)
    window.rowconfigure(2, weight=1)
    window.rowconfigure(3, weight=1)
    return keyButtonList


def play_sound():
    pass


def start_window():
    root = Tk()
    
    s_width = root.winfo_screenwidth()
    s_height = root.winfo_screenheight()
    print(s_width, s_height)
    x_win = 1020
    y_win = 350
    

    width_center = int((s_width/2) - (x_win/2))
    height_center = int((s_height/2) - (y_win/2))
    
    root.geometry(f"{x_win}x{y_win}+{width_center}+{height_center}")
    root.resizable(False, False)
    keyButtonList = create_board(root, x_win, y_win)
    root.mainloop()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_window()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

