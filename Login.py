import os
import sys

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
