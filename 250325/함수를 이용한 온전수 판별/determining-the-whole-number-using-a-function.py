a, b = map(int, input().split())

# Please write your code here.

def num(a,b):
    cnt=0
    for i in range(a,b+1):
        if i % 2 == 0:
            continue
        if i % 10 == 5: 
            continue
        if i % 3 == 0 and i % 9 != 0:
            continue
        else:
            cnt +=1
    return cnt

result = num(a,b)
print(result)
