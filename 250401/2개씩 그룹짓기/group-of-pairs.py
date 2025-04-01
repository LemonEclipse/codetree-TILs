n = int(input())
nums = list(map(int, input().split()))

nums.sort()

max_sum = 0
for i in range(n):
    pair_sum = nums[i] + nums[2*n - 1 - i]
    max_sum = max(max_sum, pair_sum)

print(max_sum)
