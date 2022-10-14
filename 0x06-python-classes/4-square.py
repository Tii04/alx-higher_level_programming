#!/usr/bin/python3

'''Defines a square'''


class Square():

    """Size is the size of a square"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Getter method"""

        return self.__size

    @size.setter
    def size(self, value):
        """Setter method. value should be of type int."""

        if not isinstance(value, int):
            raise TypeError("size must be integer")

        if value < 0:
            raise valueError("size must >= 0")

        self.__size = value

    def area(self):
        return (self.__size * self.__size)
