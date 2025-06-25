#!/usr/bin/python3
"""This module is used to create rectangle."""


class Rectangle:
    """Define a rectangle with given two parameters."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize two parameters and increase\
            the number of instances by 1."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """Return rectangle with the character #."""
        return ("\n".join(str(self.print_symbol)
                          * self.__width for _ in range(self.__height))
                if self.__width > 0 and self.__height > 0 else "")

    def __repr__(self):
        """Return rectangle dimensions."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Delete the instance and decrease\
            the number of instances by 1."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Check if rectangles are instances of Rectangle class
        and return the one with bigger area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() > rect_2.area() else rect_2
