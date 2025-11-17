'''
import sys
print(sys.builtin_module_names)
'''
'''
import math
print(dir(math))
'''
import tkinter as tk
from tkinter import simpledialog as d

root = tk.Tk()
root.withdraw()

name = d.askstring("Name","Enter name")
age = d.askinteger("Age","Enter age")

print(f"Name : {name}")
print(f"Age : {age}")

