#!/usr/bin/python3
"""Defines a function that adds a new attribute
to an object if possible"""


def add_attribute(obj, attribute, value):
    """Adds a new attribute"""
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    if '__slots__' in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attribute, value)
