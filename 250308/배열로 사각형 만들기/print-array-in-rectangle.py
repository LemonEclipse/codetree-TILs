arr = [
    [0 for _ in range(5)]
    for _ in range(5)
]

for j in range(5):
    arr[0][j] = 1

for i in range(1,5,1):
    for j in range(5):
        arr[i][j] += arr[i-1][j]
        if j>0:
            arr[i][j] += arr[i][j-1]

for low in arr:
    for elem in low:
        print(elem, end = " ")
    print()