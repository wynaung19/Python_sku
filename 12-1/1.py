from tkinter import *
from time import *

def clickMouse(event):
    txt=''
    if event.num == 1:
        txt += "Left ("
    elif event.num == 3:
        txt += "Right ("

    txt += str(event.y) + "," + str(event.x)+ ")"
    label1.configure(text = txt)

window = Tk()
window.geometry("400x400")
label1 = Label(window,text = "---")
window.bind("<Button>", clickMouse)
label1.pack(expand = 1, anchor = CENTER)
window.mainloop()
