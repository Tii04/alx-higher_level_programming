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

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation"""

        buf = []

        if json_string is None or len(json_string) == 0:
            return buf
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
            Returns an instance with all the attributes already set
        '''
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            r2 = Rectangle(3, 8)
        elif cls.__name__ == "Square":
            r2 = Square(5)
        r2.update(**dictionary)
        return (r2)

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
