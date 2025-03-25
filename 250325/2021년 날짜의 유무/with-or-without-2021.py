M, D = map(int, input().split())

# Please write your code here.

def Date(M,D):
    if M<=7:
        if M%2==0:
            if M==2 and D<=28 and D>=1:
                return "Yes"
            if D>0 and D<31:
                return "Yes"
            else:
                return "No"
        else:
            if D>0 and D<31:
                return "Yes"
            else:
                return "No"
    elif M<=12:
        if M%2==0:
            if D>0 and D<31:
                return "Yes"
            else:
                return "No"
        else:
            if D>0 and D<30:
                return "Yes"
            else:
                return "No"
    else:
        return "No"
result = Date(M,D)

print(result)