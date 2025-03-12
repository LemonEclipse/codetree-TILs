input_str = input()
target_str = input()
B = False
# Please write your code here.
for i in range(len(input_str)-len(target_str)+1):
    if input_str[i:i+len(target_str)] in target_str:
        B = True
        print(i)
        break
if B == False:
    print("-1")