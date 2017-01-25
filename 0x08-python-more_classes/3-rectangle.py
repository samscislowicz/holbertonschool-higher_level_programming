#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if type(width) != int:
                raise TypeError('width must be an integer')
            if width < 0:
                raise ValueError('width must be >= 0')

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if type(height) != int:
                raise TypeError('height must be an integer')
            if height < 0:
                raise ValueError('height must be >= 0')

    def area(self):
        return int(self.width) * int(self.height)

    def perimeter(self):
        if int(self.width) <= 0 or int(self.height) <= 0:
            return 0
        return (int(self.width) + int(self.height)) * 2

    def __str__(self):
        st = ""
        if (self.width == 0) or (self.height == 0):
            return st
        for h in range(self.height):
            for w in range(self.width):
                st += "#"
            st += "\n"
        st = st[:-1]
        return st
