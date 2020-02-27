import sys
import string

counter = {c: 0 for c in string.ascii_letters}
input_str = sys.stdin.read()

for char in input_str:
    char = char.lower()
    if char in string.ascii_letters:
        counter[char] += 1

for c in string.ascii_lowercase:
    v = 0 if c not in counter else counter[c]
    print('{} : {}'.format(c, v))
