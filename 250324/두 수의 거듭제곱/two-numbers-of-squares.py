a, b = map(int, input().split())

# Please write your code here.
def involution(fir,sec):
    n = fir
    for _ in range(sec-1):
        fir*=n
    return fir
result = involution(a,b)
print(result)




