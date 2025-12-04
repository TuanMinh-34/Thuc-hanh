
from tkinter import *
from tkinter import messagebox

def NewFile():
    messagebox.showinfo("New File", "New File!")

def OpenFile():
    messagebox.showinfo("Open File", "Open File!")

def Exit():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        root.quit()

def About():
    messagebox.showinfo("About", "This is a simple example of a menu")

def InsText():
    messagebox.showinfo("Insert Text", "Insert Text!")

def InsPic():
    messagebox.showinfo("Insert Picture", "Insert Picture!")

root = Tk()
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Exit)

editmenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Insert Text", command=InsText)
editmenu.add_command(label="Insert Picture", command=InsPic)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

mainloop()
