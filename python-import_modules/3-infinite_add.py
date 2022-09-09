#!/usr/bin/python3
from sys import argv as a

if __name__ == "__main__":
    ar = len(a) - 1
    r = 0

    if ar > 1:
        for i in range(ar):
            r += int(a[i + 1])
        print(r)
    else:
        print(0)
