# https://atcoder.jp/contests/code-festival-2015-morning-middle/tasks/cf_2015_morning_easy_c

N, K, M, R = map(int, input().split())
S = [int(input()) for _ in range(N - 1)]
S.sort(reverse=True)
S0 = S[:K]

# 二分探索
lo = 0
hi = M

while lo <= hi:
    mi = (lo + hi) // 2
    S = S0 + [mi]
    S.sort()
    mS = sum(S[1:]) / K
    if mS == R:
        print(mi)
        exit()
    elif mS < R:
        lo = mi + 1
    else:
        hi = mi - 1

if lo > M:
    print(-1)
else:
    print(lo)