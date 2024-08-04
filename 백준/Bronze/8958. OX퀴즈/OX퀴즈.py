n = int(input())
ox = []
for _ in range(n):
    ox.append(input())
for i in range(n):
    score, count = 0, 0
    for j in ox[i]:
        if j == 'O':
            count += 1
            score += count
        else:
            count = 0
    print(score)