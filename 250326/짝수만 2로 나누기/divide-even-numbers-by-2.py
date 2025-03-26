n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def even_div(arr):
    for i in range(len(arr)):
        if L[i]%2==0:
            L[i] //=2
    return arr

even_div(arr)
print(arr)