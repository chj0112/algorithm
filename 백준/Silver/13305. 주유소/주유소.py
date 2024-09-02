n = int(input())
road = list(map(int, input().split()))
city = list(map(int, input().split()))
cost = 0
prev = 1000000001
for i in range(len(road)):
    if city[i] < prev:
        prev = city[i]
    cost += prev * road[i]
print(cost)