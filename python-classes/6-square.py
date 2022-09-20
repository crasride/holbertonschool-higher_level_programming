#!/usr/bin/python3
"""Class square that defines a square"""


class Square:
    """Class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Method _init_: Initializes the data.
        size: parametre size the square.
        __size : atrtibute.
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """to retrieve it"""
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) and type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        #   elif(value[0] < 0 or value[1] < 0):
        #    raise TypeError("position must be a tuple of 2 positive integers")
