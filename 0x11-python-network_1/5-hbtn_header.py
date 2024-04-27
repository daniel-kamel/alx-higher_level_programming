#!/usr/bin/python3
"""Displays the value of the variable X-Request-Id in the response header"""
import requests
from sys import argv


def main():
    """
    displays the value of the variable X-Request-Id
    in the response header
    """
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))


if __name__ == "__main__":
    main()
