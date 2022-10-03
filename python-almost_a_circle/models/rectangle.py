#!/usr/bin/python3
""" class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Private instance
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

    @property
    def width(self):
        """assign each arguments to right attribute"""
        return self.__width

    @property
    def height(self):
        """assign each arguments to right attribute"""
        return self.__height

    @property
    def x(self):
        """assign each arguments to left attribute"""
        return self.__x

    @property
    def y(self):
        """assign each arguments to left attribute"""
        return self.__y

    @width.setter
    def width(self, value):
        self.__width = value

    @height.setter
    def height(self, value):
        self.__height = value

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value
