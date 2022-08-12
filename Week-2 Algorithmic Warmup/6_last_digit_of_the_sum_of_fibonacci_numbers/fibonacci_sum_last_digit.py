# Uses python3
import sys


def feb(index):
    if(index<=1):
        return ([0,1],[0,1])
    else:
        f=[0, 1]
        s=[0,1]
        for i in range(2, index+1):
            f.append((f[i-1]+f[i-2])%10)
            s.append((s[i-1]+f[i])%10)
        return (f,s)


if __name__ == '__main__':
    n = int(input())
    rem=n%60
    (f,s)=feb(rem)
    # print(f)
    print(s[rem])

