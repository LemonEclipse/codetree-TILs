def star_print(N):
    if N == 0:
        return
    print("* "*N)
    star_print(N-1)
    print("* "*N)

N = int(input())
star_print(N)