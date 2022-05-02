#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly
    n H characters in the file.
    """
    operations = 0
    i = 2
    while n >= i:
        while n % i == 0:
            operations += i
            n = n / i
        i += 1
    return operations
