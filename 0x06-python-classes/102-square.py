#!/usr/bin/python3
"""Node  class definintion """


class Square:
    """creates a square and determines area"""
    def __init__(self, size=0):
        """initializes square
        Args:
            size: size of square"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """determines area of square"""
        res = self.__size ** 2
        return(res)

    @property
    def size(self):
        """gets size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def __eq__(self, other):
        """check if equal to another square"""
        return(self.area() == other.area())

    def __lt__(self, other):
        """check if less than other square"""
        return(self.area() < other.area())

    def __le__(self, other):
        """check if less than or equal to other square"""
        return(self.area() <= other.area())

    def __ne__(self, other):
        """check if not equal to another suqare"""
        return(self.area() != other.area())

    def __gt__(self, other):
        """check if greater than another square"""
        return(self.area() > other.area())

    def __ge__(self, other):
        """check if greater than or equal to another square"""
        return(self.area() >= other.area())
