# 정수 n과 m을 입력받습니다.
n, m = tuple(map(int, input().split()))

# arr을 입력받습니다.
arr = list(map(int, input().split()))

# m이 나온 횟수를 출력합니다.
cnt = arr.count(m)
print(cnt)