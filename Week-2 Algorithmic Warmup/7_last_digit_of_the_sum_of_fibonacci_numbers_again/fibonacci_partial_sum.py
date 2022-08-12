# Uses python3
import sys

def feb(index,x):
    if(index<=0):
        return (index)
    else:
        f=[0, 1]
        s=[0,1]
        for i in range(2, index+x):
            f.append((f[i-1]+f[i-2]))
            s.append((s[i-1]+f[i]))
        return (s[index-(1-x)])


if __name__ == '__main__':
    from_, to = map(int, input().split())
    start=from_%60
    end=to%60
    (s1)=feb(start,0)
    (s2)=feb(end,1)
    c=s2-s1
    # print(s1)
    # print("-------------")
    # print(s2)
    print(c%10)