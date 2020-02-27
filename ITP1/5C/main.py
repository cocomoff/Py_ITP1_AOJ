while True:
    h, w = list(map(int, input().split()))
    if h == 0 and w == 0:
        break

    for row in range(h):
        if row % 2 == 0:
            print("#." * (w // 2), end="")
            print("" if w % 2 == 0 else "#")
        else:
            print(".#" * (w // 2), end="")
            print("" if w % 2 == 0 else ".")

    print()