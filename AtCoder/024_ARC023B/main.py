# https://atcoder.jp/contests/arc023/tasks/arc023_2

def main():
    h, w, d = list(map(int, input().split()))

    # (1, 1)からの距離に応じて格納
    A = [[] for _ in range(h + w - 1)]
    for i in range(h):
        a = list(map(int, input().split()))
        for j, aa in enumerate(a):
            A[i + j].append(aa)

    # 同じ距離のもの
    # H + W - 1が端っこ
    # Dが偶数: 0, 2, 4, ... に到達できる
    # Dが奇数: 1, 3, 5, ... に到達できる
    ans = 0
    for i in range(d % 2, min(d, h + w - 2) + 1, 2):
        ans = max(ans, max(A[i]))
    print(ans)

if __name__ == '__main__':
    main()
