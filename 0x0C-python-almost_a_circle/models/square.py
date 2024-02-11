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

    @property
    def size(self):
        '''
        getter function for size'''
        return self.width

    @size.setter
    def size(self, size):
        '''
        Setter function for size
        '''
        if not isinstance(size, int):
            raise TypeError('width must be an integer')
        if size <= 0:
            raise ValueError('width must be > 0')
        self.width = size
        self.height = size
