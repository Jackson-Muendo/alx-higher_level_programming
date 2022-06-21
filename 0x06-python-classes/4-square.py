#!/usr/bin/python3
"""create an empty class called Square"""


class Square:
    """create a square.
    size (no type/value verification)
    atributes:
    size: private instance.
    """

    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
