from itertools import permutations

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

iP = -1
iQ = -1
for idx, perm in enumerate(permutations(range(1, N+1))):
    lp = list(perm)
    if lp == P:
        iP = idx
    if lp == Q:
        iQ = idx
print(abs(iP - iQ))