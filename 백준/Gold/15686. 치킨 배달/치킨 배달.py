def backtracking(k, s, lst):
    if k == m:
        result = 0
        for i in range(len(house)):
            tmp = 100000
            for j in lst:
                d = abs(house[i][0] - chicken[j][0]) + abs(house[i][1] - chicken[j][1])
                tmp = min(tmp, d)
            result += tmp
        arr.append(result)
        return
    for i in range(s, len(chicken)):
        backtracking(k + 1, i + 1, lst + [i])
                

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
house = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))
arr = []
backtracking(0, 0, [])
print(min(arr))