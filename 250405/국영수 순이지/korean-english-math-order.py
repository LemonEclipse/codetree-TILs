class Score:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

N = int(input())
arr = []
for _ in range(N):
    name, kor, eng, math = input().split()
    kor = int(kor)
    eng = int(eng)
    math = int(math)
    arr.append(Score(name, kor, eng, math))

# 국어 → 영어 → 수학 점수 높은 순서로 정렬
arr.sort(key=lambda x: (-x.kor, -x.eng, -x.math))

for i in arr:
    print(i.name, i.kor, i.eng, i.math)
