import tkinter as tk

from tkinter import *

root = Tk()
root.title("text editor")
root.geometry("350x500")


text=Text(root)
text.grid()

root.mainloop()