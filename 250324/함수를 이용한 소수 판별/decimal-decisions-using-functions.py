a, b = map(int, input().split())

# Please write your code here.
def dec_sum(a,b):
    Sum = 0
    if a==b:
        return 0
    for i in range(a,b+1):
        Bool = True
        for j in range(2,i):
            if i%j ==0:
                Bool = False
        if Bool :
            Sum+=i
    return Sum

print(dec_sum(a,b))