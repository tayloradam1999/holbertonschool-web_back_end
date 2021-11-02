#!/usr/bin/env python3
""" Type-annotated function """


from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Takes a list of floats as argument and returns sum as float """
    return sum(input_list)
