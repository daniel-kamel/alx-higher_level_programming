#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
from sys import argv


def main():
    username = argv[1]
    password = argv[2]
    r = requests.get('https://api.github.com/user', auth=(username, password))
    print(r.json().get('id'))


if __name__ == "__main__":
    main()
