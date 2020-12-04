import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    factorial = 1
    if n==1:
        return 1
    else:
        for i in range(1,n + 1):
             factorial = factorial*i
        return factorial
    
# if __name__ == '__main__':
    # n = int(input())
    n = 100

res=extraLongFactorials(100)
print(res)

