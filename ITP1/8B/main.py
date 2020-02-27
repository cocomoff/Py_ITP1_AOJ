while True:
    s = input()
    if s == '0':
        break

    sum = 0
    for c in s:
        sum += int(c)
    print(sum)