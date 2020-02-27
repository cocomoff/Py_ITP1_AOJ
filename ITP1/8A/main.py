s = input()

ans_s = ''
for c in s:
    if c.isupper():
        ans_s += c.lower()
    elif c.islower():
        ans_s += c.upper()
    else:
        ans_s += c

print(ans_s)