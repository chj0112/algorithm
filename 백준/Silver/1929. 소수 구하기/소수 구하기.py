m, n = map(int, input().split())
dp = [0, 0] + [1] * n
for i in range(2, int(n ** (1 / 2)) + 1):
    if dp[i] == 1:
        for j in range(i + i, n + 1, i):
            dp[j] = 0
for k in range(m, n + 1):
    if dp[k] == 1:
        print(k)