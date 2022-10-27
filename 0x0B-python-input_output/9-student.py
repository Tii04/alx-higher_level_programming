#!/usr/bin/python3

""" A Class that defines a student.
"""


class Student:
    """ Class represents a student."""

    def __init__(self, first_name, last_name, age):
        """ Initialises parameters"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
