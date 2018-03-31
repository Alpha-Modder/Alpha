import os
import sys

from tkinter import*
from tkinter import ttk

def setup():
    global greds

    creds="credfile.tmp"
    if os.path.isfle(creds):
        Login()
    else:
        Signup()

def Signup():
    clear()

    print("Please enter new details :D\n")

    username=input("Enter Username:")
    password=input("enter Password:")
    with open(creds,"w")as f:
        f.write(username)
        f.write("/n")
        f.write(password)
        f.close()

    setup()

def login():
    clear()

    with open (creds) as f:
        data=f.readlines()
        uname=data[0].rstrip()
        pword=data[1].rstrip()

    print("Please Login.\n")
    login=input("Enter Username: ")
    login2=input("Enter Password: ")

    if login == uname and login2 == pword:
        print("\n[+] Logged In.\n")
        sys.exit()
    else:
        print("\n[!] Invalid Login.\n")
        input()
        Login()

    def clear():
        os.system("clear")
        if _name_ == "_main_":
        setup()

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
