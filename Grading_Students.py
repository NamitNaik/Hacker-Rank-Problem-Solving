#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades):
    final_grade = list()
    for i in grades:
        n = int(i) % 5
        x = 5 - n
        if int(i) > 37:
            if x < 3:
                q = int(i) / 5
                fg = 5 * (int(q)+1)
                final_grade.append(fg)
            else:
                final_grade.append(i)
        else:
            final_grade.append(i)
    return final_grade


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
