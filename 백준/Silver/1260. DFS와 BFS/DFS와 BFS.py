def dfs(here):
    visited1[here] = True
    d.append(here)
    for i in adj[here]:
        if not visited1[i]:
            dfs(i)

def bfs(here):
    visited2[here] = 1
    q = []
    q.append(here)
    while q:
        here = q.pop(0)
        b.append(here)
        for i in adj[here]:
            if visited2[i] == 0:
                visited2[i] = visited2[here] + 1
                q.append(i)

n, m, v = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
for i in adj:
    i.sort()
visited1 = [False] * (n + 1)
visited2 = [0] * (n + 1)
d = []
b = []
dfs(v)
bfs(v)
print(*d)
print(*b)