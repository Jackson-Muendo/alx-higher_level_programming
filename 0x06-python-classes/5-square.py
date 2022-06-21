#!/usr/bin/python3
""" defines a square with size"""


class Square:
    """ defines a square with size
        Attributes:
        size (int): size of square
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """ Square area """
        A = self.__size * self.__size
        return (A)

    @property
    def size(self):
        """getter def"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        """print def"""
        if self.__size == 0:
            print('')
        else:
            for i in range(0, self.__size):
                for i in range(0, self.__size):
                    print('#', end='')
                print('')
