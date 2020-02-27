
while True:
    h, w = list(map(int, input().split()))
    if h == 0 and w == 0:
        break

    for row in range(h):
        if row == 0 or row == h - 1:
            print("#" * w)
        else:
            print("#{}#".format("." * (w - 2)))

    print()