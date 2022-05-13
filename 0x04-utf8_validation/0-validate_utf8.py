#!/usr/bin/python3
"""Module: validUTF8"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    valid_UTF = True
    for byte in data:
        if byte > 128:
            valid_UTF = False
    return valid_UTF
