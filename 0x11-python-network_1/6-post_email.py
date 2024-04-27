#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter"""
import requests
from sys import argv


def main():
    """Sends a POST request to the passed URL with the email as a parameter"""
    url = argv[1]
    value = {'email': argv[2]}
    r = requests.post(url, data=value)
    print(r.text)


if __name__ == "__main__":
    main()
