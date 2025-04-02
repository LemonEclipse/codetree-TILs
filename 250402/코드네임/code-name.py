class codename:
    def __init__(self,name,score):
        self.n = name
        self.s = int(score)

students = []
for _ in range(5):
    name, score = tuple(input().split())
    students.append(codename(name,score))
min_score = students[0]
for i in students[1:]:
    if i.s<min_score.s:
        min_score = i

print(min_score.n, min_score.s)
    