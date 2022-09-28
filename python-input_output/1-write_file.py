#!/usr/bin/python3
"""writes a string to a text file (UTF8) and returns the
 number of characters written
"""


def write_file(filename="", text=""):
    """ Write filename"""
    with open(filename, "w", encoding='utf-8') as file:
         return file.write(text)
