n = int(input())

arr = [
    input() for i in range(n)
]

num = 0
length = 0
for i in arr:
    if i[0] == 'a':
        num+=1
    length+=len(i)
print(length, num)