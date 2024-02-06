#!/usr/bin/python3
'''
5-save_to_json_file module doc
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    save_to_json_file function doc
    '''
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
