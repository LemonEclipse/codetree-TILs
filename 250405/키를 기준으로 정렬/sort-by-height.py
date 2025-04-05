class Sort:
    def __init__(self,name,heigth,weight):
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

arr.sort(key=lambda x: x.heigth)
for person in arr:
    print(person.name, person.height, person.weight)