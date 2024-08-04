import sys

m = int(input())
s = []
for i in range(m):
    a = sys.stdin.readline().rstrip()
    if a == "all":
        s = [str(i + 1) for i in range(20)]
    elif a == "empty":
        s = []
    else:
        a1, a2 = a.split()
        if a1 == "add":
            if a2 not in s:
                s.append(a2)
        elif a1 == "remove":
            if a2 in s:
                s.remove(a2)
        elif a1 == "check":
            sys.stdout.write('1\n' if a2 in s else '0\n')
        elif a1 == "toggle":
            if a2 in s:
                s.remove(a2)
            else:
                s.append(a2)