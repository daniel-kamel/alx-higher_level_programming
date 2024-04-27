#!/usr/bin/python3
"""Displays the body of the response and handles error codes"""
from urllib import request, error
from sys import argv


def main():
    """displays the body of the response"""
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))


if __name__ == "__main__":
    main()
