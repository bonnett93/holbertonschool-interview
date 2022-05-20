#!/usr/bin/python3
"0 - N queens"
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

N = sys.argv[1]

if not str.isdigit(N):
    print("N must be a number")
    exit(1)

N = int(N)

if N < 4:
    print("N must be at least 4")
    exit(1)

positions = [-1] * N


def put_queen(N, col, positions):
    """Recursive function to iterate N times
        and put each Queen on a Valid place"""
    for row in range(N):
        if row in positions:
            # print(f"{row} {col} {positions} row in position")
            continue
        if diagonal_shock(row, col, positions):
            # print(f"{row} {col} {positions} diagonal block")
            continue
        positions[col] = row
        if col == N-1:
            print_positions(N, positions)
            continue
        put_queen(N, col+1, positions)
        if -1 in positions:
            positions[col] = -1


def print_positions(N, positions):
    """print possible solution"""
    final_array = []
    for i in range(N):
        final_array.append([i, positions[i]])
    print(final_array)


def diagonal_shock(row, col, positions):
    """Check if two queens are in te same diagonal"""
    for i in range(col - 1, -1, -1):
        if abs(positions[i] - row) == abs(col - i):
            # print(row, positions[i], col, i)
            return True
    return False

for i in range(N):
    positions[0] = i
    put_queen(N, 1, positions)
    positions = [-1] * N
