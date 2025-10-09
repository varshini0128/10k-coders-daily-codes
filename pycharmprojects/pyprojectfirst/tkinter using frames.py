
from tkinter import *
from tkinter import Tk,Frame
root = Tk()

newframe = Frame(root)
newframe.pack()

otherframe = Frame(root)
otherframe.pack()

def button(newframe, text, fg):

    button = button(newframe, text="click here", fg="red")

    button = button(newframe, text="click here", fg="blue")

button.pack()


button.pack()


root.mainloop()

