#!/usr/bin/python3
'''
1-write_file module doc
'''


def write_file(filename="", text=""):
    '''
    write_file function doc
    '''
    with open(filename, 'w') as f:
        return f.write(text)
