#!/usr/bin/python3
"""
    2-is_same_class: is_same_class()
"""


def is_same_class(obj, a_class):
    """
        is_same_class returns True if object is an instance of specified class.
        Args:
            obj (object): object being checked.
            a_class (class): class.
        Return: True or False.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
