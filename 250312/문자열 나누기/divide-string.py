N = int(input())
arr = input().split()
if len(arr) != N:
    print("입력한 개수와 맞게 입력하시오")
    exit()
string = "".join(arr)
for i in range(len(string)):
    print(string[i], end = "")
    if (i+1)%5==0:
        print()

