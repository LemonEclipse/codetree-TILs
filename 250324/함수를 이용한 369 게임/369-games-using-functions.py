a, b = map(int, input().split())

# Please write your code here.
def is_Thr(n):
    while n > 0:
        if n % 10 == 3 or n % 10 == 6 or n % 10 == 9:
            return True

        n //= 10

    return False
def is_369_number(n):
    return is_Thr(n) or (n % 3 == 0)


cnt = 0
for i in range(a, b + 1):
    if is_369_number(i):
        cnt += 1

print(cnt)