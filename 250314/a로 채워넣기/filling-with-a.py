Str = input()
arr = list(Str)
arr[1]='a'
arr[-2]='a'
Str = "".join(arr)
print(Str)