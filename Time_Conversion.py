#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#


def timeConversion(s):
    if "AM" in s:
        y = s[:2]
        if y == "12":
            str1 = s.replace("AM", "")
            str2 = str1.replace("12", "00")
            return str2
        else:
            str2 = s.replace("AM", "")
            return str2
    if "PM" in s:
        y = s[:2]
        if y == "12":
            str2 = s.replace("PM", "")
            return str2
        else:
            z = s[0:1]
            i = s[1:2]
            if z == "0":
                hour = int(i)
                mil = hour + 12
                mil = str(mil)
                str1 = s.replace("PM", "")
                str2 = str1.replace(y, mil)
                return str2
            else:
                hour = int(y)
                mil = hour + 12
                mil = str(mil)
                str1 = s.replace("PM", "")
                str2 = str1.replace(y, mil)
                return str2


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
