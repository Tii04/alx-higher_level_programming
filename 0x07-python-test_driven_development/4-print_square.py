#!/usr/bin/python3

""" Function that prints a square"""


def print_square(size):
    """
    Prints a square using "#"
    Size is of type integer. if non-int entered,
    TypeError raised.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(0, size):
        for j in range(0, size):
            print('#', end="")
        print()
