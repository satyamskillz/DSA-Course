# Uses python3

import sys
import numpy as np


def max_dot_product(a, b):
    a=sorted(a)
    b=sorted(b)
    mul=np.dot(a,b)
    return mul
if __name__ == '__main__':
    data = list(map(int, input().split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
