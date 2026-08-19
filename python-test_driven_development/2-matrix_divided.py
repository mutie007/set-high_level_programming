#!/usr/bin/python3
"""
Module that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div

    Args:
        matrix (list of lists): matrix of integers or floats
        div (int or float): the divisor

    Returns:
        list of lists: new matrix with all elements divided by div
                       (rounded to 2 decimal places)

    Raises:
        TypeError: if matrix is not a list of lists of integers/floats,
                   if rows have different sizes, or if div is not a number
        ZeroDivisionError: if div is equal to 0
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(num, (int, float))
                    for row in matrix for num in row)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
