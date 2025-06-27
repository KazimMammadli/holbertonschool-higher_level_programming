#!/usr/bin/python3
"""This module defines a class"""


class BaseGeometry:
    """Define area function"""

    def area(self):
        """Raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check the passed value"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
