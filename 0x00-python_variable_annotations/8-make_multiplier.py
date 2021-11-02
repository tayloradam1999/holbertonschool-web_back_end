#!/usr/bin/env python3
""" Type-annotated function """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Return a function that multiplies its argument by multiplier """
    def multiply(number: float) -> float:
        """ Multiply number by multiplier """
        return number * multiplier

    return multiply
