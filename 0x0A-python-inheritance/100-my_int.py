#!/usr/bin/python3
"""MyInt class that inverts == and != inverted"""


class MyInt(int):
    """MyInt class object that inherits from int"""
    def __init__(self, value):
        """Init method of the """
        super().__init__()

    def __eq__(self, obj):
        """inerse of normal __eq__ method"""
        if super().__eq__(obj):
            return False
        else:
            return True

    def __ne__(self, obj):
        """inerse of normal __ne__ method"""
        if super().__ne__(obj):
            return False
        else:
            return True
