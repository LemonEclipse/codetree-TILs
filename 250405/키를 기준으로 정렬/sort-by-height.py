class Sort(self,name,heigth,weight):
    def __init__(self):
        self.name = name
        self.heigth = heigth
        self.weight = weight

N = int(input())
arr = []
for _ in range(N):
    name,heigth,weight = input().split()
    heigth = int(heigth)
    weight = int(weight)
    arr.append(Sort(name,heigth,weight))

arr.sort(key=lambda x: x[1])
for n,h,w in arr:
    print(n,h,w)