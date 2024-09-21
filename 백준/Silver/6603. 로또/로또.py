def lotto(n, start, arr):
    if n == 6:
        ans.append(arr)
        return
    else:
        for i in range(start, k):
            lotto(n + 1, i + 1, arr + [s[i]])
            

while True:
    k, *s = map(int, input().split())
    if k == 0:
        break
    ans = []
    lotto(0, 0, [])
    for j in ans:
        print(*j)
    print()