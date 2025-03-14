N = list(input().split())
a = N[0][0:2]

temp = list(N[1])  
temp[0:2] = a  
N[1] = ''.join(temp)  

print(N[1])
