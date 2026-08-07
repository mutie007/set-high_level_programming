#!/usr/bin/python3
"""Defines weight_average."""


def weight_average(my_list=[]):
    """Returns the weighted average of a list of (score, weight) tuples."""
    if not my_list:
        return 0

    total_score = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for score, weight in my_list)

    return total_score / total_weight
