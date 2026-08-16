import tkinter as tk

from tkinter import *

root = Tk()
root.title("text editor")
root.geometry("350x500")

#save button function
def new_file():
    print("new_file")

def open_file():
    print("open_file")

def save_file():
    print("save_file")



text=Text(root, height=50, width=43)
text.grid(row=0, column=0)

menu = tk.Menu(root)
root.config(menu=menu)

filemenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About")

#mga function

root.mainloop()