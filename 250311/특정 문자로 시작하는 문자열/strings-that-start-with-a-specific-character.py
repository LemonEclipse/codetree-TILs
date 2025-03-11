n = int(input())

arr = []

for i in range(n):
    s = input()
    arr.append(s)

A = input()
num = 0
sum_n = 0
for i in arr:
    length = len(i)
    if i[0] == A:
        num+=1
        sum_n +=len(i)
    else:
        continue
mean = sum_n/num
print(f"{num} {mean:.2f}")
if num==0:
    print("None")