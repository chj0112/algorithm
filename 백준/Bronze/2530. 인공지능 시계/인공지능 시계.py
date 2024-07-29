a, b, c = map(int, input().split())
d = int(input())
new_c = (c + d) % 60
new_b = b + (c + d) // 60
new_a = a
while new_b >= 60:
    new_b -= 60
    new_a += 1
while new_a >= 24:
    new_a -= 24
print(new_a, new_b, new_c)