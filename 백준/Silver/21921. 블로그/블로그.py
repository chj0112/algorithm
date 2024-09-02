n, x = map(int, input().split())
visitors = list(map(int, input().split()))
m = sum(visitors[:x])
d = 1
prev = m
for i in range(x, n):
    sum = prev + visitors[i] - visitors[i - x]
    if sum > m:
        m = sum
        d = 1
    elif sum == m:
        d += 1
    prev = sum
if m == 0:
    print("SAD")
else:
    print(m)
    print(d)