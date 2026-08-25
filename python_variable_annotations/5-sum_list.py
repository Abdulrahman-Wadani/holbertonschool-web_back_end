#!/usr/bin/env python3
""" 5-sum_list.py """


def sum_list(input_list: list) -> float:
    """ sum_list func """
    sum: float = 0

    for input in input_list:
        sum += input
    return sum
