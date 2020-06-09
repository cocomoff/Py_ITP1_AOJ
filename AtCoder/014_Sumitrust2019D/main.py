N = int(input())
S = input()
count = 0
ans = set({})

for password in range(0, 1000):
    s = "{:03d}".format(password)
    s1, s2, s3 = s
    
    if s1 not in S:
        continue
    i1 = S.index(s1)
    if s2 not in S[i1+1:]:
        continue
    i2 = S[i1+1:].index(s2)
    if s3 not in S[i1+1:][i2+1:]:
        continue
    i3 = S[i1+1:][i2+1:].index(s3)
    ans.add(password)

print(len(ans))