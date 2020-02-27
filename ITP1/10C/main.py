while True:
    n = int(input())
    if n == 0:
        break

    s = list(map(int, input().split()))

    sum_s = sum(s)
    avg_s = (float)(sum_s / n)
    div = 0
    for v in s:
        div += (v - avg_s) ** 2 / n
    print("{:.10f}".format(div ** 0.5))