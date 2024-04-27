#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
from sys import argv


def main():
    """Sends a POST request to the passed URL with the email as a parameter"""
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': argv[1]}
    r = requests.post(url, data=data)
    try:
        js = r.json()
        if len(js) == 0:
            print("No result")
        else:
            print('[{}] {}'.format(js.get('id'), js.get('name')))
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
