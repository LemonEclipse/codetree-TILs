text = input()
pattern = input()

# Please write your code here.

def index():
    for i in range(len(text)-len(pattern)+1):
        if text[i:len(text)+i] == pattern:
            return i
    return -1

print(index())               