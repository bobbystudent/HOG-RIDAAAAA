
from tkinter import *

import tkinter.messagebox

root = tkinter.Tk()

root.title(":)")
root.geometry('500x300')

def OnClick():
    for i in range(1000):
        tkinter.messagebox.showinfo("Anti Virus", "Virus detected: \nResolve issue?")

button = Button(root, text="Click me", command=OnClick, height=5, width=10)

button.pack(side='bottom')
root.mainloop()
