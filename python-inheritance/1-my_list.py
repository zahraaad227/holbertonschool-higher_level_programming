#!/usr/bin/python3
"""This module defines the MyList class that inherits from list."""


class MyList(list):
    """A class that inherits from list with an extra method to print sorted list."""

    def print_sorted(self):
        """Prints the list in ascending sorted order (without modifying original list)."""
        print(sorted(self))
