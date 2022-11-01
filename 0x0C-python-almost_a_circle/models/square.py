#!/usr/bin/python3
""" Class creates a square, derived from Rectangle."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Derived from Rectangle, class creates
    square."""

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialises parameters"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Format specification"""

        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.height))
