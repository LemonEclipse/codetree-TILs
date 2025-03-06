A = [ 
    list(map(int,input().split()))
    for _ in range(3) 
]
input()
B = [ 
    list(map(int,input().split()))
    for _ in range(3) 
]

for i in range(3):
    for j in range(3):
        A[i][j] *=B[i][j]
        print(A[i][j], end = ' ')
    print()