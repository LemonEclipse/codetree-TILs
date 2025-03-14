A = input()
B = input()
Bool = False
cut = 0
# Please write your code here.
for i in range(len(A)-len(B)+1):
    if B in A[i:i+2]:
        Bool = True
        cut+=1
if Bool == False:
    print("-1")

print(cut)