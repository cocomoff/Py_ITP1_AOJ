# https://atcoder.jp/contests/abc024/tasks/abc024_c

n, d, k = list(map(int, input().split()))
D = [list(map(int, input().split())) for _ in range(d)]
for _ in range(k):
    s, t = list(map(int, input().split()))
    if s < t: # →へ行く
        for i, (l, r) in enumerate(D):
            if l <= s <= r:
                # 追い越さないようにアップデート
                s = min(r, t)
            # ゴール
            if s == t:
                print(i + 1)
                break
    else: # ←へ行く
        for i, (l, r) in enumerate(D):
            if l <= s <= r:
                # 左に飛び越さない
                s = max(l, t)
            # ゴール
            if s == t:
                print(i + 1)
                break