#!/usr/bin/python3

"""Square class definintion """





class Square:

    """ Square class defined

        Attributes:

            size (int): Size of square

    """

    def __init__(self, size=0, position=(0, 0)):

        """initializes

        Args:

            size (int): size

            postion(tuple): postion

        Returns:

            None

        """

        self.size = size

        self.position = position



    def area(self):

        """

        set area

        Return:

            area (int)

        """

        return self.__size ** 2



    @property

    def size(self):

        """

        getter of size

        Return:

            Size of square

        """

        return self.__size



    @size.setter

    def size(self, value):

        """

        Setter of size

        Args:

            value (int): size

        Raises

            TypeError: if size is not int

            ValueError: size less than 0

        Returns:

            None

        """

        if type(value) is not int:

            raise TypeError("size must be an integer")

        elif value < 0:

            raise ValueError("size must be >= 0")

        else:

            self.__size = value



    def my_print(self):

        """

        print a square

        Returns:

            None

        """

        if self.size == 0:

            print()

        else:

            print('\n'*self.__position[1], end='')

            for i in range(0, self.__size):

                print(' '*self.__position[0], end='')

                print('#'*self.__size)



    @property

    def position(self):

        """

        get postion attribute

        """

        return self.__position



    @position.setter

    def position(self, value):

        """

            setter of position

        Args:

            value (tuple): position of the square in 2D space

        Returns:

            None

        """

        if len(value) != 2 or type(value) != tuple:

            raise TypeError("position must be a tuple of 2 positive integers")

        if type(value[0]) != int or value[0] < 0:

            raise TypeError("position must be a tuple of 2 positive integers")

        if type(value[1]) != int or value[1] < 0:

            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value
