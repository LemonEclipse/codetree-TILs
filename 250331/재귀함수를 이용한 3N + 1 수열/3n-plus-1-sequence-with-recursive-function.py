def f(N, cnt = 0):
    if N == 1:
        return cnt
    if N%2 == 0:
        return f(N//2,cnt+1)
    else:
        return f(N*3+1,cnt+1)
num = int(input())
print(f(num))