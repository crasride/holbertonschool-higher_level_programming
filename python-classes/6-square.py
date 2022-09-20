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
        if (type(self.__size) is not int):
            raise TypeError("size must be an integer")
        if (self.__size < 0):
            raise ValueError("size must be >= 0")

        if type(self.__position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(self.__position[0]) and type(self.__position[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (self.__position[0] < 0 or self.__position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """to set it"""
        self.__size = value
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")

        def area(self):
            return (self.__size*self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")

        else:
            for i in range(self.__position[1]):
                print()
            for y in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                    for z in range(self.__size):
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
        elif (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
