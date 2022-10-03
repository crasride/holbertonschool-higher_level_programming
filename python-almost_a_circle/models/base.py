#!/usr/bin/python3
""" Base class """


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
