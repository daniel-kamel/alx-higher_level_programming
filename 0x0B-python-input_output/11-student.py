#!/usr/bin/python3
'''
10-student module doc
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

    def to_json(self, attrs=None):
        '''
        returns object attributes as json-like dictionary
        '''
        if attrs is not None:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        '''
        Replaces all attributes of the Student instance
        '''
        for k, v in json.items():
            setattr(self, k, v)
