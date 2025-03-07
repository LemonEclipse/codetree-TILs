N,M = map(int,input().split(" "))

arr_1 = [
    [0 for _ in range(M)]
    for _ in range(N)
]
arr_2 = [
    [0 for _ in range(M)]
    for _ in range(N)
]
arr_1 = [
    list(map(int,input().split(" ")))
    for _ in range(M)
]
arr_2 = [
    list(map(int,input().split(" ")))
    for _ in range(M)
]

for i in range(N):
    for j in range(M):
        if arr_1[i][j] == arr_2[i][j]:
            print("0 ", end="")
        else:
            print("1 ", end="")
    print()