#!/usr/bin/env python3
""" Type-annotated function """


from typing import List


def sum_mixed_list(mxd_list: List[float, int]) -> float:
    """ Returns the sum of all ints and floats from passed list """
    sum_ = 0.0
    for item in mxd_list:
        sum_ += item
    return sum_
