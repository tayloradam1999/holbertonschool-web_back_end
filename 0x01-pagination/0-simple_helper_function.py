#!/usr/bin/env python3
"""
Function <index_range> takes two integer arguments
<page> and <page_size>
"""
from typing import Union, Tuple


def index_range(page: int, page_size: int) -> Union[tuple[int, int], None]:
    """
    Returns a tuple of size 2 containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.

    Page numbers are 1 -indexed, the first page is page 1.
    """
    if page < 1 or page_size < 1:
        return None
    return (page_size * (page - 1), page_size * page)
