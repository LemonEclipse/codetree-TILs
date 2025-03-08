n = int(input())

arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    arr_2d[i][0] = 1
    arr_2d[i][i] = 1

for i in range(n):
	for j in range(1, i):
		arr_2d[i][j] = arr_2d[i - 1][j - 1] + arr_2d[i - 1][j]

for low in arr_2d:
    for elem in low:
        if elem == 0:
            continue
        print(elem , end = " ")
    print()
