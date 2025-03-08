arr = ["apple","banana","grape","blueberry","orange"]
num = 0
c = input()
for i in range(5):
    if arr[i][2]==c or arr[i][3]==c:
        print(arr[i])
        num += 1
print(num)