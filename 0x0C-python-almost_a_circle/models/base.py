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

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        writes the JSON string representation of list_objs to a file
        '''
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]

        with open(f'{cls.__name__}.json', 'w') as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        '''
        returns the list of the JSON string representation json_string
        '''
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
         returns an instance with all attributes already set
         '''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            inst = Rectangle(1, 1)
        elif cls is Square:
            inst = Square(1)
        inst.update(**dictionary)
        return inst
