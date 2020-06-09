# 足りない分を見る

def main():
    N, K, M, R = (int(i) for i in input().split())
    S = [int(input()) for i in range(N-1)]
    S.sort(reverse=True)  # 大きい方からK-1個取る
    ans = sum(S[:(K-1)])
    need = K*R - ans  # 残りどれだけあればいいか
    if need <= 0 or (K-1 < N-1 and need <= S[K-1]):
        print(0)
    elif need <= M:
        print(need)
    else:
        print(-1)

if __name__ == '__main__':
    main()