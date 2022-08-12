# Uses python3
import sys

def piscoLenght(m):
    l=1
    old=0
    new=1
    f=[]
    f.append(0)
    f.append(1)
    i=2
    while True:
        f.append(f[i-1]+f[i-2])
        old,new=new,(old+new)%m
        if(old==0 and new==1):
            break
        l += 1
        i += 1
    return (l,f)

if __name__ == '__main__':
    n,m= map(int, input().split())
    (pl,f)=piscoLenght(m)
    rem=n%pl
    new=f[rem]%m
    print(new%m)
