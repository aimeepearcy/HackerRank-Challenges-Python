# Given an array of integers, find the sum of its elements.

#!/bin/python3

import os
import sys

def simpleArraySum(ar):
    total = 0 
    for n in ar:
        total += n
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
