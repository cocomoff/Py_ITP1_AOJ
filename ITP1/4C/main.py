# -*- coding: utf-8 -*-

while True:
    a, op, b = input().split()
    a = int(a)
    b = int(b)

    if op == '?':
        break
    elif op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    else:
        print(a // b)