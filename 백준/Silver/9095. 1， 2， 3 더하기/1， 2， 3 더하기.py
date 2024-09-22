def recursive(arr):
    global result
    if sum(arr) == n:
        result += 1
        return
    elif sum(arr) <= n:
        for i in range(3):
            recursive(arr + [i + 1])

t = int(input())
for _ in range(t):
    n = int(input())
    result = 0
    recursive([])
    print(result)