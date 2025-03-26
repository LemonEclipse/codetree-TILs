a, b = map(int, input().split())

# Please write your code here.

def A(fir,sec):
    if fir>sec :
        fir+=25
        sec*=2
    else:
        fir*=2
        sec+=25
    return fir, sec

a,b = A(a,b)

print(a,b)