switch = int(input())
arr = list(map(int, input().split()))
student = int(input())
for i in range(student):
    s, n = map(int, input().split())
    if s == 1:
        for j in range(n - 1, len(arr), n):
            arr[j] = int(not arr[j])
    if s == 2:
        arr[n - 1] = int(not arr[n - 1])
        for k in range(1, min(n - 1, len(arr) - n) + 1):
            if arr[n - 1 - k] != arr[n - 1 + k]:
                break
            else:
                arr[n - 1 - k] = int(not(arr[n - 1 - k]))
                arr[n - 1 + k] = int(not(arr[n - 1 + k]))
for l in range(0, len(arr)):
    print(arr[l], end=('\n' if l % 20 == 19 else ' '))