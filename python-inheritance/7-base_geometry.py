# !/usr/bin/python3
"""This module defines a class"""


class BaseGeometry:
    """Geometry class."""

    def __init__(self):
        """Initialize object."""
        pass

    def area(self):
        """Raise an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the value passed as int."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)
bg.integer_validator("age", 1)



bg.integer_validator("age")
