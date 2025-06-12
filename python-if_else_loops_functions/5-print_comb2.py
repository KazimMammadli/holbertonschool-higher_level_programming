#!/usr/bin/python3
str = ""
for i in range(100):
    str += f"{i:02d}"
    if i != 99:
        str += ", "
    else:
        pass
print("{}".format(str))
