#!/usr/bin/python3
""" Class creates a square, derived from Rectangle."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Derived from Rectangle, class creates
    square."""

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialises parameters"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter method for size"""

        return self.width

    @size.setter
    def size(self, value):
        """ Setter method for size"""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Assigns attributes"""

        if len(args):
            for count, ele in enumerate(args):
                if count == 0:
                    self.id = ele
                elif count == 1:
                    self.size = ele
                elif count == 2:
                    self.x = ele
                elif count == 3:
                    self.y = ele
        else:
            for key, val in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, val)

    def to_dictionary(self):
        """ Dictionary representation"""

        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """ Format specification"""

        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.height))
