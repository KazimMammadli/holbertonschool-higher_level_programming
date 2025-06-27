#!/usr/bin/python3
"""Load, add, save."""
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
filename = "add_item.json"
try:
    info = load_from_json_file(filename)
except FileNotFoundError:
    info = []
info[:] += sys.argv[1:]
save_to_json_file(info, filename)
