#!/usr/bin/python3
"""displays the body of the response"""
from urllib import request


def main():
  """displays the body of the response"""
  with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf-8')))


if __name__ == "__main__":
  main()
