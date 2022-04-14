#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    pascal_triangle = []
    if n > 0:
        pascal_triangle.append([1])
        for i in range(n-1):
            tmp_level = [0] + pascal_triangle[i] + [0]
            new_level = [tmp_level[n]+tmp_level[n+1] for n in range(i+2)]
            pascal_triangle.append(new_level)
    return pascal_triangle
