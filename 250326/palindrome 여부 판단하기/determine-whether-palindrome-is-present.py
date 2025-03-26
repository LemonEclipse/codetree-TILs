A = input()

# Please write your code here.
def palindrome(A):
    cnt = 0
    B = True
    for i in range(len(A)-1,-1,-1):
        if A[i] != A[cnt]:
            B = False
        cnt+=1
    return B
result = palindrome(A)
if result:
    print("Yes")
else:
    print("No")