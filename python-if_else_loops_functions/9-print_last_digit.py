#!/usr/bin/python3
def print_last_digit(number):
    l_dig = number % 10 if number > 0 else ((-number) % 10)
    print(l_dig, end="")
    return(l_dig)
