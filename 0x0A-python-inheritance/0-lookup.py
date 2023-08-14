#!/usr/bin/python3
"""Defines a function that returns a list
of available methods and attributes of an object."""


def lookup(obj):
    """return list of available attributes of object"""
    return dir(obj)
