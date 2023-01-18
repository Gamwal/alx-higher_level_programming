#!/usr/bin/python3
"""Square class that inherits from Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the instance of a Square object.

        Args:
            size (int): The size of the square.
            x (int): x-coord of the square.
            y (int): y-coord of the square.
            id (int): instance id of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns [Square] (<id>) <x>/<y> - <size>
        """
        save = f"[Square] ({self.id}) {self.x}/{self.y} - "
        save += f"{self.size}"
        return save

    @property
    def size(self):
        """set/get the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        updates the Rectangle
        Args:
            *args (ints): new attribute values where:
                1st argument should be the id attribute
                2nd argument should be the size attribute
                3rd argument should be the x attribute
                4th argument should be the y attribute
        """
        if args and len(args) != 0:
            cnt = 0
            for arg in args:
                if cnt == 0:
                    if not arg:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif cnt == 1:
                    self.size = arg
                elif cnt == 2:
                    self.x = arg
                elif cnt == 3:
                    self.y = arg
                cnt += 1

        elif kwargs and len(kwargs) != 0:
            for key, arg in kwargs.items():
                if key == "id":
                    if not arg:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif key == "size":
                    self.size = arg
                elif key == "x":
                    self.x = arg
                elif key == "y":
                    self.y = arg

    def to_dictionary(self):
        """Returns dictionary represenation of a Square"""
        return {'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y}
