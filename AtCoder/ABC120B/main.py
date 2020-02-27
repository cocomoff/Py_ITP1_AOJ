A, B, K = list(map(int, input().split()))

def factors(i):
    ans = []
    for j in range(1, i + 1):
        if i % j == 0:
            ans.append(j)
    return ans

fA = factors(A)
fB = factors(B)

AB = [a for a in fA if a in fB]
# print(A, fA)
# print(B, fB)
# print(AB)
print(AB[::-1][K - 1])