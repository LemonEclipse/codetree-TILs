L = input().split()
lis_T = []
result_list = []
for i in range(int(L[0])):
    s = input()
    lis_T.append(s)
lis_T.sort()
for i in lis_T:
    if i[:len(L[2])] == L[2]:  
        result_list.append(i)

print(result_list[int(L[1])-1])