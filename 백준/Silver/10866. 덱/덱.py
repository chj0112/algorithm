from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
dq = deque()
for i in range(n):
    cmd = input().rstrip().split()
    if cmd[0] == "push_front":
        dq.appendleft(cmd[1])
    elif cmd[0] == "push_back":
        dq.append(cmd[1])
    elif cmd[0] == "pop_front":
        if not dq:
            print(-1)
        else:
            print(dq.popleft())
    elif cmd[0] == "pop_back":
        if not dq:
            print(-1)
        else:
            print(dq.pop())
    elif cmd[0] == "size":
        print(len(dq))
    elif cmd[0] == "empty":
        if not dq:
            print(1)
        else:
            print(0)
    elif cmd[0] == "front":
        if not dq:
            print(-1)
        else:
            print(dq[0])
    elif cmd[0] == "back":
        if not dq:
            print(-1)
        else:
            print(dq[-1])