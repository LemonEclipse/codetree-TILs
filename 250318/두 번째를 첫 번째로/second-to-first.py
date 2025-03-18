Str = input()
arr = list(Str)
for i in range(len(Str)):
    a = Str[0]
    if arr[i] == Str[1]:
        arr[i] = a
result = "".join(arr)
print(result)