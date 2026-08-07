#!/usr/bin/python3
"""Module that defines a function to square all integers in a matrix."""


def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.

    Args:
        matrix (list of lists): A 2-dimensional array of integers.

    Returns:
        list of lists: A new matrix of the same size where each value
        is the square of the corresponding value in the input matrix.
        The original matrix is not modified.
    """
    return [[x ** 2 for x in row] for row in matrix]
