class home:
    def __init__(self,name, num, area):
        self.name = name
        self.num = num
        self.area = area
N = int(input())
arr = []
for _ in range(N):
    a,b,c = input().split()
    arr.append(home(a,b,c))
result = arr[0]
for i in arr[1:]:
    if i.name>result.num:
        result = i

print("name",result.name)
print("addr", result.num)
print("city", result.area)