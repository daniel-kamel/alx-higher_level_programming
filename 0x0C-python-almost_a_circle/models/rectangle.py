#!/usr/bin/python3
'''
Rectangle module
'''
from models.base import Base


class Rectangle(Base):
    '''
    Rectangle class derived from Base
    '''
    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Initializes objects of the class
        '''
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height

        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x

        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y

    @property
    def width(self):
        '''
        Getter function for width
        '''
        return self.__width

    @width.setter
    def width(self, width):
        '''
        Setter function for width
        '''
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        '''
        Getter function for height
        '''
        return self.__height

    @height.setter
    def height(self, height):
        '''
        Setter function for height
        '''
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        '''
        Getter function for x
        '''
        return self.__x

    @x.setter
    def x(self, x):
        '''
        Setter function for x
        '''
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        '''
        Getter function for y
        '''
        return self.__y

    @y.setter
    def y(self, y):
        '''
        Setter function for y
        '''
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        '''
        Calculates area of rectangle
        '''
        return self.__width * self.__height

    def display(self):
        '''
        displays the rectangle
        '''
        print('\n' * self.__y, end='')
        for _ in range(self.__height):
            print(' ' * self.__x +
                  '#' * self.__width, )

    def __str__(self) -> str:
        '''
        string method for Rectangle objects
        '''
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id, self.__x, self.__y,
            self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        '''
        updates Rectangle attributes
        '''
        if args is None or len(args) == 0:
            self.id = kwargs.get('id', self.id)
            self.__width = kwargs.get('width', self.__width)
            self.__height = kwargs.get('height', self.__height)
            self.__x = kwargs.get('x', self.__x)
            self.__y = kwargs.get('y', self.__y)
        else:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.__width = args[i]
                elif i == 2:
                    self.__height = args[i]
                elif i == 3:
                    self.__x = args[i]
                elif i == 4:
                    self.__y = args[i]
