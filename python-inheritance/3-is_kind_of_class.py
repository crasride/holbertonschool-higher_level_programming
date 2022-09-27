#!/usr/bin/python3
"""
Finds if the object is an instance of, or if the object is an
instance of a class that inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    function returns True if the specified object is of the specified type,
    otherwise False.
    Returns True or False
    """

    return isinstance(obj, a_class)
