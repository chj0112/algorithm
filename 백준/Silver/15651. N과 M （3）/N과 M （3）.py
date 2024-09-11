def dfs(k, arr):
    if k == m:
        ans.append(arr)
        return
    else:
        for i in range(1, n + 1):
            dfs(k + 1, arr + [i])

n, m = map(int, input().split())
ans = []
dfs(0, [])
for lst in ans:
    print(*lst)