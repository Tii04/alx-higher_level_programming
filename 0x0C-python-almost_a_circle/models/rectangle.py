#!/usr/bin/python3

"""
A rectangle class that is a subclass of
Base class.
"""


from models.base import Base


class Rectangle(Base):
    """ Class that represents
    a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialises parameters"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Getter method for width"""

        return self.__width

    @width.setter
    def width(self, value):
        """ Setter method for width"""

        self.valid_attr("width", value)
        self.__width = value

    @property
    def height(self):
        """ Getter method for height"""

        return self.__height

    @height.setter
    def height(self, value):
        """ Setter method for height"""

        self.valid_attr("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter method for x"""

        return self.__x

    @x.setter
    def x(self, value):
        """Setter nethod for x"""

        self.valid_attr("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter method for y"""

        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y"""

        self.valid_attr("y", value)
        self.__y = value

    def area(self):
        """ Calculates area of triangle"""

        return self.width * self.height

    def display(self):
        """ Uses width and height to
        display triangle with '#'"""

        rect = ""
        print('\n' * self.y, end="")
        for h in range(self.height):
            rect += (' ' * self.x) + ('#' * self.width) + '\n'
        print(rect, end="")

    def __str__(self):
        """ Format specification"""

        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute"""
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]

        except IndexError:
            pass

    @staticmethod
    def valid_attr(attr, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(attr))
        if attr == "x" or attr == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attr))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(attr))

    def to_dictionary(self):
        """ Converts to dictionary representation"""

        return {
            "id": getattr(self, "id"),
            "width": getattr(self, "width"),
            "height": getattr(self, "height"),
            "x": getattr(self, "x"),
            "y": getattr(self, "y")
        }
