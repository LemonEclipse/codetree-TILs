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

arr.sort(key=lambda x: x.kor, x.eng, x.math)
for name,kor,eng,math in arr:
    print(name,kor,eng,math)
