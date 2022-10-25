#!/usr/bin/python3
"""
defining class Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square
    """

    def __init__(self, size):
        """
        Initialises parameters
        """

        self.integer_validator("size", size)
        self.__size = size

        super().__init__(self.__size, self.__size)
