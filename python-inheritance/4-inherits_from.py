#!/usr/bin/python3
"""function that returns True if the object is an instance"""


def inherits_from(obj, a_class):
    """function that returns True"""
    obj_class = type(obj)
    return issubclass(obj_class, a_class) and obj_class is not a_class
