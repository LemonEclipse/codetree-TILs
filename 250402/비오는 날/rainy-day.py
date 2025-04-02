class Weater:
    def __init__(self,date,week,weater):
        self.date = date
        self.week = week
        self.weater = weater

N = int(input())
List = []
for _ in range(N):
    date,week,weater = tuple(input().split())
    if weater == "Rain":
        List.append(Weater(date,week,weater))
result = List[0]
for i in List[1:]:
    if i.date<result.date:
        result = i

print(result.date,result.week,result.weater)