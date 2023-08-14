#!/usr/bin/python3
"""The class MyList inherits from list"""


class MyList(list):
    """Inheriting from list"""
    def print_sorted(self):
        """that prints the list, but sorted (ascending sort)"""
        print(sorted(self))
