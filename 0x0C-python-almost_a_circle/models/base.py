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

    @classmethod
    def save_to_file(cls, list_objs):
        """ JSON representation to a file"""

        buf = []
        file_name = cls.__name__ + ".json"

        if list_objs is not None:
            for item in list_objs:
                item = item.to_dictionary()
                json_dictionary = json.loads(cls.to_json_string(item))
                buf.append(json_dictionary)
        with open(file_name, mode="w") as file:
            return json.dump(buf, file)
