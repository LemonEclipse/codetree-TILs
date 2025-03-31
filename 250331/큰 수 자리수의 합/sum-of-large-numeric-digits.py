arr = list(map(int, input().split()))
m_arr = arr[0]*arr[1]*arr[2]

def f(N):
    if N<10:
        return N
    return f(N//10) + (N%10)
result = f(m_arr)
print(result)