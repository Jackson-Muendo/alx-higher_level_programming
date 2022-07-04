#!/usr/bin/python3
"""
    100-my_int: class MyInt implements int
"""


class MyInt(int):
    """
        MyInt implements int. (inherits from)
    """
    def __init__(self, number):
        self.number = number

    def __ne__(self, value):
        return (self.number == value)

    def __eq__(self, value):
        return (self.number != value)

    def __str__(self):
        return (str(self.number))
