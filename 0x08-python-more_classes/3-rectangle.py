#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """
        Initialising a new Rectangle.

        Arguements:

        width of type int: width of the new rectangle.
        height of type int: height of the new rectangle.
        """
        self.width = width
        self.height = height

    def __str__(self):
        """
        prints a rectangle with "#" symbol using
        width and height.
        """
        rect = []
        if self.__width == 0 or self.__height == 0:
            return ("")

        for h in range(0, self.__height):
            for w in range(0, self.__width):
                rect.append("#")
            if h != self.height - 1:
                rect.append("\n")
        return ("".join(rect))

    @property
    def width(self):
        """Gette method of width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Setter method for height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates area of rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Calculates perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.height)
