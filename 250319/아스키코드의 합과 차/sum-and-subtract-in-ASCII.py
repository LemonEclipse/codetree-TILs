Alp = input().split()

print(ord(Alp[0])+ord(Alp[1]), end = ' ')
if ord(Alp[0])>ord(Alp[1]):
    print(ord(Alp[0])-ord(Alp[1]))
else:
    print(ord(Alp[1])-ord(Alp[0]))