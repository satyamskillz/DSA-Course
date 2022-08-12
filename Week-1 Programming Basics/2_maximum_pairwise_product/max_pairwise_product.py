# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    first=-1
    second=-2
    for i in numbers:
        if(i>=first and first>=second):
            second=first
            first=i
        elif(i>=second and first>=second):
            second=i

    max_product=first*second
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
