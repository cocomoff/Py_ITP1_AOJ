s = input()
n = int(input())

for _ in range(n):
    line = input().split()
    if line[0] == 'replace':
        a, b = int(line[1]), int(line[2])
        # print(s[:a], s[a:b+1], s[b+1:])
        s = s[:a] + line[3] + s[b+1:]
        # print(s)
    elif line[0] == 'reverse':
        a, b = int(line[1]), int(line[2])
        s = s[:a] + s[a:b+1][::-1] + s[b+1:]
    else:
        a, b = int(line[1]), int(line[2])
        print(s[a:b + 1])