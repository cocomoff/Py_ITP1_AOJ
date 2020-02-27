from math import sqrt

x1, y1, x2, y2 = list(map(float, input().split()))

dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print("{:.10f}".format(dist))