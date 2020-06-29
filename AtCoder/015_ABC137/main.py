# https://atcoder.jp/contests/abc137/tasks/abc137_d

n, m = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(n)]

print(n, m, AB)

# dp[i][j] i日目までにjまで使って得られる最大の報酬
# dp[M][N] 解

dp = [[-1] * (n + 1) for _ in range(m + 1)]
for k in range(1, n + 1):
    dp[1][k] = 0

for i in range(1, m + 1):
    # i日目
    for k in range(1, n + 1):
        # (k-1)品目
        if i > AB[k - 1][1]:
            dp[i][k] = max(dp[i][k], dp[i - AB[k - 1][1]][k] + AB[k-1][0])

for row in dp: print(*row)