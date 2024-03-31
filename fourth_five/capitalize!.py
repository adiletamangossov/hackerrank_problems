import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    cap_s = " ".join([word.capitalize() for word in s.split(" ")])
    return cap_s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
