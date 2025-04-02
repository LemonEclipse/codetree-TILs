class Level:
    def __init__(self,iD="codetree",lv = 10):
        self.iD = iD
        self.lv = lv
result = Level()
change = tuple(input().split())
print("user",result.iD,"lv",result.lv)
iD,lv = change
print("user",iD,"lv",lv)