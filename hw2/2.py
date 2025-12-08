import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

window = tk.Tk()
window.title("Tab HW")

notebook = ttk.Notebook(window)

tab1 = tk.Frame(notebook)
tab2 = tk.Frame(notebook)

dog_img = PhotoImage(file="img/dog.png")
cat_img = PhotoImage(file="img/cat.png")

tk.Label(tab1, image=dog_img).pack()
tk.Label(tab2, image=cat_img).pack()

notebook.add(tab1, text="Dog")
notebook.add(tab2, text="Cat")

notebook.pack(expand=True, fill="both")

window.mainloop()
