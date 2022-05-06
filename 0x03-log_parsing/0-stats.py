#!/usr/bin/python3
"""
0. Log parsing
"""
import sys
import signal
import re
from functools import partial
from datetime import datetime


def check_format(line_split):
    try:
        ip = line_split[0].split('.')
        if not all(map(str.isdigit, ip)):
            print("PAILAS IP")
            return False

        date_str = line_split[2][1:]+' '+line_split[3][:-1]
        date_format = "%Y-%m-%d %H:%M:%S.%f"
        datetime.strptime(date_str, date_format)

        if line_split[-2] not in ["200", "301", "400", "401",
                                  "403", "404", "405", "500"]:
            return False

        int(line_split[-1])
        return True
    except:
        return False


def printstats(file_size, status_codes):
    print("File size:", file_size)
    for code in status_codes:
        if status_dict[code] > 0:
            print(f"{code}: {status_dict[code]}")

x = 0
file_size = 0

status_dict = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

try:
    for line in sys.stdin:
        line_split = line.split()
        if not check_format(line_split):
            continue
        file_size += int(line_split[-1])
        status_code = int(line_split[-2])
        status_dict[status_code] += 1

        x += 1
        if x % 10 == 0:
            x = 0
            printstats(file_size, status_codes)


except KeyboardInterrupt:
    printstats(file_size, status_codes)
