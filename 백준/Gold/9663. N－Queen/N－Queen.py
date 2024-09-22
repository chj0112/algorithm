def recursive(k):
    global result
    if k == n:
        result += 1
        return
    for i in range(n):
        if v1[i] == v2[k + i] == v3[k - i] == 0:
            v1[i] = v2[k + i] = v3[k - i] = 1
            recursive(k + 1)
            v1[i] = v2[k + i] = v3[k - i] = 0

n = int(input())
v1 = [0] * n # 세로 열
v2 = [0] * (2 * n - 1) # 합 판별 대각선
v3 = [0] * (2 * n - 1) # 차 판별 대각선
result = 0
recursive(0)
print(result)