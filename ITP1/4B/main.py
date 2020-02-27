# -*- coding: utf-8 -*-

# from math import pi
import math

r = float(input())
area = math.pi * r * r
circ = 2.0 * math.pi * r
print("{:.10f} {:.10f}".format(area, circ))