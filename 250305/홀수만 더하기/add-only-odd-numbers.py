N = int(input())
sum_vul=0
for i in range(N):
    n = int(input())
    if(n%3==0 and n%2==1):
        sum_vul+=n
print(sum_vul)