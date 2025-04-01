nums = list(map(int,input().split()))
arr = list(map(int,input().split()))
L = []
for i in arr:

    L.append(i)
L.sort()
print(L[nums[1]-1])