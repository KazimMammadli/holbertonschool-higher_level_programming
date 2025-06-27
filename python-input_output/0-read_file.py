#!/usr/bin/python3
"""This file is used to read another file."""


def read_file(filename=""):
    """Print the contents of file."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
