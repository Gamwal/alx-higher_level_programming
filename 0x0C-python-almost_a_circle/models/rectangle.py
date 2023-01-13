#!/usr/bin/python3

class Rectangle(Base):

    __width

    def __init__(self, width, height, x=0, y=0, id=None):
        super.__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @setter
    def __width(self, width):
        
