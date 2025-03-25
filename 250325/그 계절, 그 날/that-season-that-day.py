Y, M, D = map(int, input().split())

# Please write your code here.
def leep_year(Y):
    if Y%4==0 and Y%100!=0 or Y%400==0:
        return True
    else:
        return False

def last_day_number(Year, Month):

    if Month == 2 and leep_year(Year):
        return 29
    elif Month == 2 :
        return 28
    elif Month ==4 or Month==6 or Month==9 or Month==11:
        return 30
    else:
        return 31

def F_season(Month):
    if Month>=3 and Month<=5:
        return "Spring"
    elif Month>=6 and Month<=8:
        return "Summer"
    elif Month>=9 and Month<=11:
        return "Fall"
    else:
        return "Winter"

def season(Y,M,D):
    if M<=12 and D<=last_day_number(Y,M):
        return  F_season(M)
    else:
        return "-1"

result = season(Y,M,D)

print(result)