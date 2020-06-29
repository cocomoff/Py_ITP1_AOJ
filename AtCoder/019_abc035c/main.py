# https://atcoder.jp/contests/abc035/tasks/abc035_c

N, Q = map(int, input().split())

board = [0] * (N + 2)

for _ in range(Q):
    li, ri = map(int, input().split())
    board[li] += 1
    board[ri + 1] -= 1

# 累積和 (imos-method)
for i in range(1, N + 1):
    board[i] += board[i - 1]
ans = "".join("0" if v % 2 == 0 else "1" for v in board[1:-1])
print(ans)