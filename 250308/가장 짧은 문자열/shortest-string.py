s1 = input()
s2 = input()
s3 = input()

lengths = [len(s1), len(s2), len(s3)]

diff = max(lengths) - min(lengths)

print(diff)
