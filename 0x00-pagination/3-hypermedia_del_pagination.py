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

    def get_hyper_index(
            self, index: int = None, page_size: int = 10  # type: ignore
    ) -> Dict:  # nopep8
        """
        A method that ensures pagination is consistent in the event
        deletion or addition of data occurs.

        Handles deletion in a deletion-resilient manner
        """
        indexed_datasest = self.indexed_dataset()
        assert index <= len(indexed_datasest)

        current_idx = index

        data = []
        while len(data) < page_size and current_idx < len(indexed_datasest):  # nopep8
            item = indexed_datasest.get(current_idx)
            if item:
                data.append(item)
            current_idx += 1

        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": current_idx
        }
