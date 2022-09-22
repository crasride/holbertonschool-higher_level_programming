#!/usr/bin/python3
"""
Prints a text with 2 new lines after each of these characters: ., ? and :
-strip() returns a copy of the string with leading and trailing blank
characters removed
-split() or separate a string into parts
-join() method returns a string in which the string elements of sequence
have been joined by str separator.
"""


def text_indentation(text):
    """ Prints a text with 2 new lines """

    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        for doc in ".:?":
            text = (doc + "\n\n").join([line.strip() for line in text.split(doc)])
            print("{}".format(text), end="")
