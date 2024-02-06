#!/usr/bin/python3
'''
0-read_file module doc
'''


def read_file(filename=""):
    '''
    read_file function doc
    '''
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read())
