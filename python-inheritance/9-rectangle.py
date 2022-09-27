#!/usr/bin/python3
""" Classe Rectangle inherits in BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle inherits BaseGeometry """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Rectangle function """
        return self.__height * self.__width

    def __str__(self):
        """ print string function rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
