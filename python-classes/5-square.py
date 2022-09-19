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

    @property
    def size(self):
        """to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """to set it"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        returns the current square area.
        """
        return (self.__size*self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for row in range(self.__size):
                for column in range(self.__size):
                    print("#", end="")
                print()
