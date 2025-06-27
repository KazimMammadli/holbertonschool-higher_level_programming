#!/usr/bin/python3
"""This module is used to write text to the file."""


def write_file(filename="", text=""):
    """Write text to the file and
    return the number of characters."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
