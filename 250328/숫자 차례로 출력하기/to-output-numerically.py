num = int(input())

def A(num):
    if num == 0:
        return
    A(num-1)
    print(num , end = " ")

def B(num):
    if num == 0:
        return
    print(num , end = " ")
    B(num-1)

A(num)
print()
B(num)