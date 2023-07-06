#!/usr/bin/env python3
"""
Type-annotated function sum_list which takes a
list input_list of floats as argument and returns their sum as a float

"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]] = []) -> float:
    """
    Returns the sum as a floa
    """
    return float(sum(mxd_lst))
