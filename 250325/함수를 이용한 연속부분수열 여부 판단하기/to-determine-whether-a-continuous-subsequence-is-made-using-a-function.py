n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.


def L(fir,sec):
    
    length = len(fir)-len(sec)
    for i in range(length+1):
        B = True
        for j in range(len(sec)):
            if fir[j+i]!=sec[j]:
                B = False
                break
        if B :
            break 
    if B :
        return True
    else:
        return False


result = L(a,b)
if result:
    print("Yes")
else:
    print("No")

