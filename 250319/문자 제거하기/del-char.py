string = input()

leng = len(string)

arr = list(string)

while leng > 1:
	a = int(input())
	if a >= leng:
		a = leng - 1
	arr.pop(a)
	leng -= 1
	string = ''.join(arr)
	print(string)