n= 4 
arr_2d = [
    list(map(int,input().split()))
    for _ in range(n)
]

for i in range(n):
    sum_val=0
    for j in range(4):
        sum_val+=arr_2d[i][j]
    print(sum_val)