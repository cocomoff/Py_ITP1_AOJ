# -*- coding: utf-8 -*-

counter = [[[0] * 10 for i in range(4)] for k in range(5)]
# counter = [[[0] * 10] * 3] * 4

n = int(input())
for _ in range(n):
    b, f, r, v = list(map(int, input().split()))
    b -= 1
    f -= 1
    r -= 1
    counter[b][f][r] += v

x = 0
for i in range(4):
    if x != 0:
        print("#" * 20)
    x += 1

    for a in range(3):
        for b in range(10):
            print(" {}".format(counter[i][a][b]), end="")
        print()
