#!/usr/bin/python3
"""Class square that defines a square"""


class Square:
    """Class Square"""
    def __init__(self, size=0):
        """
        Method _init_: Initializes the data.
        size: parametre size the square.
        __size : atrtibute.
        """
        self.__size = size
        if (type(self.__size) != int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        returns the current square area.
        """
        return (self.__size ** 2)
