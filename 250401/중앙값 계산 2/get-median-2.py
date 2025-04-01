def f(List):
    List.sort()
    length = len(List)
    return List[length//2]

N = int(input())

List = list(map(int, input().split()))
n_list = []
cnt = 1
for i in List:
    n_list.append(i)
    if cnt == 1:
        print(i, end = " ")
    elif cnt%2==1:
        print(f(n_list), end = " ")
    cnt+=1
