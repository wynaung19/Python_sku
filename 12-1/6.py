from tkinter import *
from tkinter.filedialog import *
window = Tk()
window.geometry("400x400")

file = askopenfilename(parent = window,filetypes = (("GIF files","*.gif"),("All Files","*.*")))

photo = PhotoImage(file = file)
pLabel = Label(window, image = photo)
pLabel.place(x=0,y=0)
window.mainloop()
