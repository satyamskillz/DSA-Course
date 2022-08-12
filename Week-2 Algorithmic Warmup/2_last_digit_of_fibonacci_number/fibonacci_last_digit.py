# Uses python3
import sys


def get_fibonacci_last_digit(n):
    if(n<=1):
        return n
    old=0
    new=1
    for i in range(n-1):
        old,new=new,(old+new)%10
    return new%10
if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit(n))
