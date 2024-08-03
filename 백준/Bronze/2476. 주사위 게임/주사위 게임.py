import sys

n = int(input())
prize = 0
for _ in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    money = 0
    if a[0] == a[1] == a[2]:
        money = 10000 + a[0] * 1000
    elif a[0] == a[1] or a[1] == a[2]:
        money = 1000 + a[1] * 100
    else:
        money = 100 * a[2]
    if prize < money:
        prize = money
print(prize)