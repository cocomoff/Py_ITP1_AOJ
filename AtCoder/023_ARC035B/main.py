# https://atcoder.jp/contests/arc035/tasks/arc035_b

from collections import Counter

MOD = int(10 ** 9 + 7)
f = [0] * (10001)
f[0] = f[1] = 1
for i in range(2, 10001):
    f[i] = i * f[i - 1] % MOD

n = int(input())
A = [int(input()) for _ in range(n)]
cA = Counter(A)
A.sort()
ans = 0
now = 0
for a in A:
    ans += (now + a)
    now += a

pos = 1
for key in cA:
    pos = (pos * f[cA[key]]) % MOD

print(ans)
print(pos)
