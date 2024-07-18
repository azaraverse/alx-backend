#!/usr/bin/env python3
"""Simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    A function that takes in int args and retuns a tuple
    of size two containing a start index and an end index

    Args:
        page (int): page number
        page_size (int): total number of pages

    Returns:
        A tuple of size two
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
