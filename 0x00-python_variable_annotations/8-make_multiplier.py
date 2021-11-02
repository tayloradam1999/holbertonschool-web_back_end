#!/usr/bin/env python3
""" Type-annotated function """


def make_multiplier(multiplier: float) -> float:
    """ Return a function that multiplies its argument by multiplier """
    def multiply(value: float) -> float:
        """ Return the product of value and multiplier """
        return value * multiplier
    return multiply
