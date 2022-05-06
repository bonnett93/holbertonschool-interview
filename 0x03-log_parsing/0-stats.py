#!/usr/bin/python3
"""
0. Log parsing: reads stdin line by line and computes metrics
"""
import sys


def printstats(file_size, status_codes):
    """
    print stats about file_size and status_codes
    """
    print("File size:", file_size)
    for code in status_codes:
        if status_dict[code] > 0:
            print(f"{code}: {status_dict[code]}")

x = 0
file_size = 0

status_dict = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]


for line in sys.stdin:
    try:
        line_split = line.split()
        file_size += int(line_split[-1])
        status_code = int(line_split[-2])
        status_dict[status_code] += 1

        x += 1
        if x % 10 == 0:
            x = 0
            printstats(file_size, status_codes)

    except KeyboardInterrupt:
        printstats(file_size, status_codes)
    except Exception:
        continue
