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

    limits = '.:?'
    if type(text) is not str:
        raise TypeError("text must be a string")
    for doc in limits:
        text = str(doc + '\n\n').join(b.strip() for b in text.split(doc))
    print(text, end='')
    if len(text) > 0 and text[-1] in limits:
        print('\n')
