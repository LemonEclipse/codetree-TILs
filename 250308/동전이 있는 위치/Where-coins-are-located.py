n , m = list(map(int, input().split()))

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]    

for _ in range(m):
    r,c = tuple(map(int, input().split()))
    arr[r-1][c-1] = 1

for low in arr:
    for elem in low:
        print(elem, end = " ")
    print()

