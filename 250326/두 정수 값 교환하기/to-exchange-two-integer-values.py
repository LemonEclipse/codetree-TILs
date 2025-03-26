n, m = map(int, input().split())

# Please write your code here.
def swap(fir,sec):
    fir,sec = sec,fir
    return fir,sec
n,m = swap(n,m)
print(n,m)
