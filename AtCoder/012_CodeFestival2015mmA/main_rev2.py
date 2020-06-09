# https://atcoder.jp/contests/code-festival-2015-morning-middle/tasks/cf_2015_morning_easy_c

N, K, M, R = map(int, input().split())
S = [int(input()) for _ in range(N - 1)]
S.sort(reverse=True)
S0 = S[:K]

if sum(S[:K]) > R * K:
    print(0)
    exit()

# 一番小さいやつを抜いて，M足してクリアできる？
if sum(S[:K-1]) + M < R * K:
    print(-1)
    exit()

# 二分探索
lo = -1
hi = M

s = sum(S[:K-1])
while hi - lo > 1:
    m = (hi + lo) // 2
    if s + m >= R * K:
        hi = m
    else:
        lo = m

print(hi)