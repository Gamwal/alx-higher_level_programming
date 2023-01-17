#!/usr/bin/python3

from models.base import Base

class Rectangle(Base):


    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        for l in range(self.y):
            print("\n", end='')
        for i in range(self.height):
            for k in range(self.x):
                print(" ", end='')
            for j in range(self.width):
                print("#", end='')
            if j == self.width - 1:
                print("\n", end='')

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        
        if args and len(args) != 0:
            keep = 0
            for arg in args:
                if keep == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif keep == 1:
                    self.width = arg
                elif keep == 2:
                    self.height = arg
                elif keep == 3:
                    self.x = arg
                elif keep == 4:
                    self.y = arg
                keep += 1

        elif kwargs and len(kwargs) != 0:
            for key, arg in kwargs.items():
                if key == 'id':
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif key == 'width':
                    self.width = arg
                elif key == 'height':
                    self.height = arg
                elif key == 'x':
                    self.x == arg
                elif key == 'y':
                    self.y == arg
