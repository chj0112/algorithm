import math

n = int(input())
m = int(input())
x = list(map(int, input().split()))
h = x[0]
p = 0
for i in x:
    if math.ceil((i - p) / 2) > h:
        h = math.ceil((i - p) / 2)
    p = i
if n - p > h:
    h = n - p
print(h)