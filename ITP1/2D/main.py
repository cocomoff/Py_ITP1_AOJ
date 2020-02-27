# -*- coding: utf-8 -*-

W, H, x, y, r = list(map(int, input().split()))

if y + r > H: # Up
    print("No")
elif y - r < 0: # Down
    print("No")
elif x - r < 0: # Left
    print("No")
elif x + r > H: # Right
    print("No")
else:
    print("Yes")
