#!/usr/bin/python3
"""Rectangle class that inherits from Base class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the instance attributes.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): x start location of the rectangle.
            y (int): y start location of the rectangle.
            id (int): Rectangle id.
        Raises:
            TypeError: if any anttribute is not and integer.
            ValueError: if any attribute is less than 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """set/get the width of the new Rectangle"""
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
        """set/get the height of the new Rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """set/get the x-coord of the new Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """set/get the y-coord of the new Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """prints in stdout the rectangle instance with
        the character '#'
        """
        for n in range(self.y):
            print("\n", end='')
        for i in range(self.height):
            for k in range(self.x):
                print(" ", end='')
            for j in range(self.width):
                print("#", end='')
            if j == self.width - 1:
                print("\n", end='')

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        save = f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
        save += f"{self.width}/{self.height}"
        return save

    def update(self, *args, **kwargs):
        """
        Updates the Rectangle

        Args:
            *args (ints): new attribute values where:
                1st argument should be the id attribute
                2nd argument should be the width attribute
                3rd argument should be the height attribute
                4th argument should be the x attribute
                5th argument should be the y attribute
        """
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
            del keep

        elif kwargs and len(kwargs) != 0:
            for key, arg in kwargs.items():
                if key == "id":
                    if not arg:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif key == "width":
                    self.width = arg
                elif key == "height":
                    self.height = arg
                elif key == "x":
                    self.x = arg
                elif key == "y":
                    self.y = arg

    def to_dictionary(self):
        """Returns dictionary represenation of a Rectangle"""
        return {'x': self.x, 'y': self.y,
                'id': self.id, 'height': self.height,
                'width': self.width}
