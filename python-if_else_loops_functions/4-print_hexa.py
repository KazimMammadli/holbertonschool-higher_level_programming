#!/usr/bin/python3
str = ""
for i in range(99):
    str += f"{i} = {hex(i)}\n"
#print("{}".format(str.rstrip()))
print("{}".format(str), end="")
