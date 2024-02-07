#!/usr/bin/python3
'''
9-student module doc
'''


class Student:
    '''
    Student class doc
    '''
    def __init__(self, first_name, last_name, age) -> None:
        '''
        initializes Student object
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''
        returns object attributes as json-like dictionary
        '''
        items = {}
        for key, value in vars(self).items():
            if key[:2] != '__' and key[-2:] != '__':
                items[key] = value
        return items
