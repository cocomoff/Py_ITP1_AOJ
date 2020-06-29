# https://atcoder.jp/contests/dwango2015-prelims/tasks/dwango2015_prelims_2

from math import factorial

S = input()
N = len(S)

# fast fact
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
def comb(n, k):
    return factorial(n) // factorial(k) // factorial(n - k)


# Sの連結する25を探す
i = 0
pos = []
while i + 1 < N:
    j = i
    while j + 1 < N and S[j] == '2' and S[j+1] == '5':
        j += 2
    if i < j:
        # print(i, j, S[i:j])
        pos.append(S[i:j])
    i = j + 1

# print(S, pos)
ans = 0
for ss in pos:
    num = len(ss) // 2
    ans_num = 0
    for k in range(1, num + 1):
        # print(num, k, comb(num, k), num - k + 1)
        # ans_num += comb(num, k)
        ans_num += (num - k + 1)
    # print(num, ans_num)
    ans += ans_num
print(ans)