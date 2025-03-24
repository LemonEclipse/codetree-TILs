y = int(input())

# Please write your code here.
def leep_year(year):
    if y % 4 != 0:
        return false
    
    if y % 100 != 0:
        return true
    
    if y % 400 == 0:
        return true
    
    return false
if leep_year(y):
    print("true")
else:
    print("false")