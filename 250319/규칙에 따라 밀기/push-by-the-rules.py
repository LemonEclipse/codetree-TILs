Str = input()
Q = input()

for i in range(len(Q)):
    if Q[i] == 'L':
                Str = Str[1:] + Str[0]
    elif Q[i] == 'R':
        Str = Str[-1] + Str[:-1]
print(Str)