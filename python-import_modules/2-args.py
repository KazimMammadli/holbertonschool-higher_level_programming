#!/usr/bin/python3
import sys
if __name__ =="__main__":
    n = len(sys.argv ) - 1
    if n > 1:
        print("{} arguments:".format(n))
        for i in range(n):
            print("{}: {}".format(i + 1, sys.argv[i + 1]) )
    elif n == 1:
        print("{} argument:\n1: {}".format(n, sys.argv[1]))
    else:
        print("0 arguments".format())
