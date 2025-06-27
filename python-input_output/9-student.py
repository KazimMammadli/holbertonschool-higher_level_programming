#!/usr/bin/python3
"""Students to JSON."""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Init constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dictionary for json"""
        return self.__dict__
