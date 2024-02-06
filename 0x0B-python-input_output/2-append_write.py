#!/usr/bin/python3
'''
2-append_write module doc
'''


def append_write(filename="", text=""):
    '''
    append_write function doc
    '''
    with open(filename, 'a') as f:
        return f.write(text)
