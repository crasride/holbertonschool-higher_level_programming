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
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """that returns the area value of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character # """
        if self.width == 0 or self.height == 0:
            print("")

        for row in range(0, self.__height):
            for x in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print("")
