#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.


def plusMinus(arr):
    pos = 0
    neg = 0
    zer = 0
    x = len(arr)
    for i in arr:
        if int(i) > 0:
            pos = pos+1
        if int(i) < 0:
            neg = neg+1
        if int(i) == 0:
            zer = zer+1
    pop = round((pos/x), 6)
    pon = round((neg/x), 6)
    poz = round((zer/x), 6)
    return pop, pon, poz


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    pop, pon, poz = plusMinus(arr)
    print(pop)
    print(pon)
    print(poz)
