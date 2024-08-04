n, k = map(int, input().split())
arr = []
find = []
for _ in range(n):
    medal = list(map(int, input().split()))
    arr.append(medal[1:])
    if medal[0] == k:
        find = medal[1:]
sorted_arr = sorted(arr, key= lambda x: (-x[0], -x[1], -x[2]))
print(sorted_arr.index(find) + 1)