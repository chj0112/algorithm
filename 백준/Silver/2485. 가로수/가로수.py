import math, sys

n = int(input())
tree = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
d = []
for i in range(1, len(tree)):
    d.append(tree[i] - tree[i - 1])
print((tree[-1] - tree[0]) // math.gcd(*d) + 1 - len(tree))