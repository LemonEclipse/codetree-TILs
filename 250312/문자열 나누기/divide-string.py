N = int(input())
arr = input().split()
string = "".join(arr)
cnt = 0
for i in range(len(string)):
    print(string[i], end = "")
    cnt+=1
    if cnt%5==0:
        print()

