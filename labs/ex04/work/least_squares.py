# -*- coding: utf-8 -*-
"""
Least Square
"""

import numpy as np


def least_squares(y, tx):
    """calculate the least squares."""
    a = tx.T.dot(tx)
    b = tx.T.dot(y)
    return np.linalg.solve(a, b)
