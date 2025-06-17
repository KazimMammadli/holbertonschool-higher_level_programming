#!/usr/bin/python3
import sys
if __name__ == "__main__":
    n = len(sys.argv)- 1
    sum = 0
    for i in range(n):
        sum += int(sys.argv[i+1])
print("{}".format(sum))
