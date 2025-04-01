nums = list(map(int,input().split()))

L = []
for i in range(nums[0]):
    L.append(i)
L.sort()
print(L[nums[1]+1])