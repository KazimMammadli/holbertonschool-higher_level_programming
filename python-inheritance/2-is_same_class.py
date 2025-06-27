#!/usr/bin/python3
"""This module defines a function """


def is_same_class(obj, a_class):
    """Returns true if obj is an exact\
          instance of the specified class"""
    return type(obj) is a_class
