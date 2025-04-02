class secret:
    def __init__(self, code, place,time):
        self.code = code
        self.place = place
        self.time = time


arr = input().split()
result = secret(arr[0],arr[1],arr[2])
print("secret code :",result.code)
print("meeting point :",result.place)
print("time :", result.time)