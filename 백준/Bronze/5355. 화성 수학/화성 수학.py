import sys

t = int(sys.stdin.readline())
for i in range(t):
    line = sys.stdin.readline().rstrip().split()
    line[0] = float(line[0])
    while len(line) > 1:
        if line[1] == '@':
            line[0] *= 3
        elif line[1] == '%':
            line[0] += 5
        elif line[1] == '#':
            line[0] -= 7
        line.pop(1)
    sys.stdout.write("%.2f\n" %(line[0]))