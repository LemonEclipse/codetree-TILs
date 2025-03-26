A = input()

# Please write your code here.
def up_two_alp(A):
    for i in range(len(A)):
        if A[0] != A[1]:
            return True
    return False


result = up_two_alp(A)

if result:
    print("Yes")
else:
    print("No")