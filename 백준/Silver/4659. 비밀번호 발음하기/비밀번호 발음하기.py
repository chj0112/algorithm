import sys

v = ['a', 'e', 'i', 'o', 'u']
while True:
    p = sys.stdin.readline().rstrip()
    if p == "end":
        break
    check = 0
    if len(set(v) & set(p)) == 0:
        check = 1
    for i in range(1, len(p)):
        if p[i] == p[i - 1]:
            if p[i] != 'e' and p[i] != 'o':
                check = 1
                break
        if i == 1:
            continue
        if (p[i] in v and p[i - 1] in v and p[i - 2] in v) or (p[i] not in v and p[i - 1] not in v and p[i - 2] not in v):
            check = 1
            break
    if check == 0:
        sys.stdout.write("<{}> is acceptable.\n".format(p))
    else:
        sys.stdout.write("<{}> is not acceptable.\n".format(p))