a = input().split()
length = a[0]
for i in range(int(a[1])):
    Q = int(input())
    if Q == 1:
        length = length[1:] + length[0]
        print(length)
    elif Q == 2:
        length = length[-1] + length[:-1]
        print(length)
    elif Q == 3:
        arr = []
        for i in range(len(length)-1,-1,-1):
            arr.append(length[i])
        length = "".join(arr)

        print(length)