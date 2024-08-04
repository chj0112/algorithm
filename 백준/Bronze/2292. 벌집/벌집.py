n = int(input())
count = 0
pre = 1
while True:
    count += 1
    if n <= pre + (6 * (count - 1)):
        break
    pre += 6 * (count - 1)
print(count)