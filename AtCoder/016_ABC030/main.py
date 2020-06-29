# https://atcoder.jp/contests/abc030/tasks/abc030_c

import bisect

n, m = map(int, input().split())
x, y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# print(n, m, x, y)
# print(A, B)

ans = 0
now = 0
while True:
    # print(ans, now)
    # A -> B
    i = bisect.bisect_left(A, now)
    if i == n:
        break
    now = A[i] + x

    # B -> A
    j = bisect.bisect_left(B, now)
    if j == m:
        break
    now = B[j] + y
    ans += 1

print(ans)