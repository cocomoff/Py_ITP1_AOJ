# -*- coding: utf-8 -*-

while True:
    m, f, r = list(map(int, input().split()))
    if m == -1 and f == -1 and r == -1:
        break

    grade = None
    if m < 0 or f < 0:
        grade = "F"
    elif m + f >= 80:
        grade = "A"
    elif m + f >= 65:
        grade = "B" 
    elif m + f >= 50:
        grade = "C"
    elif m + f >= 30:
        grade = "D"
        if r >= 50:
            grade = "C"
    else:
        grade = "F"
    print(grade)