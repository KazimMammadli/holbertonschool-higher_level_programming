#!/usr/bin/python3
"""Student to disk and reload."""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Init constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary for json"""
        dictionary = self.__dict__
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {key: dictionary[key] for key in attrs if key in dictionary}
        return dictionary

    def reload_from_json(self, json):
        """Return dict of replaced attributes"""
        for k, v in json.items():
            self.__dict__[k] = v
