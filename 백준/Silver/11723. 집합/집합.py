import sys

m = int(input())
s = []
for i in range(m):
    a = sys.stdin.readline().rstrip().split()
    if a[0] == "add":
        if int(a[1]) not in s:
            s.append(int(a[1]))
    elif a[0] == "remove":
        if int(a[1]) in s:
            s.remove(int(a[1]))
    elif a[0] == "check":
        sys.stdout.write('1\n' if int(a[1]) in s else '0\n')
    elif a[0] == "toggle":
        if int(a[1]) in s:
            s.remove(int(a[1]))
        else:
            s.append(int(a[1]))
    elif a[0] == "all":
        s = [i + 1 for i in range(20)]
    elif a[0] == "empty":
        s = []