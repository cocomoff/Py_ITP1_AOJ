s = input()
p = input()

# print(s)
for i in range(len(s)):
    pre = s[:i]
    post = s[i:]
    new_s = post + pre
    if new_s[:len(p)] == p:
        print("Yes")
        exit(0)

print("No")