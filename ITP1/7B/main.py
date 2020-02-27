# -*- coding: utf-8 -*-

while True:
    n, x = list(map(int, input().split()))
    if n == 0 and x == 0:
        break

    count = 0
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            for c in range(b + 1, n + 1):
                if a == c or b == c:
                    continue
                if a + b + c == x:
                    count += 1

    print(count)