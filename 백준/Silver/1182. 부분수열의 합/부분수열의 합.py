from itertools import combinations
n, s = map(int, input().split())
lst = list(map(int, input().split()))
answer = 0
for i in range(n):
    comb = list(combinations(lst, i + 1))
    for j in comb:
        if sum(j) == s:
            answer += 1
print(answer)