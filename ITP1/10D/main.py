n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

d1 = 0.0
d2 = 0.0
d3 = 0.0
dinf = 0.0

for i in range(n):
    d1 += abs(x[i] - y[i])
    d2 += (x[i] - y[i]) ** 2.0
    d3 += abs(x[i] - y[i]) ** 3.0
    dinf = max(dinf, abs(x[i] - y[i]))

d2 = d2 ** (1 / 2)
d3 = d3 ** (1 / 3)

print("{:.10f}".format(d1))
print("{:.10f}".format(d2))
print("{:.10f}".format(d3))
print("{:.10f}".format(dinf))
