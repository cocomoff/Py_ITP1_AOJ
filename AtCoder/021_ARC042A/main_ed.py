N, M = map(int, input().split())
A = [i for i in range(1, N + 1)]

# 最後に出てきた順番
loc = [-1] * (N + 1)

for idx in range(M):
    ai = int(input())
    loc[ai] = idx

# 出てきた
liA = [(loc[a], a) for a in range(1, N + 1) if loc[a] != -1]
liA.sort(reverse=True)
# 出てきていない
lniA = [a for a in range(1, N + 1) if loc[a] == -1]

for (_, a) in liA:
    print(a)
for a in lniA:
    print(a)