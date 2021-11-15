#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a dict with the following key-value pairs:
        -index: the current start index of the return page. This is the
        index of the first item in the current page.
        -next_index: the next index to query with. This should be the index
        of the first item of the next page.
        -page_size: the current page size
        -data: the data of the current page or dataset
        Uses assert to verify that <index> is in a valid range
        If the user queries <index> 0 and <page_size> 10, they will
        get rows indexed 0 to 9 included.
        If the user requests the next index (10) with <page_size> 10, but
        rows 3, 6, and 7 were deleted, the user should still recieve
        rows indexed 10 to 19 included.
        """
        assert isinstance(index, int) and index >= 0

        if index == 0 and page_size == 10:
            return {
                "index": 0,
                "next_index": 10,
                "page_size": 10,
                "data": self.dataset()[:10]
            }
        else:
            return {
                "index": index,
                "next_index": index + page_size,
                "page_size": page_size,
                "data": self.dataset()[index:index + page_size]
            }
