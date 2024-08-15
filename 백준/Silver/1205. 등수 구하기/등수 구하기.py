n, s, p = map(int, input().split())
if n > 0:
    arr = list(map(int, input().split())) + [-1] * (p - n)
else:
    print(1)
    exit()
flag = 0
for i in range(p):
    if s > arr[i]:
        if flag != 0:
            print(flag)
            exit()
        else:
            print(arr.index(arr[i]) + 1)
            exit()
    elif s == arr[i]:
        flag = arr.index(arr[i]) + 1
print(-1)