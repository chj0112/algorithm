def dfs(k):
    if k == m:
        print(*ans)
        return
    else:
        for i in range(1, n + 1):
            if v[i] == 0:
                ans[k] = i
                v[i] = 1
                dfs(k + 1)
                v[i] = 0
                
n, m = map(int, input().split())
ans = [0] * m
v = [0] * (n + 1)
dfs(0)