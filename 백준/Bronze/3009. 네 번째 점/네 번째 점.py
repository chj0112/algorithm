a, b = [0, 0, 0], [0, 0, 0]
for i in range(3):
    a[i], b[i] = map(int, input().split())
a.sort()
b.sort()
if a[0] != a[1]:
    x = a[0]
else:
    x = a[2]
if b[0] != b[1]:
    y = b[0]
else:
    y = b[2]
print(x, y)