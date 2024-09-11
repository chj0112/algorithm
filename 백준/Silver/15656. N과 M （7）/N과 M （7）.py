def dfs(k, arr):
    if k == m:
        ans.append(arr)
        return
    else:
        for i in range(0, n):
            dfs(k + 1, arr + [lst[i]])

n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
ans = []
dfs(0, [])
for lst in ans:
    print(*lst)