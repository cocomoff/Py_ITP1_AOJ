# -*- coding: utf-8 -*-

a, b = list(map(int, input().split()))
if a < b:
    print("a < b")
elif a > b:
    print("a > b")
else:
    print("a == b")