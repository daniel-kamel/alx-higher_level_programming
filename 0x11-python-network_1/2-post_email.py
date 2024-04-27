#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""
from urllib import request, parse
from sys import argv


def main():
    """sends a POST request to the passed URL with the email as a parameter"""
    url = argv[1]
    value = {'email': argv[2]}
    data = parse.urlencode(value).encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
