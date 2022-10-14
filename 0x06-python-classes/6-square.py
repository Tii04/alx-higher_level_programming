#!/usr/bin/python3

'''Defines a square'''


class Square():

    """Size is the size of a square"""
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        self.__position = position

    @property
    def size(self):
        """Getter method"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter method. value should be of type int."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise valueError("size must >= 0")

        self.__size = value

    @property
    def position(self):
        """Getter method"""

        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter method"""

        for i in value:
            if (not isinstance(i, int) or
            len(value) != 2 or i < 0):
                raise TyperError("position must be a tuple of 2 positive integers")
            self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print()
        [print() for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print()
