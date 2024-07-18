#!/usr/bin/env python3
"""Simple helper function"""
import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    A function that takes in int args and retuns a tuple
    of size two containing a start index and an end index

    Args:
        page (int): page number
        page_size (int): total number of pages

    Returns:
        A tuple of size two
    """
    start_index: int = (page - 1) * page_size
    end_index: int = start_index + page_size

    return (start_index, end_index)


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
        Gets the content of a given page with given default parameters or
        overidding parameters
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        # the index_range function
        idx_range = index_range(page=page, page_size=page_size)

        # retrieve the data from the baby names csv file
        dataset = self.dataset()

        # if input args are out of range for the dataset, return an
        # empty list
        # if the first index arg is greater than len of dataset,
        if idx_range[0] >= len(dataset):
            return []

        # append each line in generated valid index to a list
        paginated = []
        for line in range(idx_range[0], idx_range[1]):
            paginated.append(dataset[line])
        return paginated
