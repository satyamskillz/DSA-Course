# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)-1
    while left<=right:
        mid=(left+right)//2
        if(a[mid]<x):
            left=mid+1
        elif(a[mid]>x):
            right=mid-1
        else:
            return mid
    return -1



def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.readline()
    data = list(map(int, sys.stdin.readline().split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(linear_search(a, x), end = ' ')
