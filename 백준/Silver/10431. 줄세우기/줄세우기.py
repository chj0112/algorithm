p = int(input())
for i in range(p):
    t = list(map(int, input().split()))
    cnt = 0
    for j in range(2, 21):
        for k in range(1, j):
            if t[j] < t[k]:
                cnt += 1
                t[j], t[k] = t[k], t[j]
    print(t[0], cnt)