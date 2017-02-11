#!/usr/bin/env python

if __name__ == "__main__":
    print("My First python")
else:
    print("This is a module")

def clear():
    name = os.name
    if(name == "nt"):
        clear = os.system("clear")
    else:
        clear = os.system("cls")


