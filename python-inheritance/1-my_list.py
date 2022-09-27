#!/usr/bin/python3
""" Write a class MyList that inherits from list """


class MyList(list):    
    """
    Class MyList is a sub class of list.
    """
    def print_sorted(self):
        """
        instance method prints the list sorted(ascending sort)
        """
        print(sorted(self))
