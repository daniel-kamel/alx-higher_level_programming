#!/usr/bin/python3
'''
9-student module doc
'''
class_to_json = __import__('8-class_to_json').class_to_json


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
        return class_to_json(self)
