#!/usr/bin/env python3
""" 5-sum_list.py """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ sum_list func """
    sum: float = 0

    for input in input_list:
        sum += input
    return sum
