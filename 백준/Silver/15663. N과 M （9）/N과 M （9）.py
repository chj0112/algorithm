def dfs(k, arr):
    if k == m:
        ans.append(arr)
        return
    prev = 0
    for i in range(n):
        if v[i] == 0 and prev != lst[i]:
            prev = lst[i]
            v[i] = 1
            dfs(k + 1, arr + [lst[i]])
            v[i] = 0

n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
ans = []
v = [0] * n
dfs(0, [])
for j in ans:
    print(*j)