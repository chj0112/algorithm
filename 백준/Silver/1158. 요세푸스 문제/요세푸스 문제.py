n, k = map(int, input().split())
arr = [i + 1 for i in range(n)]
result = []
point = -1
while arr:
    point += k
    while point >= len(arr):
        point -= len(arr)
    result.append(arr.pop(point))
    point -= 1
print(str(result).replace('[', '<').replace(']', '>'))