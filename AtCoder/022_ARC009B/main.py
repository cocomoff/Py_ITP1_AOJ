# https://atcoder.jp/contests/arc009/tasks/arc009_2

B = list(map(int, input().split()))
N = int(input())
A = [int(input()) for _ in range(N)]

# 変換器
def f(s):
    res = ''
    for c in str(s):
        c = int(c)
        k = B.index(c)
        res += str(k)
    return int(res)
 
L = []
for i, a in enumerate(A):
    L.append((i, f(a)))
L_sort = sorted(L, key=lambda x:x[1])
 
for enum in L_sort:
    idx = enum[0]
    print(A[idx])
