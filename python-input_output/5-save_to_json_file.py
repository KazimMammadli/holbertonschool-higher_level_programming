#!usr/bin/python3
"""This module is used to save object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """Write object to a text file with the representation
    of JSON"""
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
