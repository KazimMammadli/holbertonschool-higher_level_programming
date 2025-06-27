#!/usr/bin/python3
"""This module is about deserialization"""
import json


def from_json_string(my_str):
    """JSON to string"""
    return json.loads(my_str)
