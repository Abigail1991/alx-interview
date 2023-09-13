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

if __name__ == "__main__":
    # Define your matrix here
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    
    # Call the rotation function
    rotate_2d_matrix(matrix)

    # Print the rotated matrix
    for row in matrix:
        print(row)
