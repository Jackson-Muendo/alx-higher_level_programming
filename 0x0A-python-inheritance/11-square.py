#!/usr/bin/python3
"""
    11-square: class Square from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        Square  inherits from Rectangle
        Attributes:
            size (int): side of square
        Methods:
            __init__ - initialises the square
    """
    def __init__(self, size):
        """
            initialises Square
        """
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """
            Returns the area of square
        """
        area = self.__size * self.__size
        return area

    def __str__(self):
        return ("[{}] {}/{}".format(type(self).__name__,
                                    self.__size, self.__size))
