from itertools import combinations, permutations

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
start, link = [], []
c = list(combinations(range(n), n // 2))
ans = 1000000000
for start in c:
    link = tuple(set(range(n)) - set(start))
    s, l = 0, 0
    for i, j in list(permutations(start, 2)):
        s += arr[i][j]
    for i, j in list(permutations(link, 2)):
        l += arr[i][j]
    ans = min(ans, abs(s - l))
print(ans)