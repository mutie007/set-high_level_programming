#!/usr/bin/python3
"""
Module that multiplies 2 matrices using NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy

    Args:
        m_a (list of lists): first matrix
        m_b (list of lists): second matrix

    Returns:
        numpy.ndarray: result of the multiplication
    """
    return (np.matmul(m_a, m_b))
