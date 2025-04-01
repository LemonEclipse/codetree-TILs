def conparison(A,B):
    for i in range(len(A)):
        if A[i] != B[i]:
            return "No"
    return "Yes"

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
print(conparison(A,B))