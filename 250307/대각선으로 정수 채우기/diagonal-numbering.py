n, m = map(int, input().split())

arr = [[0] * m for _ in range(n)]

num = 1
# 대각선 합(i+j)을 기준으로 숫자 채우기
for diag in range(n + m - 1):
    for i in range(n):
        for j in range(m):
            if i + j == diag:
                arr[i][j] = num
                num += 1

# 출력
for row in arr:
    print(*row)