n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
def is_odd_even(num):
    if num%2 == 0:
        num//=2
    else:
        num-=1
    return num

def sum_elem(arr, num):
    Sum = 0
    while True:
        Sum += arr[num - 1]
        if num == 1:
            break
        num = is_odd_even(num)
    return Sum

print(sum_elem(A,m))