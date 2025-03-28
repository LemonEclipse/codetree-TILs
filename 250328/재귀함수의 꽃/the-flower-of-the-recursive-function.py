def recursion(N):
    if N == 0:
        return
    print(N, end = " ")
    recursion(N-1)
    print(N, end = " ")
N = int(input())
recursion(N)