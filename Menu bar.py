from tkinter import*
from tkinter import ttk

def save():
    save()
    
def save2():
    Save()
    
def shutdown():
    shutdown()
    
def undo():
    undo()
    
def redo():
    redo()

root=Tk()
root.title("Alpha")


menubar=Menu(root)

filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="Speichern",command=save)
filemenu.add_command(label="Speichern unter",command=save2)
filemenu.add_separator()
filemenu.add_command(label="Programm beenden",command=shutdown)
menubar.add_cascade(label="Datei", menu=filemenu)

editmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label="Rückgangig",command=undo)
editmenu.add_separator()
editmenu.add_command(label="Wiederholen",command=redo)
menubar.add_cascade(label="Bearbeiten", menu=editmenu)

root.config(menu=menubar)

root.mainloop()
