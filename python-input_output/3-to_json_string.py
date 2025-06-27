#!/usr/bin/python3
import json
"""This module is about serialization"""


def to_json_string(my_obj):
    """Return the JSON representation of an object"""
    return json.dumps(my_obj)
