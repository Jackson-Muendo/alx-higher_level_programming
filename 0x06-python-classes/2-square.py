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
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
