#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    sum = 0
    for i in arr:
        sum = sum + 1
    pr_diag = 0
    sc_diag = 0
    for i in range(sum):
        for j in range(sum):
            if i == j:
                pr_diag = pr_diag + int(arr[i][j])
    for i in range(sum):
        for j in range(sum):
            if i == ((sum-1)-j):
                sc_diag = sc_diag + int(arr[i][j])
    return(abs(pr_diag-sc_diag))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
