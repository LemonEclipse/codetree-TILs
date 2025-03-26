a, b = map(int, input().split())

# Please write your code here.

def A(fir,sec):
    if fir>sec :
        fir*=2
        sec+=10
    else:
        fir+=10
        sec*=2
    return fir, sec

a,b = A(a,b)

print(a,b)