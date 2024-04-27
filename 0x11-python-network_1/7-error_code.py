#!/usr/bin/python3
"""Displays the body of the response and handles error codes"""
import requests
from sys import argv


def main():
    """displays the body of the response"""
    url = argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print('Error code: {}'.format(r.status_code))
    else:
        print(r.text)


if __name__ == '__main__':
    main()
