import sys
input = sys.stdin.readline

n = int(input())
stk = list()
for i in range(n):
    cmd = input().rstrip().split()
    if cmd[0] == "push":
        stk.append(cmd[1])
    elif cmd[0] == "pop":
        if not stk:
            print(-1)
        else:
            print(stk.pop())
    elif cmd[0] == "size":
        print(len(stk))
    elif cmd[0] == "empty":
        if not stk:
            print(1)
        else:
            print(0)
    elif cmd[0] == "top":
        if not stk:
            print(-1)
        else:
            print(stk[-1])