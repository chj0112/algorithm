n, g = input().split()
game = ['Y', 'F', 'O']
arr = []
for i in range(int(n)):
    p = input()
    arr.append(p)
print(len(set(arr)) // (game.index(g) + 1))