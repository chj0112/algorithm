n = int(input())
district = sorted(list(map(int, input().split())))
total = int(input())
answer = district[-1]
for i in district:
    if i >= total / n:
        answer = total // n
        break
    else:
        n -= 1
        total -= i
print(answer)