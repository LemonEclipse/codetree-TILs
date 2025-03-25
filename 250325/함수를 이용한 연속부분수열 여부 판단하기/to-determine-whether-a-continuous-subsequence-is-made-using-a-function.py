n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def L(fir, sec):
    for i in range(len(fir) - len(sec) + 1):
        if fir[i:i + len(sec)] == sec:
            return True
    return False

if len(a) < len(b):
    print("No")
    exit()

result = L(a, b)
if result:
    print("Yes")
else:
    print("No")
