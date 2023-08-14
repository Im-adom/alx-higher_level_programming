#!/usr/bin/python3
"""Defines a function that returns True if object is
exactly an instance of specified class; otherwise False."""


def is_same_class(obj, a_class):
    """return True if object is exactly an instance"""
    return True if type(obj) == a_class else False
