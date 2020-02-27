# -*- coding: utf-8 -*-

n = int(input())
A = list(map(int, input().split()))
for i in range(n - 1, -1, -1):
    print(A[i], end="")
    if i > 0:
        print(" ", end="")
print()