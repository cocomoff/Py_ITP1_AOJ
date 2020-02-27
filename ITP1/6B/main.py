# -*- coding: utf-8 -*-

n = int(input())
counter = {t: [0] * 13 for t in ['S', 'H', 'C', 'D']}
for _ in range(n):
    tp, num = input().split()
    num = int(num)
    counter[tp][num - 1] += 1

for t in ['S', 'H', 'C', 'D']:
    for num in range(13):
        if counter[t][num] == 0:
            print('{} {}'.format(t, num + 1))