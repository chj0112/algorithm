from collections import deque

def bfs(n):
    v[n] = 1
    q = deque()
    q.append(n)
    while q:
        c = q.popleft()
        if c == k:
            print(v[c] - 1)
            exit(0)
        if c - 1 >= 0 and v[c - 1] == 0:
            v[c - 1] = v[c] + 1
            q.append(c - 1)
        if c + 1 <= k and v[c + 1] == 0:
            v[c + 1] = v[c] + 1
            q.append(c + 1)
        if 2 * c > 200000:
            continue
        if v[2 * c] == 0:
            v[2 * c] = v[c] + 1
            q.append(2 * c)

n, k = map(int, input().split())
v = [0] * 200001
bfs(n)