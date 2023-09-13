#!/usr/bin/python3
"""Rotate 2D Matrix module.

This module contains a function related to the 2D Matrix Module.

"""


def rotate_2d_matrix(matrix):
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]

rotate_2d_matrix(matrix)

# The matrix will be rotated in-place
for row in matrix:
    print(row)
