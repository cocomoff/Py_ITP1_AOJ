# https://atcoder.jp/contests/arc023/tasks/arc023_2

def main():
    R, C, D = list(map(int, input().split()))
    A = [tuple(map(int, input().split())) for _ in range(R)]

    # (i + j) <= D or 偶奇が一致
    ans = 0
    r0, c0 = 0, 0
    for r in range(R):
        for c in range(C):
            d = abs(r - r0) + abs(c - c0)
            if d <= D and (D - d) % 2 == 0:
                ans = max(ans, A[r][c])
    print(ans)

if __name__ == '__main__':
    main()
