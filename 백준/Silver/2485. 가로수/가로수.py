import math

n = int(input())
tree = []
for _ in range(n):
    tree.append(int(input()))
d = set()
for i in range(1, len(tree)):
    d.add(tree[i] - tree[i - 1])
print((tree[-1] - tree[0]) // math.gcd(*d) + 1 - len(tree))