# -*- coding: utf-8 -*-

while True:
    x, y = list(map(int, input().split()))
    if x == 0 and y == 0:
        break
    if x > y:
        x, y = y, x
    print(x, y)