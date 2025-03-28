def Hello(n):
    if n == 0:
        return
    Hello(n - 1)
    print("HelloWorld")
num = int(input())
Hello(num)