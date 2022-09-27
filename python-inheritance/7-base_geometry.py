#!/usr/bin/python3
"""
Create an empty class BaseGeometry
"""


class BaseGeometry:
    """
    public instance method
    """
    def area(self):
        """
        Raises an Exception with the message
        'area() is not implemented'.
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ public instance validate value """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
