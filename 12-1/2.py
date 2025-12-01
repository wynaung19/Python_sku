from tkinter import *
from tkinter import messagebox
from time import *

def keyEvent(event):
    #messagebox.showinfo("KeyEvent",'Key : ' + chr(event.keycode))
    messagebox.showinfo("KeyEvent",'Key : ' + event.keysym)

window = Tk()
window.geometry("400x400")
window.bind("<Key>", keyEvent)
window.mainloop()
