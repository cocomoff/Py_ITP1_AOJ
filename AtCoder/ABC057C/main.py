N = int(input())

def F(A, B):
    a = len(str(A))
    b = len(str(B))
    return max(a, b)

fmin = 1000000000
for a in range(1, int(N ** 0.5) + 1):
    b = N // a
    if a * b == N:
        fmin = min(fmin, F(a, b))
print(fmin)