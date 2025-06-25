#!/usr/bin/python3
"""This module is used to create rectangle."""


class Rectangle:
    """Define a rectangle with given two parameters."""

    def __init__(self, width=0, height=0):
        """Initialize two parameters."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of rectangle."""
        return self.__height * self.__width

    def perimeter(self):
        """Return the perimeter of rectangle."""
        return (2 * (self.__height + self.__width)
                if self.__width != 0 and self.__height != 0 else 0)
