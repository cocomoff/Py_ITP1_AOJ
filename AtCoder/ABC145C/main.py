from itertools import permutations

N = int(input())
lx, ly = [], []
for _ in range(N):
    xi, yi = list(map(int, input().split()))
    lx.append(xi)
    ly.append(yi)

fN = 1
for i in range(1, N + 1):
    fN *= i

mcost = 0
for x in permutations(list(range(N))):
    cost = 0.0
    for i in range(len(x) - 1):
        dij = ((lx[x[i]] - lx[x[i + 1]]) ** 2 + (ly[x[i]] - ly[x[i + 1]]) ** 2) ** 0.5
        cost += dij
    mcost += cost / fN
print(mcost)