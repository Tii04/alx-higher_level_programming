#!/usr/bin/python3

""" Defines a Rectangle
"""


class Rectangle:

    """
    This class represents a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        initilisation of parameters
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Getter Method
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter Method
        """

        if not isinstance(value, int):
            raise TyperError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

        @property
        def height(self):
            """
            Getter Method
            """
            return self.__height

        @height.setter
        def height(self, value):
            """
            Setter Method
            """
            if not isinstance(value, int):
                raise TyperError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value

