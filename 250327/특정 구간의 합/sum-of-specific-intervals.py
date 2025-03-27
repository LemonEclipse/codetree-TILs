n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

def sum_of_sections():
    for a, b in queries:
        print(sum(arr[a - 1:b])) 
sum_of_sections()