N, M = map(int, input().split())
arrays = [i for i in range(1, N + 1)]
for _ in range(M):
    ai = int(input())
    arrays.remove(ai)
    arrays.insert(0, ai)

for a in arrays:
    print(a)