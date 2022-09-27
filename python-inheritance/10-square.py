#!/usr/bin/python3
""" Creates a Square class """


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Private instance attribute size.
    Inherits from Rectangle
    Public method area()
    """

    def __init__(self, size):
        """Initializes a Square / size of the square """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return super().__str__()

    def area(self):
        """ print area """
        return self.__size ** 2
