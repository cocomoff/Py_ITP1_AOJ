# -*- coding: utf-8 -*-

counter = 1
while True:
    s = int(input())
    if s == 0:
        break
    print("Case {}: {}".format(counter, s))
    counter += 1