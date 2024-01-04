#!/usr/bin/python3
from sys import argv


def main():
    argc = len(argv)

    if argc == 1:
        print("0 arguments.")
        return
    elif argc == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc - 1))

    i = 1
    while i < argc:
        print("{}: {}".format(i, argv[i]))
        i += 1


if __name__ == "__main__":
    main()
