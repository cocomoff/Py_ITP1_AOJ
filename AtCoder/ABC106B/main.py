N = int(input())

def factors(i):
    ans = []
    for j in range(1, i + 1):
        if i % j == 0:
            ans.append(j)
    return ans

count = 0
for i in range(3, N + 1, 2):
    fi = factors(i)
    # print(i, fi)
    if len(fi) == 8:
        count += 1
print(count)