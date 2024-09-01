t = int(input())
for i in range(t):
    n = int(input())
    team = list(map(int, input().split()))
    for j in range(1, max(team) + 1):
        if team.count(j) != 6:
            team[:] = (v for v in team if v != j)
    win = 0
    win_score = [10000, 10000, 10000, 10000, 10000, 10000]
    for k in set(team):
        score = list(filter(lambda x: team[x] == k, range(len(team))))
        if sum(score[:4]) < sum(win_score[:4]):
            win = k
            win_score = score
        elif sum(score[:4]) == sum(win_score[:4]):
            if score[4] < win_score[4]:
                win = k
    print(win)
