n = int(input())
A, B = 0, 0

for _ in range(n):
    s1, s2 = input().split()
    if s1 < s2:
        B += 3
    elif s1 > s2:
        A += 3
    else:
        A += 1
        B += 1

print(A, B)