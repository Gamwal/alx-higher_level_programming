#!/usr/bin/python3
"""
Student class that defines student by
    first_name
    last_name
    age
"""


class Student:
    """
    Student class object
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def __dict__(self):
        return {'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age}

    def to_json(self, attrs=None):
        """Public method to retrieve a dict representation of object"""
        if attrs is None:
            return self.__dict__
        elif attrs is not None and type(attrs) == list:
            for attr in attrs:
                if type(attr) != str:
                    return self.__dict__
        new_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dict[key] = value
        return new_dict

    def reload_from_json(self, json):
        """Public method to replace all attributes of student"""
        for key, value in self.__dict__.items():
            delattr(self, key)
        for key, value in json.items():
            setattr(self, key, value)
