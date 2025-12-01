from tkinter import *
from tkinter.filedialog import *
import webbrowser

window = Tk()
window.geometry("400x400")

mainMenu = Menu(window)
window.config(menu = mainMenu)

def fun_open():
    filepath = askopenfilename(parent = window,filetypes = (("GIF files","*.gif"),("All Files","*.*")))
    photo = PhotoImage(file = filepath)
    pLabel.configure(image = photo)
    pLabel.image = photo
def fun_exit():
    window.quit()
    window.destroy()

def fun_cont():
    webbrowser.open("https://waiyannaung.com/")

photo = PhotoImage()
pLabel = Label(window,image = photo)
pLabel.pack(expand = 1, anchor = CENTER)

fileMenu = Menu(mainMenu,tearoff = 0)
mainMenu.add_cascade(label = "File",menu = fileMenu)
fileMenu.add_command(label = "Open",command = fun_open)
fileMenu.add_separator()
fileMenu.add_command(label = "Exit",command = fun_exit)
fileMenu.add_separator()
fileMenu.add_command(label = "Contact",command = fun_cont)

window.mainloop()
