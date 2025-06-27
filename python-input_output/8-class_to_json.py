#!/usr/bin/python3
"""Module: class to json"""


def class_to_json(obj):
    """Return dictionary of attributes of the object"""
    return obj.__dict__
