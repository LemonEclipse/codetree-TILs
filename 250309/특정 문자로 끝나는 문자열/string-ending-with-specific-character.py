arr = []

for i in range(10):
    s = input()
    arr.append(s)

A = input()
num = 0
for i in arr:
    length = len(i)
    if i[length-1] == A:
        print(i)
        num+=1
    else:
        continue
if num==0:
    print("None")