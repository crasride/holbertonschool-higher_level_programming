#!/usr/bin/python3
""" class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ 
    Class Rectangle inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Itnitializes a Rectangle
        Args:
        __width -> width
        __height -> height
        __x -> x
        __y -> y
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
