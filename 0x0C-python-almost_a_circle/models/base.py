#!/usr/bin/python3
'''
Base module containing Base class
'''
import json


class Base:
    '''
    Base class from which all other classes will be derived
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Initializes objects of the class
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        returns json string representation of list_dictionaries
        '''
        if list_dictionaries is None:
            return '[]'
        else:
            return json.dumps(list_dictionaries)
