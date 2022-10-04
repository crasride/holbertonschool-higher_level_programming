#!/usr/bin/python3
""" Base class """
import json


class Base():
    """private class attribute """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize id, increment class attribute __nb_objects if there is
        no id and set it as id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
