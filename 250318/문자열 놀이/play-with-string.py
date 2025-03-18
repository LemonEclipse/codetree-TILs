N = input().split()
arr = list(N[0])
r = int(N[1])
for i in range(r):
    n = input().split()
    if n[0] == '1' :
        k = arr[int(n[1])-1]
        arr[int(n[1])-1] = arr[int(n[2])-1] 
        arr[int(n[2])-1] = k
    if n[0] == '2' :
        for j in range(len(arr)):
            if arr[j] == n[1]:
                arr[j] = n[2]
    result = "".join(arr)      
    print(result)
    
