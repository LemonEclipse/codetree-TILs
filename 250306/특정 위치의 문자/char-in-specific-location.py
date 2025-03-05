arr = ['L',"E","B","R","O","S"]
C = input()
idx = -1
for i in range(len(arr)):
    if arr[i] == C:
        idx = i
    
if idx == -1:
    print("None")
else:
    print(idx)