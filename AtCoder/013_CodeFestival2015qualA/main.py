N, T = map(int, input().split())
A, B = [], []
AB = []

for _ in range(N):
    ai, bi = map(int, input().split())
    A.append(ai)
    B.append(bi)
    AB.append((ai, bi))

AB = sorted(AB, key=lambda x: x[0] - x[1], reverse=True)

if sum(B) > T:
    print(-1)
    exit()

if sum(A) < T:
    print(0)
    exit()

now = sum(A)

count = 0
index = 0
while now > T:
    ai, bi = AB[index]
    now = now - ai + bi
    index += 1
    count += 1

print(count)