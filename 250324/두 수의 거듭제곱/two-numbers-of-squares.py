a, b = map(int, input().split())

# Please write your code here.
def involution(fir,sec):
    for _ in range(sec):
        fir*=fir

result= involutionn(a,b)
print(result)