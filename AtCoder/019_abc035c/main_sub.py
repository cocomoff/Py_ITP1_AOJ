# https://atcoder.jp/contests/abc035/tasks/abc035_c

N, Q = map(int, input().split())

board = [0] * (N + 1)

for _ in range(Q):
    li, ri = map(int, input().split())
    for j in range(li, ri + 1):
        board[j] = (1 - board[j])

ans = "".join(map(str, board[1:]))
print(ans)