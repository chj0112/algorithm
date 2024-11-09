def dfs(x, y):
    map[x][y] = 2
    global cnt
    cnt += 1
    for i in range(4):
        if x + dx[i] >= 0 and x + dx[i] < n and y + dy[i] >= 0 and y + dy[i] < n and map[x + dx[i]][y + dy[i]] == 1:
            dfs(x + dx[i], y + dy[i])

n = int(input())
map = [list(map(int, input())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
total = 0
arr = []
for i in range(n):
    for j in range(n):
        if map[i][j] == 1:
            cnt = 0
            dfs(i, j)
            arr.append(cnt)
            total += 1
print(total)
for i in sorted(arr):
    print(i)