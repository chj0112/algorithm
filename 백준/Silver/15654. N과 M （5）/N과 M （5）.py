def dfs(k, arr):
    if k == m:
        ans.append(arr)
        return
    else:
        for i in range(0, n):
            if v[i] == 0:
                v[i] = 1
                dfs(k + 1, arr + [lst[i]])
                v[i] = 0

n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
v = [0] * n
ans = []
dfs(0, [])
for lst in ans:
    print(*lst)