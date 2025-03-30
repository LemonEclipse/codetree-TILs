def f(N):
    reminder = N
    if N <= 2 :
        return reminder
    if N%2 == 1:
        return f(N-2)+reminder
    elif N%2 == 0:
        return f(N-2)+reminder

N = int(input())

result = f(N)
print(result)
