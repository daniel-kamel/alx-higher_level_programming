#!/usr/bin/python3
'''
6-load_from_json_file module doc
'''
import json


def load_from_json_file(filename):
    '''
    load_from_json_file function doc
    '''
    with open(filename, 'r') as f:
        return json.load(f)
