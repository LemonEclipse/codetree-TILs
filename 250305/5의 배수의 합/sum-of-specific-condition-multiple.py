A, B = map(int, input().split()) 
sum_val = 0
count = 0 

for i in range(A, B + 1):
    if i % 5 == 0 or i % 7 == 0:
        sum_val += i
        count += 1
     
mean = sum_val/count

print("%d %.1f" %sum_val, %mean)
