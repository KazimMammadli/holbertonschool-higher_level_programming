#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for char in str:
        if 97 <= ord(char) <= 122:
            char = chr(ord(char) - 32)
            new_str += char
        else:
            new_str += char
    print(new_str)
