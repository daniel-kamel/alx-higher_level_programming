#!/usr/bin/python3
"""displays the X-Request-Id"""
from urllib import request
from sys import argv


def main():
    """displays the X-Request-Id"""
    with request.urlopen(argv[1]) as response:
        print(response.getheader('X-Request-Id'))


if __name__ == '__main__':
    main()
