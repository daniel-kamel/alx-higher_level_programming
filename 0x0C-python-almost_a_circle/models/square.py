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

    def update(self, *args, **kwargs):
        '''
        updates Square object
        '''
        if args is None or len(args) == 0:
            self.id = kwargs.get('id', self.id)
            self.width = kwargs.get('size', self.width)
            self.height = kwargs.get('size', self.height)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)
        else:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                    self.height = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]

    def to_dictionary(self):
        '''
        returns the dictionary representation of a Square
        '''
        result = super().to_dictionary()
        result.pop('height')
        result['size'] = result.pop('width')
        return result
