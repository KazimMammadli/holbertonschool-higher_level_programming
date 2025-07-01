#!/usr/bin/python3
"""
Serialize and deserialize custom Python objects
using the pickle module.
"""
import pickle


class CustomObject:
    """Custom object class"""

    def __init__(self, name, age, is_student):
        """Constructor of class"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """Serialize the file."""
        with open(filename, "wb") as f:
            pickle.dump(self,f)

    @classmethod
    def deserialize(cls, filename):
        """Deserialize the file."""
        with open(filename, "rb") as f:
            return pickle.load(f)
    
    def display(self):
        """Display the contents."""
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")    
