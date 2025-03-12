Str = input()
cnt_e = 0
cnt_eb = 0
for i in range(len(Str)-1):
    if Str[i:i+2]=='ee':
        cnt_e+=1
    if Str[i:i+2]=='eb':
        cnt_eb+=1
print(cnt_e,cnt_eb)