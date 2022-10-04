#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializer square class """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Returns size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size """
        self.width = value
        self.height = value

    def __str__(self):
        """method should return """
        str = "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.width)
        return str

    def update(self, *args, **kwargs):
        """
        args is the list of arguments - no-keyworded arguments
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        """
        l_attribute = ["id", "size", "x", "y"]
        for attribute, arg in zip(l_attribute, args):
            setattr(self, attribute, arg)
# setattr sets the value of the specified attribute of the specified object
# zip eturns an iterator of tuples based on the iterable objects
        for key, value in kwargs.items():
            setattr(self, key, value)
# itemsreturns view object contains the key-value pairs of the dict,tuples,list
