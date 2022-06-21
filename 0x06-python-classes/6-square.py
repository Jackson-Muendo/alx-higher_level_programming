#!/usr/bin/python3
"""create an empty class called Square"""


class Square:
    """create a square.
    size (no type/value verification)
    atributes:
    size: private instance.
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) != tuple or len(value) != 2 or
                value[0] < 0 or type(value[0]) != int or
                type(value[1]) != int or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for y in range(self.__position[1]):
            print()
        for h in range(self.__size):
            for p in range(self.__position[0]):
                print(" ", end="")
            for w in range(self.__size - 1):
                print('#', end="")
            print('#')
