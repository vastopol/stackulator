#!/usr/bin/python3

# RPN calculator

# Modules
import sys

# function and data stacks
fstk = []
dstk = []

# shell loop
def main(argv):
    global fstk, dstk
    while True:
        print("")
        txt1 = input(">> ")
        txt2 = txt1.split()
        for t in txt2:
            try:
                x = int(t)
                dstk.append(x)
            except:

                fstk.append(t)
        show()
        calc()
        #show()

def calc():
    global fstk, dstk
    while not len(fstk) == 0:
        if len(dstk) >= 2:
            a = dstk.pop(0)
            b = dstk.pop(0)
            f = fstk.pop(0)
            r = eval(str(a) + str(f) + str(b))
            dstk.insert(0,r)
            show()
        else:
            return

# stack print
def show():
    global fstk, dstk
    print("")
    print("func: ",fstk)
    print("data: ",dstk)

#----------------------------------------

if __name__ == '__main__':
    main(sys.argv)