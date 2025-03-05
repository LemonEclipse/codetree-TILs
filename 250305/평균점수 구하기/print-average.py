n= list(map(float,input().split()))
sum_vul=0
for i in n:
    sum_vul+=i
mean = sum_vul/8
print(f"{mean:.1f}")