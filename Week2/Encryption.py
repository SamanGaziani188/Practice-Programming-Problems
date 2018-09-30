#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    if (math.sqrt(len(s))).is_integer() == True:
        rows = columns = int(math.sqrt(len(s)))
    else:
        rows = int(math.sqrt(len(s)))
        columns = rows + 1
    if rows*columns < len(s):
        rows = rows+1
    String = ''
##    print(rows,columns)
    for i in range(columns):
        k = i
        while k < len(s):
            String = String + s[k]
            k += columns
        String = String + ' '
    return String 

print(encryption('chillout'))
