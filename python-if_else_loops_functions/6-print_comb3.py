#!/usr/bin/python3
str = ""
for i in range(100):
    num = f"{i:02d}"
    if num[::-1] not in str and num[0] != num[1]:
        str += num
        if i != 99:
            str += ", "
print("{}".format(str[:-2]))
