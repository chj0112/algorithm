from collections import deque

case = int(input())
for _ in range(case):
    n, m = map(int, input().split())
    queue = deque(map(int, input().split()))
    arr = []
    res = 0
    while queue:
        if queue[0] >= max(queue):
            if m == 0:
                res = len(arr) + 1
                break
            else:
                arr.append(queue.popleft())
                m -= 1
        else:
            queue.append(queue.popleft())
            if m == 0:
                m = len(queue) - 1
            else:
                m -= 1
    print(res)