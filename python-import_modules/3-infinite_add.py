#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1
    sum = 0
    if not argc:
        print("0")
    else:
        for i in argv[1:]:
            sum += int(i)
            print("{}".format(sum))
