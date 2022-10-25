#!/usr/bin/python3

"""
Implementation of inheritance
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    Implements a rectangle
    '''

    def __init__(self, width, height):
        """ Initialises parameters"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        """ Specifies how printing instance objects should be"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
