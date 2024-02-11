#!/usr/bin/python3
'''
Square module
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    Square class derived from Rectangle
    '''
    __nb_objects = 0

    def __init__(self, size, x=0, y=0, id=None):
        '''
        Initializes objects of the class
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        '''
        string method for Square objects
        '''
        return '[Square] ({}) {}/{} - {}'.format(
            self.id, self.x, self.y, self.height)
