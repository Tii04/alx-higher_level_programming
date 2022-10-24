#!/usr/bin/python3

"""
Class MyList is subclass of class list
"""


class MyList(list):
    """ This class represents MyList
    """

    def print_sorted(self):
        """
        Function prints a sorted list
        in ascending order, assuming all elements
        of list are of type int.
        """

        print(sorted(self))
