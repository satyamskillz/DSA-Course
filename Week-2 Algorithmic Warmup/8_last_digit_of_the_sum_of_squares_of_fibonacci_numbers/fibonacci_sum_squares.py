# Uses python3
from sys import stdin

def squ(index):
    f=[0,1]
    s=[0,1]
    a=[0,1]
    for i in range(2, index+1):
        f.append((f[i-1]+f[i-2])%10)
        s.append((f[i]**2)%10)
        a.append((a[i-1]+s[i])%10)
    return a

if __name__ == '__main__':
    n = int(input())
    rem=n%60
    if (rem <= 1):
        print(rem)
    else:
        (a)=squ(rem+1)
        # print(f)
        # print(s)
        print(a[rem])
