#!/usr/bin/env python3
"""
Type-annotated function sum_list which takes a
list input_list of floats as argument and returns their sum as a float

"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """Returns the sum of the list as a float"""
    return float(sum(mxd_lst))
