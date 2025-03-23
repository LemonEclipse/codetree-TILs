n, m = map(int, input().split())

# Please write your code here.

def GDC(fir,sec):
    Max = 0
    for i in range(1, min(fir, sec) + 1):
        if fir%i == 0 and sec % i == 0:
            Max = i
    return Max
result = GDC(n,m)
print(result)