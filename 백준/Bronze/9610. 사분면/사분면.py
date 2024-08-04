import sys

n = int(input())
q1, q2, q3, q4, axis = 0, 0, 0, 0, 0
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if x == 0 or y == 0:
        axis += 1
    elif x > 0:
        if y > 0:
            q1 += 1
        else:
            q4 += 1
    else:
        if y > 0:
            q2 += 1
        else:
            q3 += 1
print("Q1: {}\nQ2: {}\nQ3: {}\nQ4: {}\nAXIS: {}".format(q1, q2, q3, q4, axis))