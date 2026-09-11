import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("text editor")
root.geometry("350x500")

current_file = None

#============frame sa text and scrollbar===========
text_frame = tk.Frame(root, relief="groove")
text_frame.pack(fill="both", expand=True)

#===========scrollbuttonbar
scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side="right", fill="y")

#============text
text_area = tk.Text(text_frame, bg="lightgrey") # test background to lightgrey
text_area.pack(side="left" ,fill="both", expand=True)

text_area.insert("1.0", "hello\n" * 100) #test 100 hello

text_area.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_area.yview)




#=================Ag file button function===========
def new_file():
    global current_file

    text_area.delete("1.0", tk.END)
    print("new_file") #Testing==========================

    current_file = None

    root.title("Untitled - text editor")

def open_file():
    global current_file
    file_path = filedialog.askopenfilename(
        filetypes=[
            ("Text_Files", "*.txt"),
            ("All Files", "*.*")
        ]
    )

    if file_path:
        with open(file_path, "r") as f:
            content = f.read()

        text_area.delete("1.0", tk.END)
        text_area.insert("1.0", content)

        current_file = file_path

        root.title(f"{current_file} - text editor")

def save_file():
    global current_file

    if current_file is None:
        current_file = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[
                ("Text Files", "*.txt"),
                ("All Files", "*.*")
            ]
        )

        if not current_file:
            return

    content = text_area.get("1.0", tk.END)

    with open(current_file, "w") as f:
        f.write(content)

    root.title(f"{current_file} - text editor")

#====================EDIT========================

def font_menu():
    text_area.config(font="Courier") #test===================================


#=============menu
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
editmenu.add_separator()
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_separator()
editmenu.add_command(label="Font", command=font_menu)


#help menu
helpmenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About")

#mga function

root.mainloop()