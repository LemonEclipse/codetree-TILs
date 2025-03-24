n = int(input())

# Please write your code here.
def magic_n(n):
    return n%2==0 and (int(n%10)+int(n/10))%5 ==0

if magic_n(n):
    print("Yes")
else:
    print("No")