#!/usr/bin/env python3
""" 6-sum_mixed_list.py """
from typing import (List, Union)


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ sum_mixed_list """
    sum: float = 0

    for input in mxd_lst:
        sum += input

    return sum
