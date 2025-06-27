#!/usr/bin/python3
"""This module defines a class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    "Square class"

    def __init__(self, size):
        """Constructor of square class"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of square"""
        return self.__size ** 2
