#!/usr/bin/python3
""" Real definition of a rectangle  """


class Rectangle:
    """ Initialize Public Class Attribute Number Instance """
    number_of_instances = 0
    """ Initialize Public Class Attribute Print Instance """
    print_symbol = "#"

    """ Definition  Rectangle """
    def __init__(self, width=0, height=0):
        """ increases during each new instance instantiation """
        type(self).number_of_instances += 1
        """ Initialization """
        self.width = width
        self.height = height

    @property
    def height(self):
        """ func private variable height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Value for height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """ func private variable width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Value for width """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """ Public instance method returns rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """ Public instance method that returns rectangle perimeter"""
        if self.__width == 0 or self.height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ should print the rectangle with the character # """
        string = ""
        if self.width == 0 or self.height == 0:
            return string

        for height in range(self.__height):
            for width in range(self.__width):
                # print_symbol for string representation
                string += str(self.print_symbol)
                # print the rectangle with the character #
                # string += "#"
            string += "\n"
        return string[:-1]

    def __repr__(self):
        """ Return string representation rectangle to be able to recreate
        a new instance using eval()"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Decremented when an instance of Rectangle is deleted """
        type(self).number_of_instances -= 1
        """ Use of del method to delete an isntance of a class and print
        a message """
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Static method that returns the biggest rectangle based on the
        area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """ Class Method to Return ne Rectangle instance"""
        return cls(width=size, height=size)
