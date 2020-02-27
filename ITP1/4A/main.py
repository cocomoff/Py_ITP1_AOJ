# -*- coding: utf-8 -*-

a, b = list(map(int, input().split()))
print("{} {} {:.10f}".format(a//b, a % b, a/b))
