# -*- coding: utf-8 -*-


while True:
    h, w = list(map(int, input().split()))
    if h == 0 and w == 0:
        break
    for _ in range(h):
        print("#" * w)
    print()