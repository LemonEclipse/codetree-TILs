def print_star(num):
    if num == 0 :
        return
    print_star(num-1)
    print("*"*num)

num = int(input())
print_star(num)