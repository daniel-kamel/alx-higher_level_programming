#!/usr/bin/python3
'''
8-class_to_json module doc
'''


def class_to_json(obj):
    '''
    class_to_json function doc
    '''
    items = {}
    for key, value in vars(obj).items():
        if key[:2] != '__' and key[-2:] != '__':
            items[key] = value
    return items
