sum = 0
for _ in range(5):
    a = int(input())
    if a >= 40:
        sum += a
    else:
        sum += 40
print(sum // 5)