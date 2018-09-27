#!/usr/bin/python3

# Modules
import sys

# function and data stacks
fstk = []
dstk = []

# shell loop
def main(argv):
    global fstk, dstk
    while True:
        txt1 = input(">> ")
        txt2 = txt1.split()
        for t in txt2:
            if t.isdigit():
                dstk.append(t)
            else:
                fstk.append(t)
        print(fstk,dstk)

#----------------------------------------

if __name__ == '__main__':
    main(sys.argv)