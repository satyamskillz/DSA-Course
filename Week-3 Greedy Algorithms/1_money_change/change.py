# Uses python3
import sys

def get_change(m):
    tens=m//10
    left=m%10
    noc=tens
    if(left==5):
        noc=noc+1
    elif(left>5):
        left=left%5
        noc=noc+left+1
    else:
        noc=noc+left
    return noc

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
