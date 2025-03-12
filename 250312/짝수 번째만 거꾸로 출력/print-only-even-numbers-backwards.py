A = input()
lenght = len(A)
for i in range(lenght-1,-1,-1):
    if i%2 == 1 :
        print(A[i], end = "")
