#!/usr/bin/python3

"""
This is the base class.
"""

import json


class Base():
    """
    This class manages the id attribute.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialises parameters"""

        if id is not None:
            self.id = id

        else:
            Base. __nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON representation of list_dictionaries"""

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
