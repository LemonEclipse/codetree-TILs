a = input()

length = len(a)

num = int(input())

if num>length:
	for i in range(length-1, -1, -1):
		print(a[i-1], end = "")
else:
	for i in range(length-1, length-num,-1):
		print(a[i-1], end = "")