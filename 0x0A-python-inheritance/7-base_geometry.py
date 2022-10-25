#!/usr/bin/python3
"""
Class that defines a geometry module
"""


class BaseGeometry():
    """
    Class that represents a geometry module
    """

    # def __init__(self, name, value):
    #   """
    #   Initialising parameters
    #    """

    #   self.name = name
    #   self.value = value */

    def area(self):
        """
        Function that raises exception error
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        function that validates the value.
        Value has to be int, name must be a string
        greater than 0. Otherwise exception raised.
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
