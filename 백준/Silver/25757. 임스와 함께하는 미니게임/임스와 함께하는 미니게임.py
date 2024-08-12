import sys

n, g = input().split()
game = ['Y', 'F', 'O']
arr = []
for i in range(int(n)):
    arr.append(sys.stdin.readline())
print(len(set(arr)) // (game.index(g) + 1))