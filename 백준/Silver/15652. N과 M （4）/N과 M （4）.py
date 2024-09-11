def dfs(k, s, arr):
    if k == m:
        ans.append(arr)
        return
    else:
        for i in range(s, n + 1):
            dfs(k + 1, i, arr + [i])

n, m = map(int, input().split())
ans = []
dfs(0, 1, [])
for lst in ans:
    print(*lst)