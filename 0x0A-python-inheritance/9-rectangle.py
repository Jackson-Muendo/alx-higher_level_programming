#!/usr/bin/python3
"""
    7-rectangle: class Rectangle from BaseGeomerty
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Rectangle inherits from BaseGeometry
        Attributes:
            width (int): width of rectangle.
            height (int): height of rectangle.
        Methods:
            __init__ - initialises the Rectangle.
    """
    def __init__(self, width, height):
        """
            initialises Rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
            Returns the area of a rectangle
        """
        area = self.__width * self.__height
        return area

    def __str__(self):
        """
            retruns a string of rectangle details
        """
        return ("[{}] {}/{}".format(type(self).__name__,
                                    self.__width, self.__height))
