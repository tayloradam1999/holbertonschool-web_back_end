#!/usr/bin/env python3
"""
Function <index_range> takes two integer arguments
<page> and <page_size>
"""
from typing import Union, Tuple


def index_range(page: int, page_size: int) -> Union[Tuple[int, int], None]:
    """
    -Returns a tuple of size 2 containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    -Page numbers are 1 -indexed, the first page is page 1.
    """
    if page and page_size:
        return (page * page_size - page_size, page * page_size)
