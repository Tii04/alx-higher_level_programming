#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    number_of_instances = 0   # Class attribute
    print_symbol = "#"        # Class attribute

    @classmethod
    def square(cls, size=0):
        """
        Creates new rectangle instance
        """
        return cls(size, size)

    def __init__(self, width=0, height=0):
        """
        Initialising a new Rectangle.

        Arguements:

        width of type int: width of the new rectangle.
        height of type int: height of the new rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        prints a rectangle with "#" symbol using
        width and height.
        """
        rect_str = ""
        if self.__width == 0 or self.__height == 0:
            return ""

        for h in range(0, self.__height):
            rect_str += str(self.print_symbol) * self.__width
            if h + 1 < self.height:
                rect_str += "\n"
        return rect_str

    def __repr__(self):
        """
        Prints string representation of rectangle
        """
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return rect

    def __del__(self):
        """
        Prints message when instance is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) == Rectangle.area(rect_2):
            return rect_1
        if Rectangle.area(rect_1) > Rectangle.area(rect_2):
            return rect_1
        if Rectangle.area(rect_1) < Rectangle.area(rect_2):
            return rect_2
