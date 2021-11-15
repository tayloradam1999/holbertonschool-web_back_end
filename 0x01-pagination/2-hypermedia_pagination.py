#!/usr/bin/env python3
"""
Function <index_range> takes two integer arguments
<page> and <page_size>
"""
from typing import Union, Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Union[Tuple[int, int], None]:
    """
    -Returns a tuple of size 2 containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    -Page numbers are 1 -indexed, the first page is page 1.
    """
    if page and page_size:
        return (page * page_size - page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        -Uses assert to verify that both arguments are ints > 0
        -Uses index_range to find correct indexes to paginate the dataset
        and return the appropriate page of the dataset (i.e. the list of rows)
        -Return an empty list if passed arguments are out of range
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)

        if start >= len(self.dataset()):
            return []

        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """
        Returns a dictionary containing the following key-value pairs:
        -page_size: the length of the returned dataset page
        -page: the current page number
        -data: the dataset page (equivalent to return from previous task)
        -next_page: number of the next page, None if no next page
        -prev_page: number of the previous page, None if no previous page
        -total_pages: the total number of pages in the dataset as an integer
        Make sure to reuse get_page in your implementation
        """
        my_dataset = self.get_page(page, page_size)

        return {
            "page_size": page_size,
            "page": page,
            "data": my_dataset[0:],
            "next_page": None if len(my_dataset) < page_size else page + 1,
            "prev_page": None if page <= 1 else page - 1,
            "total_pages": math.ceil(len(self.dataset()) / page_size)
        }
