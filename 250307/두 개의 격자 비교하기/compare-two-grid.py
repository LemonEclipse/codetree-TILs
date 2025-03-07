N, M = map(int, input().split())

arr_1 = [
    list(map(int, input().split()))
    for _ in range(N)  # <- N으로 바꿈
]

arr_2 = [
    list(map(int, input().split()))
    for _ in range(N)  # <- N으로 바꿈
]

for i in range(N):
    for j in range(M):
        if arr_1[i][j] == arr_2[i][j]:
            print("0", end=" ")
        else:
            print("1", end=" ")
    print()
