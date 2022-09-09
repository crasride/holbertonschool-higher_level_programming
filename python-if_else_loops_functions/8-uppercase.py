#!/usr/bin/python3
def uppercase(str):
    character = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            character += chr(ord(i) - 32)
        else:
            character += chr(ord(i))
            print("{}".format(character))
