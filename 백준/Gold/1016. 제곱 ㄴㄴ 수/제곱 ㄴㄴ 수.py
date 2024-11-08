min, max = map(int, input().split())
num = set()
for i in range(2, int(max ** 0.5) + 1):
    for j in range(((min - 1) // (i * i) + 1) * i * i, max + 1, i * i):
        num.add(j)
print(max - min + 1 - len(num))