a, b = map(int, input().split())
c = int(input())
new_a = a + (b + c) // 60
new_b = (b + c) % 60
while new_a >= 24:
    new_a -= 24
print(new_a, new_b)