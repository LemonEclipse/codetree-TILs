# 변수 선언 및 입력
n = int(input())
satisfied = True

for i in range(2, n):
	# 1과 자기자신을 제외한 약수가 전혀 없다면 그 수는 소수입니다.
	if n % i == 0:
		satisfied = False

# 출력
if satisfied == True:
	print("P")
else:
	print("C")