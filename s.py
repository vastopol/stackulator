#!/usr/bin/python3

# RPN calculator

# currently just using the python eval() for the math part...

#----------------------------------------

# Modules
import sys

# global stacks
dstk = []
rstk = []

# lists of commands
coms = ["exit",".","clear",">r","r>","drop","dup","swap"]

#----------------------------------------

# shell loop
def main(argv):
    global dstk
    while True:
        txt1 = input("\n>> ")
        txt2 = txt1.split()
        for t in txt2:
            try:
                x = float(t)
                dstk.insert(0,x)
            except:
                run(t)

#----------------------------------------

def run(t):
    global dstk
    if t in coms:
        cmds(t)
    else:
        calc(t)

#----------------------------------------

def cmds(c):
    global dstk, rstk
    if c == "exit":
        print("")
        sys.exit()
    elif c == ".":
        show()
    elif c == "clear":
        dstk = []
    elif c == ">r":
        if len(dstk) == 0:
            print("Error: stack underflow")
        d = dstk.pop(0)
        rstk.insert(0,d)
    elif c == "r>":
        if len(rstk) == 0:
            print("Error: stack underflow")
        r = rstk.pop(0)
        dstk.insert(0,r)
    elif c == "drop":
        if len(dstk) > 0:
            dstk.pop(0)
        else:
            print("ERROR: stack underflow")
    elif c == "dup":
        if len(dstk) > 0:
            dstk.insert(0,dstk[0])
        else:
            print("ERROR: stack underflow")
    elif c == "swap":
        if len(dstk) >= 2:
            a = dstk.pop(0)
            b = dstk.pop(0)
            dstk.insert(0,a)
            dstk.insert(0,b)
        else:
            print("ERROR: stack underflow")

#----------------------------------------

def calc(f):
    global dstk
    if len(dstk) >= 2:
        b = dstk.pop(0)
        a = dstk.pop(0)
        r = eval(str(a) + str(f) + str(b))
        dstk.insert(0,r)
    else:
        print("ERROR: stack underflow")

#----------------------------------------

# stack print
def show():
    global dstk, rstk
    print("")
    print("D: ",dstk)
    print("R: ",rstk)

#========================================
#========================================

if __name__ == '__main__':
    main(sys.argv)

