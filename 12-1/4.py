from tkinter import *
from tkinter.simpledialog import *
window = Tk()
window.geometry("400x400")

label1 = Label(window,text = "val")
label1.pack()

val = askinteger("NUM","1~6",minvalue =1,maxvalue = 6)

label1.configure(text = str(val))
window.mainloop()
