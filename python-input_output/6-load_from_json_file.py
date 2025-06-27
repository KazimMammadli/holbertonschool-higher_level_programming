#!/usr/bin/python3
"""About json files"""
import json


def load_from_json_file(filename):
    """Create object from a JSON file """
    with open(filename, "r") as f:
        obj = json.load(f)
