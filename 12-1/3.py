from tkinter import *
from tkinter import messagebox
window = Tk()

mainMenu = Menu(window)
window.config(menu = mainMenu)

def fun_open():
    messagebox.showinfo("Menu","OPEN")
def fun_exit():
    window.quit()
    window.destroy()

fileMenu = Menu(mainMenu,tearoff = 0)
mainMenu.add_cascade(label = "File",menu = fileMenu)
fileMenu.add_command(label = "Open",command = fun_open)
fileMenu.add_separator()
fileMenu.add_command(label = "Exit",command = fun_exit)

window.geometry("400x400")
window.mainloop()
