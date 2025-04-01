n = int(input())
arr = []
for i in range(n):
    string = input()
    arr.append(string)
arr.sort()
for i in arr:
    print(i)