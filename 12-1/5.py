from tkinter import *
from tkinter.filedialog import *
window = Tk()
window.geometry("400x400")

label1 = Label(window,text = "path")
label1.pack()

file = askopenfilename(parent = window,filetypes = (("GIF files","*.gif"),("All F","*.*")))

label1.configure(text = str(file))
window.mainloop()
