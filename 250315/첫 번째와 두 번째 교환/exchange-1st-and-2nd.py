Str = input()
arr_Str = list(Str)
arr_copy = arr_Str[:]
for i in range(len(arr_Str)):
    
    if arr_Str[i] == arr_Str[0]:
        arr_copy[i] = arr_Str[1]
    elif arr_Str[i] == arr_Str[1]:
        arr_copy[i] = arr_Str[0]

result = "".join(arr_copy)
print(result)