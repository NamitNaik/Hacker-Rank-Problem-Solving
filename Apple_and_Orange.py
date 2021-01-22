#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.


def countApplesAndOranges(s, t, a, b, apples, oranges):
    m = len(apples)
    n = len(oranges)
    reg_apples = 0
    reg_oranges = 0
    for i in range(m):
        apples[i] = apples[i] + a
        if apples[i] >= s and apples[i] <= t:
            reg_apples = reg_apples + 1
    for j in range(n):
        oranges[j] = oranges[j] + b
        if oranges[j] >= s and oranges[j] <= t:
            reg_oranges = reg_oranges + 1
    return (reg_apples, reg_oranges)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    (reg_apples, reg_oranges) = countApplesAndOranges(s, t, a, b, apples, oranges)

    print(reg_apples)

    print(reg_oranges)
