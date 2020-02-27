# -*- coding: utf-8 -*-

r, c = list(map(int, input().split()))
A = [[0 for _ in range(c + 1)] for _ in range(r + 1)]

total = 0
for row in range(r):
    Arow = list(map(int, input().split()))
    for col in range(c):
        total += Arow[col]
        A[row][col] = Arow[col]
        A[r][col] += Arow[col]
        A[row][c] += Arow[col]
A[r][c] = total

for row in range(r + 1):
    for col in range(c + 1):
        if col < c:
            print("{} ".format(A[row][col]), end="")
        else:
            print(A[row][col], end="")
    print()