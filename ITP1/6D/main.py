# -*- coding: utf-8 -*-

n, m = list(map(int, input().split()))

A = [[0 for _ in range(m)] for _ in range(n)]
b = [0 for _ in range(m)]
c = [0 for _ in range(n)]

for row in range(n):
    arow = list(map(int, input().split()))
    for j in range(m):
        A[row][j] = arow[j]

for row in range(m):
    b[row] = int(input())

for row in range(n):
    for k in range(m):
        c[row] += A[row][k] * b[k]

for j in c:
    print(j)