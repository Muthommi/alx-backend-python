#!/usr/bin/env python3
"""
Module to provide a function to calculate sum of mixed list of
integers and floats.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function that takes a list of integers and floats and returns
    their sum.
    Returns: Float.
    """
    return sum(mxd_lst)
