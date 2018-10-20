#!/usr/bin/python3

# RPN calculator

# currently just using the python eval() for the math part...

#----------------------------------------

# Modules
import sys

# global stack
stk = []

# lists of commands
coms = ["exit",".","clear","drop","dup","swap"]

#----------------------------------------

# shell loop
def main(argv):
    global stk
    while True:
        txt1 = input("\n>> ")
        txt2 = txt1.split()
        for t in txt2:
            try:
                x = float(t)
                stk.insert(0,x)
            except:
                run(t)

#----------------------------------------

def run(t):
    global stk
    if t in coms:
        cmds(t)
    else:
        calc(t)

#----------------------------------------

def cmds(c):
    global stk
    if c == "exit":
        print("")
        sys.exit()
    elif c == ".":
        show()
    elif c == "clear":
        stk = []
    elif c == "drop":
        if len(stk) > 0:
            stk.pop(0)
        else:
            print("ERROR: stack underflow")
    elif c == "dup":
        if len(stk) > 0:
            stk.insert(0,stk[0])
        else:
            print("ERROR: stack underflow")
    elif c == "swap":
        if len(stk) >= 2:
            a = stk.pop(0)
            b = stk.pop(0)
            stk.insert(0,a)
            stk.insert(0,b)
        else:
            print("ERROR: stack underflow")

#----------------------------------------

def calc(f):
    global stk
    if len(stk) >= 2:
        b = stk.pop(0)
        a = stk.pop(0)
        r = eval(str(a) + str(f) + str(b))
        stk.insert(0,r)
    else:
        print("ERROR: stack underflow")

#----------------------------------------

# stack print
def show():
    global stk
    print("")
    print("data: ",stk)

#========================================
#========================================

if __name__ == '__main__':
    main(sys.argv)

