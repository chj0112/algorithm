import sys

n = int(input())
for _ in range(n):
    r, e, c = map(int, sys.stdin.readline().split())
    m = e - r - c
    if m > 0:
        sys.stdout.write("advertise\n")
    elif m < 0:
        sys.stdout.write("do not advertise\n")
    else:
        sys.stdout.write("does not matter\n")