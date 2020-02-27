while True:
    s = input()
    if s == '-':
        break
    n = int(input())
    l = [int(input()) for _ in range(n)]

    # operation
    for v in l:
        new_s = s[v:] + s[:v]
        s = new_s
    print(s)