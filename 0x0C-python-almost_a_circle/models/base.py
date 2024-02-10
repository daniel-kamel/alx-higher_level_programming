#!/usr/bin/python3
'''
Base module containing Base class
'''


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
