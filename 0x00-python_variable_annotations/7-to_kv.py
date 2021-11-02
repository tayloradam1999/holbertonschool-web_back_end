#!/usr/bin/env python3
""" Type-annotated function """


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[int, float]]:
    """
    Convert key-value pair to tuple
    :param k: key
    :param v: value
    :return: tuple
    """
    return k, v
