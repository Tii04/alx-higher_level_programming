#!/usr/bin/python3

"""Defines a rectangle."""


class Rectangle:
    """
    Represents a new rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Arguments:

        width of type int: width of rectangle
        height of type int: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter method """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter Method"""
        if not isinstance(value, int):
            raise TyperError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter Method"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter Method"""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
