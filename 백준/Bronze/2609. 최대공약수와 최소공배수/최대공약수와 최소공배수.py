n1, n2 = map(int, input().split())
a, b = max(n1, n2), min(n1, n2)
while True:
    if a % b == 0:
        break
    else:
        a, b = b, a % b
print(b)
print(n1 * n2 // b)