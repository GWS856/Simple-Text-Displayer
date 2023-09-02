import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Text Displayer by GWS")
root.geometry("230x130")

var = tk.StringVar(root)

def enterdata():
    info = e1.get() 
    var.set(info)
label1 = tk.Label(root, textvariable=var)
label1.grid(row=0, column=0)

var.set("Default Text")
label = tk.Label(root, textvariable=var)
label.grid(row=0, column=0)

e1 = tk.Entry(root, bd=0)
e1.grid(row=1, column=0)

bt1 = tk.Button(root, bg='light gray', fg='black', text='Display Text', command=enterdata)
bt1.grid(row=2, column=0)

root.mainloop()