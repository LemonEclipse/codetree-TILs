n = int(input())

# Please write your code here.
def magic(n):

    return n%2==0 and (int(n%10)+int(n/10))

bool a = magic(n)

print(a)