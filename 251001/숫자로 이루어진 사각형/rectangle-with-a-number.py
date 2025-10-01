n = int(input())

# Please write your code here.
def Code_tree(n):
    N = 0
    for _ in range(n):
        for _ in range(n):
            N+=1
            print(N, end = ' ' )
            if N == 10 :
                N == 1
        print()

Code_tree()
            