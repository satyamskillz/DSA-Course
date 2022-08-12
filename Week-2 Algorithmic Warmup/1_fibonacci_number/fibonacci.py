# Uses python3
def calc_fib(n):
    f=(((1+5**0.5)/2)**n-((1-5**0.5)/2)**n)/5**0.5
    return int(f)

n = int(input())
print(calc_fib(n))
