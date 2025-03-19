a = input()
length = len(a)
k = -1
print(a)
for i in range(length):
    result = a[k:]+a[:length+k]
    print(result)
    k-=1