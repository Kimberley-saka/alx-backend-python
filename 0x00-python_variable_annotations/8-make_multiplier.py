#!/usr/bin/env python3
"""type-annotated function make_multiplier
"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier"""
    def multiply(x: float) -> float:
        return multiplier * x

    return multiply
