a, b, c = map(int, input().split())

# Please write your code here.

def Min(*args):
    ans = []
    ans.append(args)
    return min(args)

print(Min(a,b,c))