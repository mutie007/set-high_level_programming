#!/usr/bin/python3
"""Module that defines a function to generate Pascal's triangle."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    the Pascal's triangle of n.

    Args:
        n (int): The number of rows.

    Returns:
        list: A list of lists representing Pascal's triangle.
              Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev = triangle[-1]
        row = [1]
        for j in range(1, len(prev)):
            row.append(prev[j - 1] + prev[j])
        row.append(1)
        triangle.append(row)

    return triangle
