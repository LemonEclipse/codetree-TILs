class program:
    def __init__(self,code,color,sec):
        self.code = code
        self.color = color
        self.sec = sec

code, color,sec = input().split()

result = program(code,color,sec)

print("code :",result.code)
print("color :", result.color)
print("second :", sec)