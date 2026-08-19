#!/usr/bin/python3
"""
Module that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices

    Args:
        m_a (list of lists): first matrix
        m_b (list of lists): second matrix

    Returns:
        list of lists: result of the multiplication

    Raises:
        TypeError: if m_a or m_b is not a list, not a list of lists,
                   contains non-int/float, or rows are not the same size
        ValueError: if m_a or m_b is empty or matrices can't be multiplied
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
mkdir -p tests
cat > tests/100-matrix_mul.txt << 'EOF'
===============================
How to use 100-matrix_mul.py
===============================

This module defines a matrix multiplication function ``matrix_mul(m_a, m_b)``.

Usage
=====

``matrix_mul(...)`` returns a new matrix representing the multiplication of
``m_a`` by ``m_b``.

::

    >>> matrix_mul = __import__('100-matrix_mul').matrix_mul
    >>> print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    [[7, 10], [15, 22]]
    >>> print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
    [[13, 16]]

Error cases (validated in the required order)
=============================================

::

    >>> matrix_mul("not a list", [[1]])
    Traceback (most recent call last):
        ...
    TypeError: m_a must be a list

    >>> matrix_mul([[1]], "not a list")
    Traceback (most recent call last):
        ...
    TypeError: m_b must be a list

    >>> matrix_mul([1, 2], [[1]])
    Traceback (most recent call last):
        ...
    TypeError: m_a must be a list of lists

    >>> matrix_mul([[1]], [1, 2])
    Traceback (most recent call last):
        ...
    TypeError: m_b must be a list of lists

    >>> matrix_mul([], [[1]])
    Traceback (most recent call last):
        ...
    ValueError: m_a can't be empty

    >>> matrix_mul([[]], [[1]])
    Traceback (most recent call last):
        ...
    ValueError: m_a can't be empty

    >>> matrix_mul([[1]], [])
    Traceback (most recent call last):
        ...
    ValueError: m_b can't be empty

    >>> matrix_mul([[1]], [[]])
    Traceback (most recent call last):
        ...
    ValueError: m_b can't be empty

    >>> matrix_mul([[1, "2"], [3, 4]], [[1, 2], [3, 4]])
    Traceback (most recent call last):
        ...
    TypeError: m_a should contain only integers or floats

    >>> matrix_mul([[1, 2], [3, 4]], [[1, "2"], [3, 4]])
    Traceback (most recent call last):
        ...
    TypeError: m_b should contain only integers or floats

    >>> matrix_mul([[1, 2], [3]], [[1, 2], [3, 4]])
    Traceback (most recent call last):
        ...
    TypeError: each row of m_a must be of the same size

    >>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3]])
    Traceback (most recent call last):
        ...
    TypeError: each row of m_b must be of the same size

    >>> matrix_mul([[1, 2]], [[1, 2], [3, 4], [5, 6]])
    Traceback (most recent call last):
        ...
    ValueError: m_a and m_b can't be multiplied

Missing arguments
=================

::

    >>> matrix_mul()
    Traceback (most recent call last):
        ...
    TypeError: matrix_mul() missing 2 required positional arguments: 'm_a' and 'm_b'

    >>> matrix_mul([[1]])
    Traceback (most recent call last):
        ...
    TypeError: matrix_mul() missing 1 required positional argument: 'm_b'
