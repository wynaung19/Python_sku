from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("WaiYan")
window.geometry("400x400")
'''
window.resizable(width = True,height=True)
label1 = Label(window,text = "I'm")
label2 = Label(window,text = "Wai Yan Naung",font = ("Comic Sans MS",30),fg = "blue")
label3 = Label(window,text = "waiyannaung.com",bg="light cyan",width=20,height=5,anchor = SE)

label1.pack()
label2.pack()
label3.pack()

photo1 = PhotoImage(file = "GIF/dog.gif")
label1 = Label(window,image = photo1)
photo2 = PhotoImage(file = "GIF/cat.gif")
label2 = Label(window,image = photo2)

label1.pack(side="left")
label2.pack()
def myFun():
    messagebox.showinfo("Text","Desccccc")

btn1 = Button(window,text = "callfun",fg = "cyan4",command = myFun)

'''
'''
def myFunc():
    if chk.get() == 0:
        messagebox.showinfo("","0")
    else:
        messagebox.showinfo("","1")
chk = IntVar()
cb1 = Checkbutton(window,text="Checkbox",variable = chk,command = myFunc)
cb1.pack()

def lan():
    if l.get() == 1 :
        label1.configure(text = "Python")
    elif l.get() == 2:
        label1.configure(text = "C")
    else:
        label1.configure(text = "Java")

l = IntVar()

rb1 = Radiobutton(window,text = "Python",variable = l, value=1,command=lan)
rb2 = Radiobutton(window,text = "C",variable = l, value=2,command=lan)
rb3 = Radiobutton(window,text = "Java",variable = l, value=3,command=lan)
rb1.pack()
rb2.pack()
rb3.pack()
label1 = Label(window,text="Selected Lang",fg="midnight blue")
label1.pack()

btnl = [None] *3
for i in range(0,3):
    btnl[i] = Button(window,text = "BTN"+str(i+1))

for btn in btnl:
    btn.pack(side = RIGHT)
'''
def cl(e):
    messagebox.showinfo("CL","Left")
def cr(e):
    messagebox.showinfo("CR","Right")

window.bind("<Button-1>",cl)
pic = PhotoImage(file="GIF/rabbit.gif")
label = Label(window,image = pic)
label.bind("<Button-3>",cr)
label.pack(expand = 1, anchor = CENTER)
window.mainloop()
