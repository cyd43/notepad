import tkinter as tk
from tkinter import *

root = Tk()
root.title("text editor")
root.geometry("350x500")

#Ag file button function
def new_file():
    print("new_file")

def open_file():
    print("open_file")

def save_file():
    print("save_file")

#frame sa text and scrollbar
text_frame = Frame(root, relief="groove")
text_frame.pack(fill="both", expand=True)

#scrollbuttonbar
scrollbar = Scrollbar(text_frame)
scrollbar.pack(side="right", fill="y")

#text
text_area=Text(text_frame, bg="lightgrey")
text_area.pack(side="left" ,fill="both", expand=True)

text_area.insert("1.0", "Hello\n" * 50) #test

text_area.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_area.yview)

#menu
menu = tk.Menu(root)
root.config(menu=menu)

#file menu
filemenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

#edit menu
editmenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=editmenu)

editmenu.add_command(label="Undo")
editmenu.add_command(label="Redo")
editmenu.add_command(label="dunno")


#help menu
helpmenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About")

#mga function

root.mainloop()