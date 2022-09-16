#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string is None) or type(roman_string) != str:
        return 0
    else:
        list_roman = {'I': 1,
                      'V': 5,
                      'X': 10,
                      'L': 50,
                      'C': 100,
                      'D': 500,
                      'M': 100
                      }
        int_sum = 0
        for i in range(len(roman_string)):
            if (i != (len(roman_string) - 1) and list_roman[roman_string[i]] <
                    list_roman[roman_string[i + 1]]):
                int_sum -= list_roman[roman_string[i]]
            else:
                int_sum += list_roman[roman_string[i]]
        return int_sum
