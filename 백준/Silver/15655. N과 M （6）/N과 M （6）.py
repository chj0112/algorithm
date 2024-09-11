def dfs(k, s, arr):
    if k == m:
        ans.append(arr)
        return
    else:
        for i in range(s, n):
            dfs(k + 1, i + 1, arr + [lst[i]])

n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
ans = []
dfs(0, 0, [])
for lst in ans:
    print(*lst)