a, b = map(int, input().split())

# Please write your code here.
def decimal(num):
    cnt = 0
    for i in range(2,num):
        if num%i == 0 :
            cnt +=1
    if cnt >0:
        return False
    else:
        return True
def two(num):
    top = num//10
    oop = num%10
    if (top+oop)%2 == 0:
        return True
    else:
        return False
cnt = 0       
for i in range(a,b+1):
    
    if decimal(i) and two(i):
        cnt+=1
print(cnt)
                        