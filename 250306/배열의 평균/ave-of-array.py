arr_2d =[
    list(map(int,input().split()))
    for _ in range(2)
]
for i in range(2):
    mean1 = sum(arr_2d[i])/4
    print(f"{mean1:.1f}", end = " ")
print()
for i in range(4):
    n = 0
    for j in range(2): 
        n += arr_2d[j][i]
    mean2 = n/2
    print(f"{mean2:.1f}", end = " ")
print()
sum_val2 = 0
for i in range(2):
    
    sum_val2 += sum(arr_2d[i])
mean3 = sum_val2/8
print(f"{mean3:.1f}")
    
    