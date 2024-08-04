t = int(input())
a, b, c = 0, 0, 0
while t >= 300:
    t -= 300
    a += 1
while t >= 60:
    t -= 60
    b += 1
while t >= 10:
    t -= 10
    c += 1
if t == 0:
    print(a, b, c)
else:
    print(-1)