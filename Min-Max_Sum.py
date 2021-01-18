#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.


def miniMaxSum(arr):
    total = sum(arr)
    sl = list()
    n = len(arr)
    for i in range(n):
        s = total - arr[i]
        sl.append(s)
        s = total
    print(min(sl), max(sl))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
