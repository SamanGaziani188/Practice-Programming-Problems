#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    startpoint = round(math.sqrt(a))
    count = 0
    while startpoint**2 <= b:
        if startpoint**2 < a:
            startpoint = startpoint+1
        else:
            count = count+1
            startpoint = startpoint+1
    return count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
