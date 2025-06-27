#!/usr/bin/python3
"""This module is used to append text in the file."""


def append_write(filename="", text=""):
    """Append text in the file and return
    the number of the characters in the file"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
