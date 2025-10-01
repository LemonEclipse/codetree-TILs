n = int(input())

# Please write your code here.
def Code_tree(n):
    N = 1
    for _ in range(n):
        for _ in range(n):
            print(N, end = ' ' )
            N+=1
            if N == 10 :
                N = 1
        print()

Code_tree(n)
            