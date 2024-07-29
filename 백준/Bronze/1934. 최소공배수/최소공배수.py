import sys

t = int(sys.stdin.readline())
for i in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if a > b:
        max = a
        min = b
    else:
        max = b
        min = a
    while min > 0:
        max, min = min, max % min
    gcd = max
    lcm = a * b // gcd
    sys.stdout.write(str(lcm) + '\n')