from collections import deque

t = int(input())
for _ in range(t):
    p = input()
    n = int(input())
    arr_str = input().strip('[ ]')
    arr = deque(map(int, arr_str.split(','))) if n != 0 else deque()
    flag = 0
    for i in p:
        if i == 'R':
            flag += 1
        elif i == 'D':
            if not arr:
                flag = -1
                break
            if flag % 2 == 0:
                arr.popleft()
            else:
                arr.pop()
    if flag % 2 == 1:
        arr.reverse()
    print(str(list(arr)).replace(' ', '') if flag != -1 else "error")