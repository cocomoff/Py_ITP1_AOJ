from math import sin, cos, radians, sqrt

a, b, C = list(map(float, input().split()))

height = b * sin(radians(C))
area = a * height * 0.5
rem_a = a - b * cos(radians(C))
c = sqrt(rem_a ** 2 + height ** 2)
L = a + b + c

print("{:.10f}".format(area))
print("{:.10f}".format(L))
print("{:.10f}".format(height))