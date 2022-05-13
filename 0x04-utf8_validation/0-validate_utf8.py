#!/usr/bin/python3
"""Module: validUTF8"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    data_bytes = len(data)
    i = 0
    while i < data_bytes:
        byte_type = char_type(data[i])
        if byte_type == 1 or byte_type > 4:
            return False
        if byte_type == 0:
            i += 1
            continue
        valid_bytes = check_bytes(data[i+1: i + byte_type])
        if valid_bytes is False:
            return False
        i += byte_type

    return True


def char_type(byte):
    """Determine and return the type of the byte: 0, 1, 2, 3 or 4
    """
    byte_type = 0
    b_byte = bin(byte)[2:]
    left_zeros = (8 - len(b_byte))*'0'
    b_byte= left_zeros + b_byte
    for bit in b_byte:
        if bit == '0':
            break
        byte_type += 1
    return byte_type


def check_bytes(data_chunk):
    """check if byte secuence is a valir UTF-8 patron"""
    for byte in data_chunk:
        if char_type(byte) != 1:
            return False
    return True
