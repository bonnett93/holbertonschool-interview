#!/usr/bin/python3
""" Rotate 2d Matrix """


def rotate_2d_matrix(matrix):
    """Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    posicion i,j -> [j][n-i-1]
    """
    n = len(matrix)
    matrix_b = [row.copy() for row in matrix]
    for i in range(n):
        for j in range(n):
            matrix[j][n-i-1] = matrix_b[i][j]
